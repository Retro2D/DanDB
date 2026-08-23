# A basic demo for DanDB, showing how a table is sucessfully made.

import DanDB

table = DanDB.create_table("test", 5, 3, [], "column", "row") # Creating a basic table with unspecified data, column and row names of "column" and "row" respectively.

table.addrow(3, "other row") # Add three other rows with the names "other row"
table.replace([1, 3, 5], ['new value', 'newer value', 'newest value']) # Replaces data at list index 1, 3, and five with "ndw value", "newer value", and "newest value" respectively.  (please note that indexes are added by one as per Python's default indexing guidelines.  For example, first item in table is at index zero).

DanDB.pretty_print(table) # Pretty print our table.  Pretty straightforward.

table.writejson("example.json") # Writes json of table to example.json file