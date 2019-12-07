"""
inspired by: https://stackoverflow.com/questions/39549971/bit-shifting-of-negative-integer
"""
def twos_comp(val: int, nbits: int):
    """compute the 2's complement of int value val"""

    if val > (1 << (nbits-1)-1):
        val = 0
    return val
    
    if val < 0: 
        print(f"{val} is less than 0; ",end="")
        val += (1 << nbits)
        print(f"it becomes {val}")

        
    return val
    
def foo(a,b,c=8):
    print(f"{a:b} >> {b:b} = {a>>b:b} <-->"\
    +f" {twos_comp(a,c):b} >> {b:b} = {twos_comp(a>>b,c):b} ")
            
        
foo(-2,1)
foo(-3,1)
foo(-5,1)
foo(-7,1)   
        