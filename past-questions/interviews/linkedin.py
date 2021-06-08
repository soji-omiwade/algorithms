"""
/**
 * Returns a^b, as the standard mathematical exponentiation function
 */
public double pow(double a, int b) {
    // implementation here
}
"""

#return a ^ b
"""
2,-3 -> 1/8

2, 8 -> 256

2*2 = 4 pow(2,2)
4*4 = 16 = 2^2*2^2 = pow(2,2) * pow(2,2) = pow(4,2)
16*(16)=256 = 4^2 * 4^2 = pow(2,2) * pow(2,2) * pow(2,2) * pow(2,2) = pow(16,2) = pow(8,2) * pow(2,2)


pow(16,2) -> 16*16

pow(16,7) -> 16*pow(16,3)*pow(16,3) -> 16*16*pow(16,2)*16*pow(16,2)
"""
def pow(a, b): 
    count=0
    ans = 1
    magb=abs(b)
    while count < magb: #O(b)
        ans = ans * a
        count += 1
    if b < 0: ans = 1/ans
    return ans

fp(2,4) = fp(2,2)*fp(2,2)

#2 * fp(2,3)
#2 * 2 * fp(2,2)
# fp(2,-3) = 1/fp(2,3)
# fp(a, -b) = 1/fp(a, b)
def fast_pow(a, b):
    if b < 0: 
        return 1/fast_pow(a, -b)
    if b == 0: 
        return 1
    if b == 1: 
        return a
    return (a if b%2==1 else 1) * fast_pow(a,b//2) * fast_pow(a,b//2) 



"""
/**
 * This is the interface that represents nested lists.
 * You should not implement it, or speculate about its implementation.
 */
public interface NestedInteger
{
    /** @return true if this NestedInteger holds a single integer, rather than a nested list */
    boolean isInteger();
 
    /** @return the single integer that this NestedInteger holds, if it holds a single integer
     * Return null if this NestedInteger holds a nested list */
    Integer getInteger();
 
    /** @return the nested list that this NestedInteger holds, if it holds a nested list
     * Return null if this NestedInteger holds a single integer */
    List<NestedInteger> getList();
}


/**
 * Given a nested list of integers, returns the sum of all integers in the list weighted by their depth
 * For example, given the list {{1,1},2,{1,1}} the function should return 10 (four 1's at depth 2, one 2 at depth 1)
 * Given the list {1,{4,{6}}} the function should return 27 (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3)
 */
public int depthSum (List<NestedInteger> input)
{
    //Implementation here
}

{1,{4,{6}}}
{1}

"""
summ = 0
def foo(NestedInteger, count=1):
    if isInteger(nestedIntList):
        return getInteger() * count
    return summ += foo(getList(NestedInteger), count+1)

def depthSum(nestedIntList):
    the_sum = 0
    for i in range(len(a)):
        the_sum += a[i] * d[i]
    return the_sum



