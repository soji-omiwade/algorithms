/**complexity
time:
**/
public static Tuple<double,int> binfind(a,p,r,max_func_val)
{
	if (p==r)
	{
		return (max_func_val,p);
	}
	
	q=(int)(p+r)/2;
	if (func(q) > max_func_val)
	{
		return binfind(a,q+1,r,func(q))
	}
	return binfind(a,p,q-1,max_func_val)
}

/**
parent_func_value is the best func so far. otherwise we wouldn't be going to 
look for better
time: O(sigma i=1 up to lg(maximum) f(i)) where f is the time it takes
		to compute the i-th frac stage
space: O(1)
**/
public static Tuple<int,int> hopper(start, maximum, parent_func_value)
{
	if (start>=maximum)
	{
		//like the if below, start/2+1 would be wrong because
		//we don't yet know that it is not better than the maximum
		return Tuple((int)start/2,maximum)
	}
	
	if (func(start)<=parent_func_value)
	{
		//start/2+1 would be wrong since start/2 could be the optimal!
		//Similarly, maximum=start is wrong because we know for a fact
		//that start cannot be the optimal (it
		//func(start/2))
		return Tuple((int)start/2, start-1)  
	}
	
	return hopper(2*start,maximum,func(start))
}

start,end=hopper(a,1,60,max_func_val=0)
max_func_val, opt_frac = binfind(a,start,end,0)