import MapReduce
import sys

"""
Multiply two matrix
in using the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: matrix id
    # value: matrix[i,j] value
    key = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    # If it's the matrix a
    if key == "a":
        mr.emit_intermediate((i,0), record)
        mr.emit_intermediate((i,1), record)
        mr.emit_intermediate((i,2), record)
        mr.emit_intermediate((i,3), record)
        mr.emit_intermediate((i,4), record)
    else:
        mr.emit_intermediate((0,j), record)
        mr.emit_intermediate((1,j), record)
        mr.emit_intermediate((2,j), record)
        mr.emit_intermediate((3,j), record)
        mr.emit_intermediate((4,j), record)

def reducer(key, list_of_values):
    # key: (i,j)
    # value: list of A[i,k], B[k,j]
    multiply_value = 0
    for vA in list_of_values:
        matrixA = vA[0]
        jA = vA[2]
        valueA = vA[3]
        if matrixA == "a":
            for vB in list_of_values:
                matrixB = vB[0]
                jB = vB[1]
                valueB = vB[3]
                if matrixB == "b" and jB == jA:
                    multiply_value += valueA * valueB
    mr.emit((list(key) + [multiply_value]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
