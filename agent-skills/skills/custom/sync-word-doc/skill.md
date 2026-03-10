---
name: sync-word-doc
description: Sync a markdown file to a SharePoint/OneDrive Word document via Word COM automation -- use when you need to push markdown content to an active Word doc
user-invocable: true
argument-hint: "<markdown-path> <sharepoint-url>"
---

# Sync Markdown to Word Document

Push/pull markdown content to/from an active SharePoint/OneDrive Word document using Word COM automation (C#, Markdig + typed Office Interop). Works with documents that are open and locked by SharePoint -- COM edits through Word itself.

## Arguments

- `$0` -- path to the local markdown file
- `$1` -- SharePoint/OneDrive sharing URL for the target Word document

## Prerequisites

- Windows, Word desktop app installed
- .NET 10 SDK
- mmdc (Mermaid CLI): `npm install -g @mermaid-js/mermaid-cli`

## Install / Update

The tool is published to the renli.feed NuGet feed as a dotnet global tool.

```powershell
# First-time install
dotnet tool install --global sync-word-doc --add-source "https://pkgs.dev.azure.com/microsoft/OS.Developer/_packaging/renli.feed/nuget/v3/index.json"

# Update to latest
dotnet tool update --global sync-word-doc --add-source "https://pkgs.dev.azure.com/microsoft/OS.Developer/_packaging/renli.feed/nuget/v3/index.json"
```

**When invoking this skill, always ensure the tool and dependencies are available and up to date:**

```powershell
# Ensure sync-word-doc is installed/updated
$installed = dotnet tool list --global | Select-String "sync-word-doc"
if ($installed) {
    dotnet tool update --global sync-word-doc --add-source "https://pkgs.dev.azure.com/microsoft/OS.Developer/_packaging/renli.feed/nuget/v3/index.json"
} else {
    dotnet tool install --global sync-word-doc --add-source "https://pkgs.dev.azure.com/microsoft/OS.Developer/_packaging/renli.feed/nuget/v3/index.json"
}

# Ensure mmdc (Mermaid CLI) is installed
$hasMmdc = Get-Command mmdc -ErrorAction SilentlyContinue
if (-not $hasMmdc) {
    npm install -g @mermaid-js/mermaid-cli
}
```

## Usage

```powershell
# Push markdown to Word (incremental diff -- only changed paragraphs updated)
sync-word-doc push <markdown-path> <sharepoint-url>

# Push with full rewrite (destructive -- clears and rewrites entire doc)
sync-word-doc push <markdown-path> <sharepoint-url> --full

# Pull Word doc to markdown
sync-word-doc pull <sharepoint-url> <markdown-path>

# Preview diff without applying changes
sync-word-doc diff <markdown-path> <sharepoint-url>

# List comments on the document
sync-word-doc comments list <sharepoint-url>

# Add a comment to a paragraph
sync-word-doc comments add <sharepoint-url> <para_index> <text>
```

If `<sharepoint-url>` is omitted for push/diff, it's read from the `sharepoint` key in the markdown file's YAML frontmatter.

SharePoint auto-syncs after save.

## What It Converts

| Markdown | Word Output |
|---|---|
| `# ## ###` | Heading 1, 2, 3 |
| `- bullet` | Bullet list (nested lists supported) |
| `1. item` | Numbered list |
| `**bold**` | Bold (inline, position-accurate) |
| `*italic*` | Italic (inline) |
| `[text](url)` | Clickable hyperlink |
| `` `code` `` | Inline code (Consolas font) |
| ` ``` block ``` ` | Code block (Consolas, compact spacing) |
| ` ```mermaid ``` ` | Rendered PNG image (via mmdc) |
| `> blockquote` | Quote style paragraph |
| `\| table \|` | Native Word table with bold headers and proportional column widths |
| YAML frontmatter | Stored as Word custom document properties |
| `---` | Skipped |

## Sync Modes

### Incremental (default)

Parses both the markdown source and existing Word document into paragraph-level elements, diffs them, and applies only the changes. Manual edits and comments in unchanged sections are preserved.

- **Replace**: text changed in a matching paragraph -> update in-place (uses Find/Replace to preserve paragraph marks)
- **Insert**: new paragraphs added -> insert at correct position
- **Delete**: paragraphs removed from markdown -> delete from Word
- **Fallback**: if >60% of content changed, automatically falls back to full rewrite

### Full Rewrite (`--full`)

Clears the entire doc and rewrites from scratch. Use when incremental produces unexpected results, or for the initial sync. Deletes all comments.

## Known Documents

| Markdown Source | Word Doc (SharePoint) | Description |
|---|---|---|
| `docs/fhl-2026/executive-summary.md` | [FHL March 2026.docx](https://microsoft.sharepoint-df.com/:w:/t/WindowsExperiences/cQrKW_wAfWuAT7pi5ctDMen-EgUC-S0AmV6iPaIJqdi2Hg9dTw) | FHL executive summary |
| `docs/fhl-2026/learning-day-plan.md` | [FHL March 2026 Learning Sessions.docx](https://microsoft.sharepoint-df.com/:w:/t/WindowsExperiences/cQobN1-IC3MlQ7M7hFozal-EEgUCuG9pQpZ01hcNdonH87NB5w) | Workshop day plan |

**Test doc** (safe to overwrite): [testdoc.docx](https://microsoft-my.sharepoint-df.com/:w:/p/renli/cQoCPht8ShG3SK-adtPPsQq3EgUCGUn2jaTLBPp6X1R7BlBI5Q)

## Known Limitations

- No image support (except mermaid diagrams)
- Table cells: whole-cell bold only (no per-word bold in cells)
- Incremental diff on tables operates at the row level, not cell level
- Nested list depth detection during pull may not capture all indent levels

## Troubleshooting

- **"Failed to open"** -- Open the URL manually in Word first to authenticate, then retry.
- **Lock errors via Graph API** -- Use this COM approach instead; COM works through Word and bypasses locks.
- **"mmdc not found" warning** -- Install with `npm install -g @mermaid-js/mermaid-cli`.
