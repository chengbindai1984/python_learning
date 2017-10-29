
rowData = [['apple', 'organge111','cherries','banana'], [
    'alice', 'bob', 'Carol3333', 'David'], ['dog', 'cats888', 'moose', 'goose']]

def printTable(tableData):
    # 取出打印每列的最大字符串宽度
    colWidths = [0] * len(tableData)
    for raw in range(len(tableData)):
        compare_list=[]
        for col in tableData[raw]: 
            compare_list.append(len(col))
        colWidths[raw]=max(compare_list)
    
    # 逐行按照列次序打印
    for col in range(len(tableData[0])):
        for raw in range(len(tableData)):
            print (tableData[raw][col].rjust(colWidths[raw], ' '), end='  ')
        print ('\n')
    
printTable(rowData)
