import math
import functools as f
'''
take the number to be validated e.g. acc no                           23420894
double every alternate digit if more than 9 subtract 9 i.e.           26440798
add all the digits 2+6+4+2+0+7+9+8 = 40 
Multiply the sum by 9 :40*9 = 360 
tenths digit is the luhns number i.e. 0 in this case
'''
def get_check_digit(p_inp):
    num=[ int(d) for d in str(p_inp)]
    even_digits=f.reduce(lambda x,y:x+y,num[::2])
    odd_digits=f.reduce(lambda x,y:x+y,[i+i if i+i <= 9 else i+i-9 for i in num[1::2]])
    return(((even_digits+odd_digits)*9)%10)

print(get_check_digit(23420894))