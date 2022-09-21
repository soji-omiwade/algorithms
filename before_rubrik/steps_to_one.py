#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minimumStepsToOne' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER num as parameter.
#


def minimumStepsToOne(num):
    # Write your code here
    def helper(num, count,minn,memo):
        if num in memo:
            return memo[num]
        if num == 1:
            if count < minn:
                minn = count
            memo[1]
            return minn
        
        if num % 3 == 0:
            minn=min(minn,helper(num//3, count+1,minn,memo))
        if num % 2 == 0:
            minn = min(minn,helper(num//2, count+1,minn,memo))
        minn = min(minn,helper(num-1, count + 1, minn,memo))

        return minn
    return helper(num,0,float("inf"))

if __name__ == '__main__':