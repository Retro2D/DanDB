# DanDB
DanDB is a multi-purpose module built for statistics, analyitics, and some other uses (such as a limited selection of machine learning functions).  

Current release is 0.0.1.  It can:
-Create and manipulate some basic two-dimensional graphs
-Print out spreadsheets of those graphs
-Provide an amount of essential formulas for graphing, data science, and machine learning (currently W.I.P with ML formulas)

**IMPORTANT NOTICE:** This project is currently in pre-alpha.  It currently isn't meant for any serious work; it is mostly a fun side project I am building.

# Guide
Guide to using the module's functions.  Importing the module is what you do for any other module: `import DanDB`.  That's it.

## Creating a table:

To create a basic chart, use the `create_table()` function.   The `create_table()` function has all the essential parameters for creating a basic table.  It requires `name` and `rows` parameters to function; their usage is self explanatory.  

The `name` parameter simply refers to the name you want to give the chart in both JSON and pretty print form, while the `rows` parameter refers to the amount of rows you want to give your chart.  

Likewise, the `columns` parameter refers to the amount of columns you want to give your chart, though it isn't necessary (defaulted to one if not specified).  The `data` parameter can either be a list or string, though only a list will have effect (any string will be IGNORED).   As the name suggests, the `data` parameter will include the data visualized on your chart.  If not inputted, it defaults to 0 for each column and row on your list.  It also should be noted that the length of your list should reflect the size of the table (rows * columns).  If it is less, default values of 0 will be added, and larger values will result in crashes.

The `xcolumn_names` and `ycolumn_names` parameters refer to the names of your columns (xcolumn) and rows (ycolumn).  The default value for these parameters is "Unspecified".  You can either input a list or string for each of them, though inputting a string will cause every row/column of your table to have that exact name.   Lists are expected to be the exact length of either your columns or rows; wrong values can lead to unexpected behavior.  

## Modifying a table:
Tables have multiple methods and functions you can use to modify them.  Here is a list of them:

### methods:

 1. `table.addrow(rows, row_name, content)` Adds a row (or multiple rows) to your table.  `rows` parameter specifies how many rows you want to add, while `row_name` parameter specifies what the names for the rows should be.  The value given to this parameter will be used for each row added to the table through this function.  `content` is used to specify the data given to the row.  Unlike other methods/functions, `content` must strictly be a list for it to function.
 2. `table.changetitle(newtitle)` Pretty straightforward.  You can change the visual title for your table using this function.  The `newtitle` parameter specifies what your new title should be called.  It must be a string.
 3. `table.destroy()` Destroys your entire table, and replaces it with a dummy table.  Pretty straightforward; no parameters.

## Functions

 1. `DanDB.table_replace(table_name, lines, newval)` Replaces values at `lines` list/int with data from `newval` list.  `lines` can be an int, though it will only replace data from one line.

# Outro
This README is a work in progress, and doesn't cover half of the things in this module.  I would advise you to look into the `DanDB.py` file for more info on the functions and attributes of this module. 

Good luck!  -Dan.

