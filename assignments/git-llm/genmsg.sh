#!/bin/sh

$(git diff) | uv run llm -t git_commit_message
