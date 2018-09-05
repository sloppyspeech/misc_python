import math
import functools as f
'''
take the number to be validated e.g. acc no                           23420894
double every alternate digit if more than 9 subtract 9 i.e.           26420798
add all the digits 2+6+4+2+0+7+9+8 = 38 
Multiply the sum by 9 :38*9 = 342 
tenths digit is the luhns number i.e. 2 in this case
'''
def get_check_digit(p_inp):
    num=[ int(d) for d in str(p_inp)]
    even_digits=f.reduce(lambda x,y:x+y,num[::2])
    odd_digits=f.reduce(lambda x,y:x+y,[i+i if i+i <= 9 else i+i-9 for i in num[1::2]])
    return(((even_digits+odd_digits)*9)%10)

get_check_digit(455669592034729455)