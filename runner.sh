#!/bin/bash

TMP_DIR="tmp"

for file in "$TMP_DIR"/*.txt; do
  if [[ -f "$file" ]]; then
    base_name=$(basename "$file" .txt)
    csv_file="$TMP_DIR/$base_name.csv"
    python3 convert_txt_to_csv.py "$file" > "$csv_file"
    echo "Output from $file saved to $csv_file"
  fi
done
