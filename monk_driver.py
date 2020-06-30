
import monk 
def monkey_f(self): 
    a = b = 42
    print("monkey_f() is being called", a, b)
   
# replacing address of "func" with "monkey_f" 
obj = monk.A() 
# monk.A.func = monkey_f 
import types
obj.func = types.MethodType(monkey_f, obj)
  
# calling function "func" whose address got replaced 
# with function "monkey_f()" 
obj.func()
# obj.func() 