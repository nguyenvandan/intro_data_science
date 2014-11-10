import MapReduce
import sys

"""
Unique strims
in using the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence id
    # value: nucleotides
    key = record[0]
    value = record[1]
    mr.emit_intermediate(1, value[:-10])

def reducer(key, list_of_values):
    # key: 1
    # value: list of nucleotides
    set_of_nucleotides = set(list_of_values)
    for v in set_of_nucleotides:
        mr.emit(v)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
