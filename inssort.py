import random
import math
# inp_val=[18,1,5,2,7,4,3,13,65,23]
# inp_val=[5,4,3,1,12,17,11,13,8,6,7,9,10,1,1,1,1,1,1,1,1,1,2,76,24,-1,75,34,-4,0,9,86,67,54,32,10]
inp_val=[math.floor(random.random()*10000) for i in range(10000) ]
# print(inp_val)
for i in range(1,len(inp_val)):
    # print(f'i is {i}')
    j=i
    while(j>0):
        # print(f'j is {j}')
        # print(f'inp_val[j] inp_val[j-1] :{inp_val[j]} === {inp_val[j-1]}')
        if inp_val[j]<inp_val[j-1]:
            tmp=inp_val[j-1]
            inp_val[j-1]=inp_val[j]
            inp_val[j]=tmp
        j=j-1
print(inp_val)