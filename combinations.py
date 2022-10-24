T=["1","2","3","4","5","6"]
S = T.copy()


for k in range(0,2):
    temp = []
    for i in range(0, len(T)):
        for j in range(0,len(S)):
            temp.append(T[i] + " "+ S[j])
    S = temp
#print(S)
c= 0
for x in S:
    temp  = list(x.split())
    temp_list = list(map(int, temp))
    temp_sum = sum(temp_list)
    if temp_sum == 10:
        c+=1
        print(temp)
print(c)



