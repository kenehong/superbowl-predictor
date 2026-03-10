# Single entry point for agent-skills setup (Windows).
param(
    [Parameter(Position=0)]
    [ValidateSet("install", "link-ai-agents", "update-skills", "list-skills", "reset", "status", "project-agents")]
    [string]$Action,

    [string]$ProjectPath,
    [switch]$Help
)

# --- PowerShell 7 bootstrap (runs under PS 5.1) ---
if ($PSVersionTable.PSVersion.Major -lt 7) {
    if (-not (Get-Command pwsh -ErrorAction SilentlyContinue)) {
        if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
            Write-Host "[ERROR] winget is required. Install App Installer from the Microsoft Store." -ForegroundColor Red
            exit 1
        }
        Write-Host "[INFO] Installing PowerShell 7..." -ForegroundColor Green
        winget install --id Microsoft.PowerShell -h --accept-package-agreements --accept-source-agreements
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path","User") + ";" +
                     [System.Environment]::GetEnvironmentVariable("Path","Machine")
        if (-not (Get-Command pwsh -ErrorAction SilentlyContinue)) {
            Write-Host "[ERROR] Failed to install PowerShell 7. Install manually from https://aka.ms/powershell" -ForegroundColor Red
            exit 1
        }
    }
    Write-Host "[INFO] Re-launching under PowerShell 7..." -ForegroundColor Green
    $argList = @('-NoProfile', '-File', $MyInvocation.MyCommand.Path)
    foreach ($key in $PSBoundParameters.Keys) {
        $val = $PSBoundParameters[$key]
        if ($val -is [switch]) { if ($val) { $argList += "-$key" } }
        else { $argList += "-$key"; $argList += $val }
    }
    & pwsh @argList
    exit $LASTEXITCODE
}
# --- End bootstrap ---

$ErrorActionPreference = "Stop"
$PSNativeCommandUseErrorActionPreference = $false
$ScriptsDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoDir = Split-Path -Parent $ScriptsDir

. "$ScriptsDir\lib\helpers.ps1"
. "$ScriptsDir\lib\link-ai-agents.ps1"
. "$ScriptsDir\lib\update-skills.ps1"

if ($Help -or -not $Action) {
    Write-Host @"
Usage: setup.ps1 <command> [options]

Commands:
  install             Full setup: link AI agent configs + update skills
  link-ai-agents      Link AI agent configs only
  update-skills       Install/update external skills from manifest
  list-skills         Show skills and install status
  reset               Remove all symlinks
  status              Show current link status
  project-agents      Link agents into a project (-ProjectPath required)

Options:
  -ProjectPath <path>  Project path (for project-agents)
  -Help                Show this help
"@
    exit 0
}

function Show-Status {
    Write-Info "Current link status"
    Write-Host ""
    Write-Info "AI agent links:"
    Show-AiAgentStatus $RepoDir
}

switch ($Action) {
    "install"        { Link-AiAgents $RepoDir }
    "link-ai-agents" { Link-AiAgents $RepoDir }
    "update-skills"  { $code = Update-Skills $RepoDir; if ($code -ne 0) { exit $code } }
    "list-skills"    { $code = List-Skills $RepoDir; if ($code -ne 0) { exit $code } }
    "reset"          { Unlink-AiAgents $RepoDir }
    "status"         { Show-Status }
    "project-agents" {
        if (-not $ProjectPath) { Write-Err "Missing -ProjectPath"; exit 1 }
        if (-not (Test-Path $ProjectPath)) { Write-Err "Not a directory: $ProjectPath"; exit 1 }
        Write-Info "Linking agents into: $ProjectPath"
        Ensure-Linked "$RepoDir\agents" "$ProjectPath\.claude\agents"
    }
}

Write-Info "Done"
