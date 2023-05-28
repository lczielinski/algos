def helper(A, B, i, j):
    if i > j:
        return A[-1]
    k = (i + j) // 2

    if A[k] >= B[k]:
        return helper(A, B, k + 1, j)
    elif A[k] < B[k]:
        if k == 0 or A[k - 1] >= B[k - 1]:
            return A[k]
        else:
            return helper(A, B, i, k - 1)


def find_the_extra(A, B):
    assert len(A) == len(B) + 1
    return helper(A, B, 0, len(B) - 1)


assert find_the_extra([1, 2, 3], [1, 2]) == 3
assert find_the_extra([1, 2, 3], [1, 3]) == 2
assert find_the_extra([1, 2, 3], [2, 3]) == 1
assert find_the_extra([1, 2, 4, 5], [1, 2, 3]) in [4, 5]
assert find_the_extra([1, 2, 4, 5], [2, 3, 4]) in [1, 5]
assert find_the_extra([1, 2, 4, 5], [3, 4, 5]) in [1, 2]
assert find_the_extra([1, 6, 10], [4, 7]) in [1, 6, 10]
assert find_the_extra([2, 5, 9], [5, 10]) in [2, 9]
assert find_the_extra([1, 2, 5, 7, 10, 11], [0, 1, 6, 7, 10]) in [2, 5, 11]
assert find_the_extra([15, 18, 19, 20, 21], [15, 17, 18, 21]) in [19, 20]
