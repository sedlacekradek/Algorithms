def solution(A):
    # initiate set of fib sequence
    fib_numbers = set()
    fib_numbers.add(1)

    # edge case if A empty
    if len(A) == 0:
        return 1

    # helper function to find all fib seq numbers <= len(A)
    def fib_seq(limit=len(A) + 1, n1=1, n2=1):
        n3 = n1 + n2
        if n3 <= limit:
            fib_numbers.add(n3)
            fib_seq(limit=limit, n1=n2, n2=n3)

    # edge case - if only 1 jump needed
    if (len(A)) in fib_numbers:
        return 1

    # run helper to generate the fub seq
    fib_seq()

    # search for the lowest number of jumps
    counter = 1
    # if a leaf exists (==1) and is reachable by one of our jumps
    # it will be added to possible_positions
    possible_positions = set([-1])
    while counter <= len(A):
        positions_after_jump = set()
        # try jump from all possible positions
        for pos in possible_positions:
            # try all lengths of jumps we have available
            for jump in fib_numbers:
                # if end reached
                if pos + jump == len(A):
                    return counter
                # if we landed on a leaf, update the possible position after jump
                if pos + jump < len(A) and A[pos + jump] == 1:
                    positions_after_jump.add(pos + jump)
        # replace the possible position we already iterated through with new possible positions after jump
        # this has to be done this way because we cannot update it while the loop is ongoing
        possible_positions = positions_after_jump
        # increase counter as we know that at least 1 more jump is needed
        counter += 1
    # if counter is higher than the highest possible number of leaves, we know there is no solution
    return -1

