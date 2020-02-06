def list_sum(a, depth=0):
    if type(a) is int:
        return a*depth

    res=0
    for x in a:
        res += list_sum(x,depth+1)
    return res
    
if __name__ == "__main__":
    assert list_sum([[1,1],2,[1,1]]) == 10
    assert list_sum([1,[4,[6]]]) == 27