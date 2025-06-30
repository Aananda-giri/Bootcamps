#!/bin/bash

cd /home/anon-labs/Documents/projects/creator-script/mcp-project/

# Run all *_server.py files in servers folder
for f in servers/*_server.py; do
    uv run "$f" &
done

# Run the client
# Open a terminal window for the client so user can give input
gnome-terminal -- bash -c "uv run client.py; exec bash"

