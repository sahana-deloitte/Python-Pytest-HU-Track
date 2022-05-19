lis=[[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]

for i in range(len(lis)):
    d={}
    for j in range(len(lis[i])):
        d[lis[i][j]]=d.get(lis[i][j],0)+1
    for item,val in d.items():
        if val>=2:
            print(item,'->',val)