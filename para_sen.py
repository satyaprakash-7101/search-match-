def biagram(l,m):
    j = []
    for i in range(len(l)):
        if l[i] == " ":
            j.append(i)
    print(j)
    for i in range(len(j)):
        if i == 0:
            m.append(l[0:j[1]])
        elif i > 0 and i != (len(j)-1):
            m.append( l[j[i-1]+1:j[i+1]])
        elif i == (len(j)-1):
            m.append( l[j[i-1]+1:(len(l)-1)])
    return(m)


def brea(l,a):
    j = 0
    for i in range(len(l)):
        
        if l[i] == ".":
            a.append(l[j:i])
            j = i+1
        if i == (len(l)-1):
            a.append(l[j:len(l)])
    return a

def per(s,n):
    t = ((2*(len(list(set(s) & set(n))))) / (len(s)+len(n)))
    print ("fraction matched:", t)
    return t

def cal(l,b):
    k = []
    n = []
    s = []
    k = brea(l,k)
    print(k)
    n = biagram(b,n)
    print(n)
    o = k[0]
    print(o)
    j = 0
    for i in k:
        print(i)
    for i in range(len(k)):
        s *= 0
        s = biagram(k[i],s)
        print (s)
        p = per(s, n)
        if p >j:
            j = p
            o = k[i]
    print ("the most matching word is:", o)

l = input("enter a paragraph:")
b = input("enter the sentence to search for a match:")
cal(l, b)
