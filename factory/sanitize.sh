#!/bin/bash

# Loop through all files in the current directory
for file in *; do
  # Check if the filename contains at least one space
  if [[ "$file" == *" "* ]]; then
    echo "Removing: $file"
    rm -- "$file"
  fi
done

echo "Done."
