p=print
class print():
    def __init__(self, day1_2="aaaaaaaaaaa") -> None:
            self.two=True if day1_2==2 else False

            self.order()

    def _write(self, data):
        with open("logs_day1", "w") as f:
            f.write(data)

    def elf(self):
        with open("./day1") as text:
            elf=1
            for text in text:
                if text=="\n":elf+=1
        return elf
    
    def order(self):
        with open("./day1") as text:
            elf=1
            storage=[]
            adder=[]
            added=[]
            for text in text:   
                storage.append(text.split("\n"))

            for text in storage:
                if len(text)!=2:
                    x=sum(adder)+int(text[0])
                    added.append(x)
                elif text[0] == '':
                    added.append(sum(adder))
                    adder=[]
                else:
                    adder.append(int(text[0]))
                                
            E={}

            for elves in range(self.elf()):
                E.update({f"elf {elves+1}": added[elves]})
            
            E=dict(sorted(E.items(), key=lambda item: item[1]))
            x=[]
            for item in E:
                if self.two:
                    x.append(int(E[item]))
                else:    
                    x.append(f"{item} has {E[item]} total callories \n")

            x.reverse()

            if self.two:
                p(x[0]+x[1]+x[2])
                return
            x="".join(x).strip()
            x=f"FROM HIGHEST TOTAL CALORIES TO LOWEST\n\n{x}"
            p(x)
            ip=input("would you like to save data? (y/N) ")
            ip=True if ip.lower()=="y" else False
            if ip:
                self._write(x)
try:
    DAY=int(input("day\n"))
    print(DAY)
except Exception as e:
    p(f"NUMBERS ONLY \n\n {e}")