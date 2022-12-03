p=print


class store:
    file=[]
    pts_sys= {"r": 1, "p": 2, "s": 3}
    states = {"w":6 , "d":3 , "f":0}

    sort=[]


class print:
    def _write(self, data, u=False):
        if u:
            with open("logs_day2", 'a') as f:
                f.write(f"{data}\n")
        else:
            with open("logs_day2", "w") as f:
                f.write(data)

    def main(self):
        pts    = store.pts_sys
        states = store.states
        you    = 0
        enemy  = 0
        test   = []
        self._write("")
        with open('./day2') as day2:
            for data in day2:
                store.file.append(data.strip().split(' '))
            
            for items in store.file:
                xed  = 0
                xed2 = 0
                x    = items[0].lower()
                x2   = items[1].lower()
                
                p(you)
                self._write(str(you), True)

                if   x2=='x':           xed2=1
                elif x2=='y': you=you+3;xed2=2
                elif x2=='z': you=you+6;xed2=3

                p(you)
                self._write(str(you), True)
                
                if xed2==1: #tie
                    if   x=='a': you+=3
                    elif x=='b': you+=1
                    elif x=='c': you+=2
                
                elif xed2==2: #lose
                    if   x=='a': you+=1
                    elif x=='b': you+=2
                    elif x=='c': you+=3
                
                elif xed2==3: #win
                    if   x=='a': you+=2
                    elif x=='b': you+=3
                    elif x=='c': you+=1
                


                p(you, xed, xed2)
                self._write(f"{str(you)} {str(xed)} {str(xed2)}", True)



        p(you)




print().main()
