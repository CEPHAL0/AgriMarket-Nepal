#!/bin/bash

# Remove all __pycache__ folders
find . -type d -name "__pycache__" -exec rm -rf {} +
