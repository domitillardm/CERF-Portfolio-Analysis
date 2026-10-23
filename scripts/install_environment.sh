#!/usr/bin/env bash
set -euo pipefail
cd /workspace/CERF-Portfolio-Analysis
# Work in the existing repository; never use /workspace/cerf-project.
# The environment snapshot must contain the reviewed repository setup files.
test -f AGENTS.md
test -f .gitignore
python3 scripts/setup_project.py
python3 scripts/test_environment.py
