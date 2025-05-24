def printTable(tableData):
    # Find the maximum width of each column
    colWidths = [max(len(item) for item in col) for col in tableData]

    # Transpose the data to print row-wise
    for row in zip(*tableData):
        formatted_row = "  ".join(item.rjust(colWidths[i]) for i, item in enumerate(row))
        print(formatted_row)

# Example data
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# Call the function
printTable(tableData)