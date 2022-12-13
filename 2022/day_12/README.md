# --- Day 12: Hill Climbing Algorithm ---

## --- Part One ---

- Read lines as bytes so characters are translated to bytes
- Find start and end in matrix
- Execute Breath First Search on Grid
  - Find all neighboring cells that fit the requirements elvevation +-1 to the
    ccurrent cell.

## --- Part Two ---

- Read lines as bytes so characters are translated to bytes
- Find all lowest cells and execute code from first puzzle on all of them
  - Find start and end in matrix
  - Execute Breath First Search on Grid
    - Find all neighboring cells that fit the requirements elvevation +-1 to the
      ccurrent cell.
  - Return lowest step number
