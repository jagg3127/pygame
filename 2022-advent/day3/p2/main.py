import string
A1=[]
A2=[]
A3=[]

with open("day3") as e:
    timer=1
    for a in e:
        a=a.strip()
        if   timer==1:
            A1.append(a)
            timer=2
        elif timer==2:
            A2.append(a)
            timer=3
        elif timer==3:
            A3.append(a)
            timer=1
    
    A1.append("ADMIN")
    A2.append("ADMIN")
    A3.append("ADMIN")


def low(l: str):return string.ascii_lowercase.index(l)+1
def cap(l: str):return string.ascii_uppercase.index(l)+27

int_store=0

def _write(data, u=True):
    if u:
        with open("logs_day3", 'a') as f:
            f.write(f"{data}\n")
    else:
        with open("logs_day3", "w") as f:
            f.write(data)


while A1[0]!="ADMIN" or A2[0]!="ADMIN" or A3[0]!="ADMIN":
    a1=[]
    a2=[]
    a3=[]

    all_data=[]

    for s in A1[0]:
        all_data.append(s)
        a1.append(s)

    for s in A2[0]:
        all_data.append(s)
        a2.append(s)

    for s in A3[0]:
        all_data.append(s)
        a3.append(s)

    A1.pop(0)
    A2.pop(0)
    A3.pop(0)

    all_data.sort()
    all_data=list(set(all_data))

    a1.sort()
    a2.sort()
    a3.sort()

    x1=set(a1).symmetric_difference(a2)
    x2=set(a2).symmetric_difference(a3)
    x3=set(a3).symmetric_difference(a1)




    x4=list(x1)
    x5=list(x2)
    x6=list(x3)

    x4.sort()
    x5.sort()
    x6.sort()

    x4.extend(x5)
    x4.extend(x6)

    x4.sort()

    s5=list(set(x4))
    s5.sort()

    same=[]

    for all in all_data:
        if all not in s5:
            print(all)
            same.append(all)

    numerical_value=int
    same=same[0]
    if  same.upper() == same:
        numerical_value=cap(same)
    
    elif same.lower() ==  same:
        numerical_value=low(same)
    
    int_store+=numerical_value
    _write(f"{numerical_value} {same} Upper: {same.upper() == same} Lower: {same.lower() == same} {int_store}")


    #print("".join(same), A1, A2, A3)