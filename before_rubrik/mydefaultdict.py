class mydd(dict):
    def __init__(self, func):
        self.func = func
        super().__init__()
        
    def __getitem__(self, key):
        if key not in self:#  
            self[key] = self.func()
        return super().__getitem__(key)
    
dd = mydd(int)
print(dd[20]) # 0
dd[25] = 42 #test normal dict features
print(dd) # {20:0, 25:42}

dd = mydd(lambda: "hello")
print(dd[20])
dd[25] = 42 #test normal dict features
print(dd) # {20:"hello", 25:42}
