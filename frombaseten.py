from typing import List
def frombase10(num: int, base: int) -> List[int]:
    res = []
    while num:
        res.append(num % base)
        num //= base
    return res[::-1]
num, base = 116, 5
print(frombase10(num, base)) # [4, 3, 1]