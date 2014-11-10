import MapReduce
import sys

"""
Using map-reduce to simulate the join function in SQL
We use the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id
    # value: order or line_item
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: order_id
    # value: list of orders or line_items
    order = None
    # find the order in the list
    for v in list_of_values:
        if v[0] == "order":
            order = v
            break
    # Make join operator
    if order is not None:
        for v in list_of_values:
            if v[0] != "order":
                mr.emit(order + v)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
