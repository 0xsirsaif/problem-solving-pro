"""
In the Towers of Hanoi puzzle, we are given a platform with three pegs, a, b, and c, sticking out of it.
On peg a is a stack of n disks, each larger than the next, so that the smallest is on the top and the largest is on the bottom.

The puzzle is to move all the disks from peg a to peg c, moving one disk
at a time, so that we never place a larger disk on top of a smaller one.

See Figure 4.15 for an example of the case n = 4. Describe a recursive
algorithm for solving the Towers of Hanoi puzzle for arbitrary n.

Hint:
    Consider first the sub-problem of moving all but the n th disk from peg a to
    another peg using the third as “temporary storage.”

review and notes:
    algorithm:
        1 - move all upper disks (n-1 disks) from the src to the temp
        2 - move the nth disk to the des
        3 - move all upper disks from the temp to the src
    - step 3 is the same as step 1, but different arrangements of the poles.
    - (n = 0) indicates that there is no disks up me -> so I will move
    TODO: Still :"( !
"""


def tower_of_hanoi(src, des, temp, n):
    print(">>", "move", n, "from", src, "to", des, "with", temp)
    if n <= 0:
        return
    tower_of_hanoi(src, temp, des, n - 1)
    print(f"move {n} from {src} to {des}")
    tower_of_hanoi(temp, des, src, n - 1)


print(tower_of_hanoi('a', 'c', 'b', 3))
