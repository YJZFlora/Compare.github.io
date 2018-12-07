from enum import Enum

# defines three constants, each of which represents an operation via which a string might be transformed into another
class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())

def distances(a, b):
    """Calculate edit distance from a to b"""

    # TODO  takes two strings as arguments,  a and b. Return (via a matrix of costs) the edit distance between one and the other.
    r, c = len(a) + 1, len(b) + 1

    cost = 0
    operation = Operation.DELETED

    costs = [[cost for x in range(c)] for y in range(r)]

    for j in range(c):
        costs[0][j] = j

    for i in range(r):
        costs[i][0] = i

    for i in range(r):
        for j in range(c):
            if i != 0 and j != 0:
                if b[j - 1] == a[i - 1]:
                    costs[i][j] = min(costs[i - 1][j] + 1, costs[i][j - 1] + 1, costs[i - 1][j - 1])
                else:
                    costs[i][j] = min(costs[i - 1][j] + 1, costs[i][j - 1] + 1, costs[i - 1][j - 1] + 1)

    operations = [[operation for x in range(c)] for y in range(r)]

    for j in range(c):
        operations[0][j] = Operation.INSERTED

    for i in range(r):
        operations[i][0] = Operation.DELETED

    for i in range(r):
        for j in range(c):
            if i != 0 and j != 0:
                if costs[i][j] == costs[i - 1][j] + 1:
                    operations[i][j] = Operation.DELETED
                elif costs[i][j] == costs[i][j - 1] + 1:
                    operations[i][j] = Operation.INSERTED
                else:
                    operations[i][j] = Operation.SUBSTITUTED

    matrix = [[(cost,operation) for x in range(c)] for y in range(r)]

    for i in range(r):
        for j in range(c):
            matrix[i][j] = (costs[i][j], operations[i][j])

    matrix[0][0] = (0, None)

    return matrix
