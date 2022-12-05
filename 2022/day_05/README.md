# --- Day 5: Supply Stacks ---

## --- Part One ---

### Get the stack arangement into a workable format

- Read file
- Split current stack / crate arangement from movement plan
- Create two dimensional array of stacks
- Rotate the array by 90 degrees to get every stack into a list to work with
- Remove lists that don't include a stack. Remove lists that include the borders
  from previous representation.
- Assign stack to dictionary with stack number as key
- Remove blank / empty crates
- Reverse the order so we can use .pop(0) to use the list as stack (Python has
  no native stack data structure)

### Use the movement plan to rearange the crates

- Read count of crates to move, source stack and target stack
- Move crates from source to target

## --- Part Two ---

### Get the stack arangement into a workable format

- Read file
- Split current stack / crate arangement from movement plan
- Create two dimensional array of stacks
- Rotate the array by 90 degrees to get every stack into a list to work with
- Remove lists that don't include a stack. Remove lists that include the borders
  from previous representation.
- Assign stack to dictionary with stack number as key
- Remove blank / empty crates
- Reverse the order so we can use .pop(0) to use the list as stack (Python has
  no native stack data structure)

### Use the movement plan to rearange the crates

- Read count of crates to move, source stack and target stack
- If a single crate is moved
  - Move crates from source to target
- If more than one crate is moved
  - Append crates to temp list and remove from source
  - Prepend target stack with temp stack
