'''
start 3:30
end 

10  : 2 3 4. 5 6. 7 8. 9. 10. -> 4
2   : 2 -> 1
<= 1:   -> 0
'''

'''
37
2 3 5 7

42
6

7
5 -> 
'''
def isprime_slow(number: int) -> bool:
    for smaller in range(2, number):
        if number % smaller == 0:
            return False
    else:
        return True

def isprime(number: int) -> bool:
    for smaller in range(2, 1 + int(number**.5)):
        if number % smaller == 0:
            return False
    else:
        return True

from typing import List
'''
100 -> 2, 3, 5, 7, 9.(dont consider)
'''
def isprimefast(number: int, primes: List[int]) -> bool:
    upper = 1 + int(number**.5) #i.e. < upper
    for smaller in primes:
        if smaller >= upper:
            break
        if number % smaller == 0:
            return False
    return True

'''
3 -> 2 yes. 
2 -> 1 ... yes
'''
def primecount_fast(number: int) -> int:
    if number < 2:
        return 0
    count = 1
    primes = [2]
    for smaller in range(3, number + 1):  #
        if smaller % 2 == 1 and isprimefast(smaller, primes):
            primes.append(smaller)
            count += 1
    return count

def primecount(number: int) -> int:
    if number < 2:
        return 0
    count = 1
    for smaller in range(3, number + 1):  #
        if smaller % 2 == 1 and isprime(smaller):
            count += 1
    return count
    
def primecount_slow(number: int) -> int:
    if number < 2:
        return 0
    count = 1
    for smaller in range(3, number + 1):  #
        # print(smaller)
        if smaller % 2 == 1 and isprime_slow(smaller):
            count += 1
    return count
    
for testnum in (-1, 1, 2, 3, 10, 1000):
    print(testnum, primecount(testnum), primecount_slow(testnum), primecount_fast(testnum))
#0 0 1 2 4