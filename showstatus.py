#!/usr/bin/env python3

import os

"""
This is a very simple script which concatenates the contents of
all files in the ~/.local/status directory, and prints it to stdout.
Various programs on the machine can dump a brief status to a file in
this directory, and this program will use this program to concatenate
them, for displaying in the tmux status line.
"""

status_dir="/home/enfors/.local/status"
statuses = []

files = [f for f in os.listdir(status_dir)
         if os.path.isfile(os.path.join(status_dir, f))]

for status_file in files:
    with open(os.path.join(status_dir, status_file), "r") as f:
        statuses.append(f.readline().strip())

if len(statuses) == 0:
    raise SystemExit

print(" | ".join(statuses))
