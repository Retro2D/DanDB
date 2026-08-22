import json

#These are most of the basic functions inside of the DanDB module.  :)

def about():
    return("Welcome to DanDB! \nThis project was made for the Stardance hackathon, but I plan on using it for \ngeneral purpose.  \nThis project is open-source, and readability friendly.  \nFeel free to use for your own hacks! :D")

### Statistic functions ###

def mean(array):
    return sum(array)/len(array)

def median(array):
    array.sort() #Sort our data, pretty self-explanatory.
    if len(array)%2 == 0: #Checks if value is even
        return mean([array[len(array)//2], array[len(array)//2-1]]) #Returns mean of middle, middle+1 values since there is no one middle value.
    
    elif len(array)%2 == 1: #Checks if value is odd
        return array[(len(array)-1)//2] #Returns the middle value. Pretty simple to understand.

def mse(act, pred):
    #Error handling
    if len(act)-len(pred) != 0:
        raise ValueError("Actual and predicted values must be the same in length.")
    
    #Actual function itself
    squared_dif = []

    for i, (a, p) in enumerate(zip(act, pred)):
        squared_dif.append((a-p)**2) #Get difference squared for actual and predicted.

    return mean(squared_dif) #Now we get the mean, which should be the output of the function.

def matrix_combine(*lists):
    init_lists = [lst for lst in lists if lst]

    if not init_lists:
        return("Warning: matrix_combine function must have at least one argument")

    return list(zip(init_lists))

### Database functions ###

#Init database datatypes

class Table:

    #Rate limiting

    max_rows = 100000
    max_data = 100000000
    max_string = 1000

    #Bundling function
    def bundle_data_row(self, row, data):
        output = []
        chunk = []

        for i in range(len(row)):
            chunk = [i]
            chunk.append(row[i])

            for x in range(len(data)//len(row)):
                chunk.append(data[x])

            output.append(chunk)

        return(output)
    
    def __init__(self, name: str, columns: int, rows=1, data=None, xcolumn_names=None, ycolumn_names=None):
        if data == None:
            data = []

        if xcolumn_names == None:
            xcolumn_names ='Unspecified'

        if ycolumn_names == None:
            ycolumn_names = 'Unspecified'

        #Initialize params
        self.name = name
        self.columns = columns
        self.rows = rows
        self.dimensions = 3
        self.data = data

        #Error handling for wrong datatype
        def column_check(self, column_val: int):
            if not isinstance(column_val, int):
                raise ValueError("Column datatype must be of int")

        def dimen_check(self, dimen_val: int):
            if not isinstance(dimen_val, int):
                raise ValueError("Dimension datatype must be of int")


        #Error handling for maximum thershold
        def threshold_check(self, columns, rows):
            if columns * rows > self.max_data:
                raise ValueError("Total data value exceeds maximum threshold")
            
        column_check(self, columns)

        tableinit = []
        xcolumns_init = []
        ycolumns_init = []
        mydata = []
        tableinit.append(name)
        fulldatasize = columns * rows

        #Append data to table
        if len(data) == 0 or isinstance(data, str):
            if isinstance(data, str):
                print("Warning: Inputting string values as data will not do anything, and instead call the default values of 0.  If you want this, using [] as the input is \nthe best practice.")

            for i in range(fulldatasize):
                mydata.append(0)

        elif fulldatasize != len(data) and isinstance(data, str) != True:
            mydata = data
            fixeddatasize = fulldatasize - len(data)

            for i in range(fixeddatasize):
                mydata.append(0)

        else:
            mydata = data

        self.data = mydata

        for i in range(columns):
            if isinstance(xcolumn_names, str):
                xcolumns_init.append(xcolumn_names)

            else:
                if len(xcolumn_names) == 1:
                     xcolumns_init.append(xcolumn_names[0])

                else:
                    if i+1 <= len(xcolumn_names):
                        xcolumns_init.append(xcolumn_names[i])

                    else:
                        xcolumns_init.append("Unspecified")

        self.columns = xcolumns_init

        for i in range(rows):
            if len(ycolumn_names) == 1:
                 ycolumns_init.append(ycolumn_names[0])

            else:
                if isinstance(ycolumn_names, str):
                    ycolumns_init.append(ycolumn_names)

                else:
                    if i+1 <= len(ycolumn_names):
                        ycolumns_init.append(ycolumn_names[i])

                    else:
                        ycolumns_init.append("Unspecified")

        self.ycolumns = ycolumns_init

        bundledrows = self.bundle_data_row(self.ycolumns, mydata)

        tableinit = matrix_combine(bundledrows, xcolumns_init)
        self.table = [name, tableinit]

    #Methods

    def addrow(self, rows, row_name="undefined", content=None):
        if content == None:
            content = []

        if rows <= 0:
            raise ValueError("Row value must be at least one.")

        if rows+len(self.ycolumns) > self.max_rows:
            raise ValueError("Total row value exceeds maximum threshold")
        
        for i in range(rows):
            self.ycolumns.append(row_name)
            for x in range(len(self.columns)):   
                if i+1 <= len(content):
                    self.data.append(content[i])
                else:
                    self.data.append(0)

        bundledrows = self.bundle_data_row(self.ycolumns, self.data)

        print(bundledrows)

        tableinit = matrix_combine(bundledrows, self.columns)
        self.table = [self.name, tableinit]
        
        return self
    
    def changetitle(self, newtitle):
        self.table[0] = newtitle

    def destroy(self):        
        self.table[0] = "Unnamed"
        self.name = "Unnamed"
        for i in range(len(self.data)):
            self.data[i] = 0

        for i in range(len(self.ycolumns)):
            self.ycolumns[i] = "Unnamed"
            
        for i in range(len(self.columns)):
            self.columns[i] = "Unnamed"

        bundledrows = self.bundle_data_row(self.ycolumns, self.data)

        tableinit = matrix_combine(bundledrows, self.columns)
        self.table = [self.name, tableinit]

    def replace(self, lines, new_val):
        if isinstance(lines, int):
            self.data[lines] = new_val

        elif isinstance(lines, list):
            for i, x in enumerate(lines):
                if isinstance(new_val, str):
                    self.data[x] = new_val
                elif isinstance(new_val, list):
                    self.data[x] = new_val[i]

        else:
            raise ValueError("lines param must be either int or list datatype")
    
        return self

    #length organization methods

    @staticmethod
    def get_longest_item(inputlist):
        if isinstance(inputlist, list):
            longestitem = inputlist[0]
            for i in inputlist:
                if len(str(i)) > len(longestitem):
                    longestitem = str(i)
            return(longestitem)
        
        else:
            raise ValueError("Input type must be list!")
        
    @staticmethod
    def get_shortest_item(inputlist):
        if isinstance(inputlist, list):
            longestitem = inputlist[0]
            for i in inputlist:
                if len(i) < len(longestitem):
                    longestitem = i
            return(longestitem)
        
        else:
            raise ValueError("Input type must be list!")
        
    def getlongestrow(self):
        return(self.get_longest_item(self.ycolumns))
    
    def getlongestcolumn(self):
        return(self.get_longest_item(self.columns))

    #padding methods

    @staticmethod
    def getrowpadding(currentrow, toprow):
        return (f"{' ' * (toprow - len(str(currentrow)))}{currentrow}|")

    def getjson(self):
        return(json.dumps(self.table, separators=(',', ':')))

    def getformattedjson(self):
        return(json.dumps(self.table, indent=2))

    #File saving
    def writejson(self, filename):
        with open(filename, "w") as f:
            f.write(json.dumps(self.table, indent=2))
                    


#Now, here are the functions :)

def create_table(name, rows, columns=1, data=None, column_names="Unspecified", row_names="Unspecified"):
    if data == None:
        data = []

    new_table = Table(name, rows, columns, data, column_names, row_names)
    return new_table

def table_addxy(table, y_rep):
    pass

def return_raw(table_name):
    return table_name.table

def pretty_print(table_name):
    printinit = [] #This list defines our content, since we cannot return mroe than once.
    toprowinit = []
    longestrow = len(table_name.getlongestrow())
    toppadding = ""
    for i in range(round((longestrow-len(table_name.table[0]))/2)):
        toppadding = toppadding+"="
    
    for i in range((round(sum(map(len, table_name.columns))/2))):
        toppadding = toppadding+"="
    
    for i in range(len(table_name.columns)):
        toppadding = toppadding+"="
    
    printinit.append(f"{toppadding}{table_name.table[0]}{toppadding}")
    spacing = ""

    for i in range(longestrow):
        spacing = spacing+" "
    toprowinit.append(f"{spacing}| ")

    for i in table_name.columns:
        toprowinit.append(f"{i}| ")

    toprowinitcontent = "".join(toprowinit)
    printinit.append(toprowinitcontent)

    for i, item1 in enumerate(table_name.ycolumns): #For every item in table
        columninit = (f"{' ' * (longestrow - len(str(item1)))}{item1}|")

        for x, item2 in enumerate(table_name.columns): #For for every column in table
            dataindex = table_name.data[i * len(table_name.columns) + x] #Gets the current item by getting the current row (represented by i), multiplying it by the amount of columns to find where the row is on the list, and then adds x (the column pointer) to find which column it is located at.  This results in the exact location of the data.
            xindex = table_name.columns[i%len(table_name.columns)]

            #Length conditions

            if i-1 <=len(table_name.data): 
                if len(str(dataindex)) == len(xindex)+1:
                    columninit = columninit + (f"{dataindex}|") #Explain this later

                elif len(str(dataindex)) < len(xindex)+1:
                    columninit = columninit + (f"{dataindex}{' '* ((len(xindex)+1) - len(str(dataindex)))}|") #Explain this later

                else:
                    cleaneddata = ""
                    for y in range((len(xindex))+1):
                        cleaneddata += str(str(dataindex)[y])

                    columninit = columninit + (f"{(cleaneddata)}|") #Explain this later
                    
        printinit.append(columninit)

    print(*printinit, sep="\n", end="") #This is our pretty print!
