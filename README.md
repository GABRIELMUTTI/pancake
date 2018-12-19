# pancake
A Python3 algorithm to solve the pancake problem in the least amount of flips.
This is purely for educational purposes.

# algorithm
A trivial algorithm would be to select the largest number, flipping the list at
its index, and then flipping again to put it at its correct spot. With this procedure,
we can sort a list with `2n` flips more or less.

A cleverer algorithm would be one that doesn't select the ideal number to order, but instead
only takes in consideration the number on the top of the "pancake pile" (the first number
on the list). With this method we can sort the numbers on top without making two flips. The
problem with this algorithm is that when sorting the top number, it can make flips that return
a number already sorted to the top of the list. This, of course, is bad because we then have to
sort the number again.
This is the current implemented algorithm.

The algorithm that I've thought, but have not yet implemented, is one that is similar to the
former but it sorts the top number in reverse order if the flip that sorts it in the correct
order fragments a set of numbers that are already ordered. From testing, this seems to be better
than the previous method. When I'll have the algorithm I'll implement it.

# files
## flipper.py
A program to manually flip lists.
### build list
Enter each number followed by a <RET> to build a list.
Press <RET> to finish building.

### select list
Enter a number to select the corresponding list.

### random list
Creates a random list with length `n`

### commands
* u: undo last flip.
* f: show number of flips.
* r: resets the list.

## pancake.py
The best algorithm I've managed to create (for now).
