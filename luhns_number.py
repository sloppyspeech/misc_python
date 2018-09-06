import math
import functools as f
'''
take the number to be validated e.g. acc no                           23420894
double every alternate digit if more than 9 subtract 9 i.e.           26440798
add all the digits 2+6+4+2+0+7+9+8 = 40 
Multiply the sum by 9 :40*9 = 360 
tenths digit is the luhns number i.e. 0 in this case
'''
class LuhnsNumber(object):
    '''
        number passed to get_check_digit will generate and return check digit
        number passed to is_valid will check if the last digit of the number is valid 
          check digit based on Luhns Algoritm

    '''
    def __init__(self,p_inp):
        if type(p_inp) not in [int]:
            raise TypeError('Invalid Input,Input Should be Integers Only')
        else:
            self.p_inp=p_inp

    def get_check_digit(self):
        num=[ int(d) for d in str(self.p_inp)]
        even_digits=f.reduce(lambda x,y:x+y,num[::2])
        odd_digits=f.reduce(lambda x,y:x+y,[i+i if i+i <= 9 else i+i-9 for i in num[1::2]])
        return(((even_digits+odd_digits)*9)%10)

    def is_valid(self):
        check_digit=str(self.p_inp)[-1]
        self.p_inp=str(self.p_inp)[:len(str(self.p_inp))-1]
        if int(check_digit) == self.get_check_digit() :
            return True
        else:
            return False

    def __repr__(self):
        return "LuhnsNumber({0})".format(self.p_inp)

if __name__=='__main__':
    luhns_num=LuhnsNumber(53461861341123)
    print(luhns_num.get_check_digit())
    luhns_num=LuhnsNumber(534618613411238)
    print(luhns_num.is_valid())
    luhns_num=LuhnsNumber('Test')
