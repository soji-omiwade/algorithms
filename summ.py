import unittest


class mytest(unittest.TestCase):
    def test(self):
        a = [1,2,3,4,5]
        self.assertEqual(foo(a,7), (2,3))
    def test2(self):
        b= [9, 1, 5, 4]
        self.assertEqual(foo(b,3), (0,0))
    def test3(self):
        b= [9, 1, 5, 4]
        self.assertEqual(foo(b,10), (0,1))
    def test4(self):
        b= [9, 1, 5, 25, 4]
        self.assertEqual(foo(b,25), (3,3))
    
def foo(arr: list, target: int) -> tuple:
    n=len(arr)
    i=j=0
    im,jm=0,n
    
    while i < n:
        summ=sum(arr[k] for k in range(i,j+1))
        if summ >= target:
            if j-i < jm-im:
                im,jm=i,j
                print(f"found: {(im,jm)}")
            i+=1
        else: 
            if j < n-1:
                j+=1
            else: 
                i+=1
    print("done")
    return im,jm

unittest.main()