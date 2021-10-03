from typing import List
import sys

def basex_repr_num(num: int, base: int) -> List[int]:
    res = []
    while num:
        res.append(num % base)
        num //= base
    return res[::-1]
args = num, base = int(sys.argv[1]), int(sys.argv[2])
print(frombase10(*args)) # [4, 3, 1] if base five