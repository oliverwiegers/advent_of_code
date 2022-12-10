# --- Day 10: Cathode-Ray Day ---

## --- Part One ---

- Read lines
- Try to split lines in two to see if line is action or noop line
- If action increase cycle and if cycle is 20 or 20 + value divisible by 40
  calculate result
  - Do it tow times
- If noop only increase cycle
- Sum up result and print

## --- Part Two ---

- Read lines
- Try to split lines in two to see if line is action or noop line
- If action append register value to crt lis
  - Increase register by value afterwards
- If noop only append register value to crt
- After doing so for every line
  - Create lists with length of 40
  - For every item in there calculate absolute value
    - If <= 1 appned # to row
    - Otherwise append .
  - Print line and reset line for next row
