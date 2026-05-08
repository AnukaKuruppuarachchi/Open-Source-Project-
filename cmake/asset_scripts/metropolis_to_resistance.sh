#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/replace_color.sh"
replace_color $1 "#2a2336" "#451700" "#591fa8" "#df4a00" "#310e66" "#5d1319" "#3d107b" "#92000c" "#211b3b" "#7d2a00" "#29224a" "#8a2e00" "#302a58" "#aa3900" "#310e5b" "#df7126"
