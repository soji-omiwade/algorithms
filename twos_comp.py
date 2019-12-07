"""
inspired by: https://stackoverflow.com/questions/39549971/bit-shifting-of-negative-integer
"""
def twos_comp(val: int, nbits: int):
    """compute the 2's complement of int value val"""
    if val < 0: 
        val += (1 << nbits)  #  0001 << 4 = 10000 = 16 = 2 ^ 4
    elif (val & (1 <<(nbits-1))) != 0:
        #if sign bit is set, then compute negative values
        val -= (1 << nbits)
    return val
    
def foo(a,b):
    print(f"{a:b} >> {b:b} = {a>>b:b} <-->"\
    +f" {twos_comp(a,8):b} >> {b:b} = {twos_comp(a>>b,8):b} ")
            
        
foo(-2,1)
foo(-3,1)
foo(-5,1)
foo(-7,1)   
        