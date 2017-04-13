def p(s,k):
    ns = s
    front_s = ""
    new_s = ""
    nss = mysplit(s, k)
    counter = 0
    cc = 0
    for i in s:
        if i == "-":
            front_s += "-"
        else:
            break
    new_s = s[len(front_s):] + front_s
    for i in range(len(s)):
        try:
            cs = new_s[i:i+k]
            if "+" not in cs:
                new_s[i:i+k] = r("+", k) 
        except:
            pass
        
    new_s = list(new_s)
    for i in range(len(new_s)):
        if "+" not in new_s[i:i+k]:
            new_s[i:i+k] = r("+", k)
            counter += 1
        elif "" in new_s[i:i+k]
            
    print(counter, new_s)
                
            


def r(s, n):
    ns = ""
    for i in range(n):
        ns += s
    return ns
        
def fl(l):
    s = ""
    for i in l:
        s += i
    return s

def mysplit(l, n):
    nl = []
    for i in range(0, len(l), n):
        nl += [l[i:i + n]]
    return nl
