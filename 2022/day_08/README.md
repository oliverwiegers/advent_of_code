# --- Day 8: Treetop Tree House ---

## --- Part One ---

- Read all lines
- Turn lines into list and append these to other list to get 2D array / grid
- Add all outer trees to result. 2x length left to right + 2x length top to
  bottom - 4. Minus 4 because the lenght overlaps at the corners.
- In iteration ignore outer trees because they are all visible and already added
  to the result.
- Check for every tree if is the highest in list slice left, slice right.
- Create tmp list for all trees in top to bottom at same posistion and check if
  tree is the highest in slice top, slice down.
- Dont forget to break the loop so trees are not counted twice if they are
  visible for example from left and the top.

## --- Part Two ---
