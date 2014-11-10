import MapReduce
import sys

"""
Asymmetric friendships
in using the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: one friend
    key = record[0]
    value = record[1]
    mr.emit_intermediate((key,value), 1)
    mr.emit_intermediate((value,key), 1)

def reducer(key, list_of_values):
    # key: (person,friend)
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
        total += 1
    if total == 1:
        mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
