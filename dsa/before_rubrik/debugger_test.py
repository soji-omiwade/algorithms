def caller():
    print("caller welcomes u")
    a = callee()
    
def callee():
    print("callee welcomes u")
    a = 42
    print(a)
    return a

breakpoint()
print(caller())
print("rice")