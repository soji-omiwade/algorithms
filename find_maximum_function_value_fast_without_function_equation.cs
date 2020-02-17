/**complexity
time:
**/
public static Tuple<double,int> binfind(a,p,r,bestnpv)
{
	if (p==r)
	{
		return (bestnpv,p);
	}
	
	q=(int)(p+r)/2;
	npvq = npv(q)
	if (npvq > bestnpv)
	{
		return binfind(a,q+1,r,npvq)
	}
	else
	{
		return binfind(a,p,q-1,bestnpv)
	}
}

/**
parent_npv is the best npv so far. otherwise we wouldn't be going to 
look for better
time: O(sigma i=1 up to lg(maximum) f(i)) where f is the time it takes
		to compute the i-th frac stage
space: O(1)
**/
public static Tuple<int,int> hopper(a, start, maximum, parent_npv)
{
	if (start>maximum)
	{
		return Tuple((int)start/2+1,maximum)
	}
	
	if (npv(start)<parent_npv)
	{
		return Tuple((int)start/2+1, start)
	}
	if (npv(start)>parent_npv)
	{
		return hopper(a,2*i,maximum,npv(start))
	}
}

start,end=hopper(a,1,60,bestnpv=0)
bestnpv, opt_frac = binfind(a,start,end,0)