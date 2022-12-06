# --- Day 6: Tuning Trouble ---

## --- Part One ---

- Read transmission line
- Filter out empty lines (only one will remain)
- Enumerate every char in line (string)
- Append every char to marker list if it is not already in it
  - If char is in marker already delete items of marker until first occurence of
    char and append char
- If marker length is equals to 4 return index of current char

## --- Part Two ---

- Use function from part one and execute two times
  - First search for marker
  - Second search for message
- Return marker index + message index
