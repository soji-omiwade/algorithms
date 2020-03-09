def organize_photos(S):
    """process: 
	- add another column to remember current order. 
	- now sort by time
	- maintain a dict  to act as a counter: foo[Warsaw] += 1. and change the name there and then.
	- now resort by the original order [no need]
	- go through again. and depending on maxdigits[city], do a zero fill for those cities needing zeros accordingly
    """
    aux=[]
    for item in S.split("\n"):
        name,city,date=item.split(",")
        nname,ext=name.split(".")
        aux.append([nname,ext,city,date])
    auxp=sorted(aux,key=lambda x:x[3])

    from collections import defaultdict
    d=defaultdict(int)
    for item in auxp:
        d[item[2]]+=1
        item[0]=str(d[item[2]])

    res=[]
    for nname,ext,city,date in aux:
        res.append(city+nname.zfill(len(str(d[city])))+"."+ext+"\n")
    return "".join(res)

    
    
S="""photo.jpg, Warsaw, 2013-09-05 14:08:15
john.png, London, 2015-06-20 15:13:22
myFriends.png, Warsaw, 2013-09-05 14:07:13
Eiffel.jpg, Paris, 2015-07-23 08:03:02
pisatower.jpg, Paris, 2015-07-22 23:59:59
BOB.jpg, London, 2015-08-05 00:02:03
notredame.png, Paris, 2015-09-01 12:00:00
me.jpg, Warsaw, 2013-09-06 15:40:22
a.png, Warsaw, 2016-02-13 13:33:50
b.jpg, Warsaw, 2016-01-02 15:12:22
c.jpg, Warsaw, 2016-01-02 14:34:30
d.jpg, Warsaw, 2016-01-02 15:15:01
e.png, Warsaw, 2016-01-02 09:49:09
f.png, Warsaw, 2016-01-02 10:55:32
g.jpg, Warsaw, 2016-02-29 22:13:11"""
print(organize_photos(S))