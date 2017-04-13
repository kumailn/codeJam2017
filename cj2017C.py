def b(n, k):
    l = []
    l2 = []
    for i in range(n):
        l.append(0)
    l = [1] + l + [1]
    r = []
    rs = 0
    cc = 0
    ncc = 0
    #print(l)
    for i in l:
        if i == 1:
            l2.append(False)
        else:
            r = l[cc:]
            rs = r.index(1) - 1
            
            lls = closestOneLeft(cc, l)
                
            l2.append([lls, rs])
            #print(rs, lls)
        cc += 1
    #print(l2)
    counter1 = 0
    lg = 0
    for i in range(k):
        if len(maxMin(l2)) == 1:
            lg = maxMin(l2)[0]
            l[maxMin(l2)[0]] = 1
            l2[maxMin(l2)[0]] = False
            if counter1 == k-1:
                #print("last guy " + str(lg))
                #print("this", maxMin(l2), l, l2)
                #print(closestOneLeft(lg, l),closestOneRight(lg, l), "VALUES")
                #print("maxmin: " + str(max(closestOneLeft(lg, l),closestOneRight(lg, l))) + " " + str(min((closestOneLeft(lg, l),closestOneRight(lg, l)))))
                return [(max(closestOneLeft(lg, l),closestOneRight(lg, l))), (min((closestOneLeft(lg, l),closestOneRight(lg, l))))]
        else:
            lg = maxMax(l2)
            l[maxMax(l2)] = 1
            l2[maxMax(l2)] = False
            if counter1 == k-1:
                #print("last guy " + str(lg))
                #print(closestOneLeft(lg, l), closestOneRight(lg, l), "2VALUES")
                #print("maxmin: " + str(max(closestOneLeft(lg, l),closestOneRight(lg, l))) + " " + str(min((closestOneLeft(lg, l),closestOneRight(lg, l)))))
                return [(max(closestOneLeft(lg, l),closestOneRight(lg, l))), (min((closestOneLeft(lg, l),closestOneRight(lg, l))))]


        #print(str(counter1) + "COUNT!")
        for j in range(len(l2)):
            if l2[j] != False:
                r = l[j:]
                rs = r.index(1) - 1
                lls = closestOneLeft(j, l)
                l2[j] = [lls, rs]
        counter1 += 1
    
        #print(l, l2)
    print(l) #l2
            
    
def closestOneLeft(index, l):
    counter = 0
    for i in range(len(l)):
        if i == index:
            break
        if l[i] == 1:
            counter = 0
        else:
            counter += 1
    return counter

def closestOneRight(index, l):
    counter = 1
    for i in range(len(l)):
        if l[index + counter] == 0:
            counter += 1
        else:
            return counter - 1

def maxMin(l2):
    new_l = []
    for i in range(len(l2)):
        if l2[i] != False:
            new_l.append(min(l2[i]))
        else:
            new_l.append(-1)
    #print(new_l)
    all_i = [i for i, x in enumerate(new_l) if x == max(new_l)]
    #print(new_l)
    if len(all_i) > 1:
        return all_i
    else:
        return [new_l.index(max(new_l))]

def maxMax(l2):
    new_l = []
    p = []
    for i in range(len(l2)):
        if l2[i] != False:
            new_l.append(max(l2[i]))
        else:
            new_l.append(False)
    #print(new_l)
    cc = 0
    fl = []
    for i in maxMin(l2):
        fl.append(new_l[i])
    for i in maxMin(l2):
        #print(new_l[i], max(fl))
        if new_l[i] == max(fl):
            #print("yo")
            return i
    #return new_l.index(max(new_l))
            

def test(n):
    for i in range(n):
        print("#" + str(i) + " " + str(b(n,i)))

def t(n, k):
    if k > n*0.7:
        return [0,0]
def lr(l):
    r = []
    rs = 0
    cc = 0
    ncc = 0
    for i in l:
        if i == 1:
            pass
        else:
            r = l[cc:]
            rs = r.index(1) - 1

            lls = closestOneLeft(cc, l)
                
            
            print(rs, lls)
        cc += 1
    
