try:
    callfirst()
except NameError:
    print("all objects must be declared b4 they are used!")
else:
    raise Exception("a name error shoulda been thrown!")
    
def callfirst():
    print("hello")