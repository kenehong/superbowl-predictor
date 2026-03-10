# Install/update external skills from the skills manifest (Windows).
# Uses gh CLI to clone specific paths from GitHub repos.

function Compare-DirectoriesIgnoringLineEndings {
    param([string]$Left, [string]$Right)

    $git = Get-Command git -ErrorAction SilentlyContinue
    if (-not $git) { return $false }

    & $git.Source diff --no-index --ignore-cr-at-eol --exit-code -- $Left $Right *> $null
    if ($LASTEXITCODE -eq 0) { return $true }
    if ($LASTEXITCODE -eq 1) { return $false }
    return $false
}

function Install-SkillFromGitHub {
    param(
        [string]$Repo,
        [string]$Path,
        [string]$Ref,
        [string]$Dest,
        [string]$Name
    )

    $tempDir = Join-Path ([System.IO.Path]::GetTempPath()) ("skill-clone-" + [Guid]::NewGuid().ToString("N"))

    try {
        # Sparse clone: only the skill path
        git clone --depth 1 --branch $Ref --filter=blob:none --sparse "https://github.com/$Repo.git" $tempDir 2>$null
        if ($LASTEXITCODE -ne 0) { return $false }

        Push-Location $tempDir
        git sparse-checkout set $Path 2>$null
        Pop-Location

        $sourcePath = Join-Path $tempDir $Path
        if (-not (Test-Path $sourcePath)) { return $false }

        $destPath = Join-Path $Dest $Name
        if (Test-Path $destPath) { Remove-Item $destPath -Recurse -Force }
        Copy-Item $sourcePath $destPath -Recurse -Force
        return $true
    }
    finally {
        if (Test-Path $tempDir) {
            Remove-Item $tempDir -Recurse -Force -ErrorAction SilentlyContinue
        }
    }
}

function Update-Skills {
    param([string]$RepoDir)

    $skillsDir = Join-Path $RepoDir "skills\external"
    $manifestPath = Join-Path $RepoDir "scripts\skills-manifest.json"

    if (-not (Test-Path $manifestPath)) { Write-Err "Missing manifest: $manifestPath"; return 1 }

    $manifest = Get-Content $manifestPath -Raw | ConvertFrom-Json
    $skills = @($manifest.skills)
    $count = $skills.Count

    if ($count -eq 0) {
        Write-Info "No external skills in manifest."
        return 0
    }

    New-Item -ItemType Directory -Path $skillsDir -Force | Out-Null

    $updated = 0
    $skipped = 0
    $failed = 0
    $tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("skills-update-" + [Guid]::NewGuid().ToString("N"))
    New-Item -ItemType Directory -Path $tempRoot -Force | Out-Null

    Write-Info "Updating $count skills from manifest..."

    try {
        foreach ($skill in $skills) {
            $name = [string]$skill.name
            $repo = [string]$skill.repo
            $path = [string]$skill.path
            $ref = if ($skill.PSObject.Properties.Name -contains "ref" -and $skill.ref) { [string]$skill.ref } else { "main" }

            if (-not $name -or -not $repo -or -not $path) {
                Write-Host "  [FAIL] Invalid manifest entry" -ForegroundColor Red
                $failed++
                continue
            }

            $dest = Join-Path $skillsDir $name
            $staged = Join-Path $tempRoot $name

            $ok = Install-SkillFromGitHub -Repo $repo -Path $path -Ref $ref -Dest $tempRoot -Name $name
            if (-not $ok -or -not (Test-Path $staged)) {
                Write-Host "  [FAIL] $name (from $repo)" -ForegroundColor Red
                $failed++
                continue
            }

            if ((Test-Path $dest) -and (Compare-DirectoriesIgnoringLineEndings $dest $staged)) {
                Remove-Item $staged -Recurse -Force
                Write-Host "  [SKIP] $name (unchanged)" -ForegroundColor Yellow
                $skipped++
                continue
            }

            if (Test-Path $dest) { Remove-Item $dest -Recurse -Force }
            Move-Item $staged $dest
            Write-Host "  [OK] $name (from $repo)" -ForegroundColor Green
            $updated++
        }
    }
    finally {
        if (Test-Path $tempRoot) {
            Remove-Item $tempRoot -Recurse -Force -ErrorAction SilentlyContinue
        }
    }

    Write-Host ""
    Write-Info "Updated: $updated, Skipped: $skipped, Failed: $failed"
    if ($failed -gt 0) { return 1 }
    return 0
}

function List-Skills {
    param([string]$RepoDir)

    $manifestPath = Join-Path $RepoDir "scripts\skills-manifest.json"

    if (-not (Test-Path $manifestPath)) { Write-Err "Missing manifest: $manifestPath"; return 1 }

    $manifest = Get-Content $manifestPath -Raw | ConvertFrom-Json
    $skills = @($manifest.skills)

    # Show local skills
    Write-Info "Local skills:"
    Write-Host ""
    $customDir = Join-Path $RepoDir "skills\custom"
    $marketDir = Join-Path $RepoDir "skills\marketplace"
    if (Test-Path $customDir) {
        foreach ($d in (Get-ChildItem $customDir -Directory)) {
            Write-Host "  [CUSTOM]      $($d.Name)" -ForegroundColor Cyan
        }
    }
    if (Test-Path $marketDir) {
        foreach ($d in (Get-ChildItem $marketDir -Directory)) {
            Write-Host "  [MARKETPLACE] $($d.Name)" -ForegroundColor Green
        }
    }

    # Show external skills
    $count = @($skills).Count
    if ($count -gt 0) {
        Write-Host ""
        Write-Info "External skills ($count in manifest):"
        Write-Host ""
        $externalDir = Join-Path $RepoDir "skills\external"
        foreach ($skill in $skills) {
            $name = [string]$skill.name
            $repo = [string]$skill.repo
            $dest = Join-Path $externalDir $name
            if (Test-Path $dest) {
                Write-Host "  [INSTALLED] $name  ($repo)" -ForegroundColor Green
            } else {
                Write-Host "  [MISSING]   $name  ($repo)" -ForegroundColor Red
            }
        }
    }

    return 0
}
