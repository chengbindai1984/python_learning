

rowData = [['apple', 'organge111','cherries','banana'], [
    'alice', 'bob', 'Carol3333', 'David'], ['dog', 'cats888', 'moose', 'goose']]


for x in range(len(rowData)):
    compare_list=[]
    for y in rowData[x]: 
        compare_list.append(len(y))
    print (compare_list)
    print (max(compare_list))
    