from __future__ import print_function
rowData = [['apple', 'organge111','cherries','banana'], [
    'alice', 'bob', 'Carol3333', 'David'], ['dog', 'cats888', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    for raw in range(len(tableData)):
        compare_list=[]
        for col in tableData[raw]: 
            compare_list.append(len(col))
        colWidths[raw]=max(compare_list)
    
    # for raw in range(len(tableData)):
    for col in range(len(tableData[0])):
        for raw in range(len(tableData)):
            print (tableData[raw][col].rjust(colWidths[raw], ' '), end='  ')
        print ('\n')
    
printTable(rowData)
