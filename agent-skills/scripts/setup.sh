#!/usr/bin/env bash
# Mac/Linux setup for agent-skills — mirrors setup.ps1 behavior.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
MANIFEST="$SCRIPT_DIR/ai-agent-links.json"

# Colors
info()  { printf "\033[32m[INFO]\033[0m %s\n" "$1"; }
warn()  { printf "\033[33m[WARN]\033[0m %s\n" "$1"; }
err()   { printf "\033[31m[ERROR]\033[0m %s\n" "$1"; }

# Resolve ~ in target paths
expand_home() { echo "${1/#\~/$HOME}"; }

# Create symlink with backup
ensure_linked() {
    local source="$1" target="$2"
    local target_parent
    target_parent="$(dirname "$target")"

    [[ -e "$source" ]] || { warn "Missing source: $source, skipping"; return; }

    mkdir -p "$target_parent"

    if [[ -e "$target" || -L "$target" ]]; then
        if [[ -L "$target" ]]; then
            local current
            current="$(readlink "$target")"
            if [[ "$current" == "$source" ]]; then
                echo "  [SKIP] $target"
                return
            fi
            rm "$target"
        else
            local backup="$target.backup.$(date +%Y%m%d_%H%M%S)"
            mv "$target" "$backup"
            info "Backed up: $target -> $backup"
        fi
    fi

    ln -s "$source" "$target"
    echo "  [LINK] $source -> $target"
}

# Remove symlink and restore backup
remove_link() {
    local target="$1"
    if [[ -L "$target" ]]; then
        rm "$target"
        echo "  [REMOVED] $target"
        # Restore most recent backup
        local latest
        latest="$(ls -t "${target}.backup."* 2>/dev/null | head -1)"
        if [[ -n "$latest" ]]; then
            mv "$latest" "$target"
            echo "  [RESTORED] $target (from $(basename "$latest"))"
        fi
    elif [[ -e "$target" ]]; then
        warn "Not a symlink, skipping: $target"
    fi
}

# Parse manifest and link
link_ai_agents() {
    [[ -f "$MANIFEST" ]] || { err "Missing manifest: $MANIFEST"; exit 1; }
    info "Linking AI agent configs..."

    # Read each target entry from manifest
    local count
    count="$(python3 -c "import json; d=json.load(open('$MANIFEST')); print(len(d['targets']))")"

    for i in $(seq 0 $((count - 1))); do
        local source_key source_rel source_abs target_path
        source_key="$(python3 -c "import json; d=json.load(open('$MANIFEST')); print(d['targets'][$i]['source'])")"
        target_path="$(python3 -c "import json; d=json.load(open('$MANIFEST')); print(d['targets'][$i]['path'])")"
        source_rel="$(python3 -c "import json; d=json.load(open('$MANIFEST')); print(d['sources'].get('$source_key',''))")"

        if [[ -z "$source_rel" ]]; then
            warn "Unknown source key '$source_key', skipping"
            continue
        fi

        source_abs="$REPO_DIR/$source_rel"
        target_path="$(expand_home "$target_path")"

        ensure_linked "$source_abs" "$target_path"
    done
}

# Remove all links
unlink_ai_agents() {
    [[ -f "$MANIFEST" ]] || { err "Missing manifest: $MANIFEST"; exit 1; }
    info "Removing AI agent links..."

    local count
    count="$(python3 -c "import json; d=json.load(open('$MANIFEST')); print(len(d['targets']))")"

    for i in $(seq 0 $((count - 1))); do
        local target_path
        target_path="$(python3 -c "import json; d=json.load(open('$MANIFEST')); print(d['targets'][$i]['path'])")"
        target_path="$(expand_home "$target_path")"
        remove_link "$target_path"
    done
}

# Show status
show_status() {
    [[ -f "$MANIFEST" ]] || { err "Missing manifest: $MANIFEST"; exit 1; }
    info "Current link status:"
    echo ""

    local count
    count="$(python3 -c "import json; d=json.load(open('$MANIFEST')); print(len(d['targets']))")"

    for i in $(seq 0 $((count - 1))); do
        local target_path
        target_path="$(python3 -c "import json; d=json.load(open('$MANIFEST')); print(d['targets'][$i]['path'])")"
        target_path="$(expand_home "$target_path")"

        if [[ -L "$target_path" ]]; then
            local dest
            dest="$(readlink "$target_path")"
            printf "  \033[32m[OK]\033[0m %s -> %s\n" "$target_path" "$dest"
        elif [[ -e "$target_path" ]]; then
            printf "  \033[33m[EXISTS]\033[0m %s (not a symlink)\n" "$target_path"
        else
            printf "  \033[31m[MISSING]\033[0m %s\n" "$target_path"
        fi
    done
}

# Usage
usage() {
    cat <<EOF
Usage: setup.sh <command>

Commands:
  install          Full setup: link AI agent configs
  link             Link AI agent configs only
  reset            Remove all symlinks (restore backups)
  status           Show current link status
  help             Show this help
EOF
}

case "${1:-help}" in
    install|link)  link_ai_agents ;;
    reset)         unlink_ai_agents ;;
    status)        show_status ;;
    help|--help|-h) usage ;;
    *) err "Unknown command: $1"; usage; exit 1 ;;
esac

info "Done"
