inp_val=[5,4,3,1,12,17,11,13,8,6,7,9,10,1,1,1,1,1,1,1,1,1,2,76,24,-1,75,34,-4,0,9,86,67,54,32,10]
# inp_val=[18,1,5,2,7,4,3]
run=True
while (run==True):
    run=False
    for i in range(1,len(inp_val)):
        # print("------")
        # print(inp_val)
        # print(i)
        # if i>0:
            # print(i-1)
            # print(inp_val[i-1])
            # print("===")
            # print(inp_val[i],inp_val[i-1])
        if inp_val[i]<inp_val[i-1]:
            run=True
            tmp=inp_val[i-1]
            inp_val[i-1]=inp_val[i]
            inp_val[i]=tmp
print(inp_val)