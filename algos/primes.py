import argparse

def is_prime(inp=0):
    """[summary]
    
    Keyword Arguments:
        inp {int} -- [description] (default: {0})
    
    Returns:
        [type] -- [description]
    """

    if(inp==0 or inp==1 or inp==2 or inp==3 or inp==5 or inp==7 ):
        return True
    elif (inp%2==0 or inp%3==0 or inp%5==0 or inp%7==0):
        return False
    else:
        idx=5
        while (idx*idx < inp) :
            if (inp%idx == 0 ) or (inp %(idx+2)==0 ):
                return False
            idx=idx+6
        return True

def get_primes_by_sieve(input_num):
    """
    Return List of All primes by using sieve of eratosthenes
    
    Arguments:
        input_num {int} -- Number upto which the list of primes to be calculated
    
    Returns:
        [list of prime numbers] -- [list of all nums below the input value]
    """
    inp=[i for i in range(input_num)]
    inp.pop(0)
    inp.pop(0)
    inp1=inp[:]
    idx=0
    while idx < len(inp):
        try:
            divisor=inp[idx]
        except IndexError:
            print("Index Error **********")
            print("{0}".format(idx))
            print("{0} {1}".format(inp,len(inp)))
            exit(1)
        for i,v in enumerate(inp,divisor):
            if v%divisor==0 and v!=divisor:
                inp1.remove(v)
        idx=idx+1
        inp=inp1[:]
    return inp

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument(
<<<<<<< HEAD
        "-s", 
        "--isprime",
        dest="is_prime",
        type=int ,
        help="Check if the given number is prime or not")
=======
        "-s", "--isprime",dest="is_prime",type=int ,help="Check if the given number is prime or not")
>>>>>>> 3969137cf0a0b3d209de43af501f06ed7d0cbd40
    parser.add_argument(
        "-a",
        "--allprimes",
        dest="all_prime",
        type=int,
        help="Get all prime numbers below this input")
<<<<<<< HEAD
        
    args=parser.parse_args()

=======
    args=parser.parse_args()
>>>>>>> 3969137cf0a0b3d209de43af501f06ed7d0cbd40
    if args.is_prime:
        input_num=args.is_prime
        print("Is {0} Prime ? {1}".format(input_num,is_prime(input_num)))
    else:
        input_num=args.all_prime
        sieve = get_primes_by_sieve(input_num)
        print("List of Primes below than {0} => {1}".format(input_num,sieve))

    # print(get_primes_by_sieve.__doc__)
