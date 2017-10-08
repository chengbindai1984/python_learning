

rowData = [['apple', 'organge111','cherries','banana'], [
    'alice', 'bob', 'Carol3333', 'David'], ['dog', 'cats888', 'moose', 'goose']]

#colWidths = [0] * len(tableData)

# for x in range(len(tableData)):
#print (x)
#    for y in range(len(tableData[x])):
#        if len(tableData[x][y])>len(tableData[x][y-1]):
#            colWidths[x]=len(tableData[x][y])
#        else:
#            colWidths[x]=len(tableData[x][0])
#print (colWidths)


def printTable(tableData):
    colWidths = [0] * len(tableData)
    print (colWidths)
    for x in range(len(tableData)):
        for y in range(len(tableData[x])):
            if len(tableData[x][y]) > len(tableData[x][y - 1]):
                colWidths[x] = len(tableData[x][y])
                print (colWidths[x])
            else:
                colWidths[x] = len(tableData[x][y-1])
                print (colWidths[x])
            #print (tableData[0][y].rjust(colWidths[0], '-'))
printTable(rowData)
