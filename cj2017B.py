import sys
import os
from sys import stdin

def tidyNum(n):
    ns = str(n)
    if checkTidy(n) == True:
        return n
    
    for i in range(n, -1, -1):
        if checkTidy(i) == True:
            return i
        else:
            pass

def checkTidy(n):
    n2 = str(n)
    for i in range(len(n2)-1):
        if int(n2[i]) <= int(n2[i+1]):
            pass
        else:
            return False
    return True

def bigNum(n):
    ns = str(n)
    cc = 0
    if checkTidy(n) == True:
        return n
    
    for i in range(len(ns) - 1):
        if checkTidy(ns[:i+1]) == True:
            #print("YEAH")
            cc += 1
        else:
            #print(cc)
            break
    print(cc)
    if cc == 1:
        l = len(ns)
        f = int(ns[0])
        o = ""
        for i in range(l - 1):
            o = o + "9"
        if f != 1:
            o = str(f-1) + o
        return int(o)
            
    else:
        ns2 = ns[cc-1:]
        ns3 = ns[:cc-1]
        print(ns2)
        print(ns3)
        n1 = bigNum(int(ns2))

        new_n = str(ns3) + str(n1)
    return int(new_n)



cf = open("B-small-attempt4.in", "r")
l = []
for i in cf:
    l.append(int(i))
cf.close()

print(l)
for i in l:
    print(int(i))
cc = 0
f = open("n.txt","w")
for i in l:
    if cc > 0:
            f.write("Case #" + str(int(cc)) + ": " + str(bigNum(int(i))) + "\n")
    cc += 1
    
f.close()

