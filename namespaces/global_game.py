def foo():
    global spam
    spam = 42
foo()
print(spam)

class A:
    def __init__(self):
        self.a = spam

print(A().a)
print(A.spam)