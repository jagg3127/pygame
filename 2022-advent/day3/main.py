import string
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

def on(int_store):
    with open("day3") as eeeee:
        eeeee_list=[]
        for data in eeeee:
            eeeee_list.append(data)
        for string in eeeee_list:
            
            x=[]
            for a in string:
                x.append(a)
            x2=[]
            for a in range(len(x)):
                if len(x) // 2 > a:
                    x2.append(x[a])
            x3=[]
            for a in range(len(x)):
                if len(x) // 2 <= a:
                    x3.append(x[a])

            x2.sort()
            x3.sort()

            x2=set(x2)
            x3=set(x3)
            z=list(x3.symmetric_difference(x2))
            same=str

            for all in x:
                if all not in z:
                    same=all

            numerical_value=int
            if  same.upper() == same:
                numerical_value=cap(same)
            
            elif same.lower() ==  same:
                numerical_value=low(same)
            
            int_store+=numerical_value
            print(numerical_value, same, f"Upper: {same.upper() == same}", f"Lower: {same.lower() == same}", int_store)
            _write(f"{numerical_value} {same} Upper: {same.upper() == same} Lower: {same.lower() == same} {int_store}")



on(int_store)