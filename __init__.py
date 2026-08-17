"""
    DanDB
    An open-source statistics module created by Daniel Long.

    Run DanDB.about() for more info.

    v0.0.1
"""

__version__ = "0.0.1"

import DanDB

exampledata = []

for i in range(16):
    exampledata.append(i+1)

mytable = DanDB.create_table("Example", 4, 4, exampledata)
DanDB.pretty_print(mytable)

mytable.writejson("example.json")