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
def isprime(number: int) -> bool:
    for smaller in range(2, 1 + int(number**2)):
        if number % smaller == 0:
            return False
    else:
        return True

'''
3 -> 2 yes. 
2 -> 1 ... yes
'''
def primecount(number: int) -> int:
    if number < 2:
        return 0
    count = 1
    for smaller in range(3, number + 1):  #
        if smaller % 2 == 1 and isprime(smaller):
            count += 1
    return count
    
for testnum in (-1, 1, 2, 3, 10):
    print(primecount(testnum))
#0 0 1 2 4