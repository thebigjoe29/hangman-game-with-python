import random
f=random.randint(0,4)
tp=("apple","banana","orange","pears","pomegranate")
secw=tp[f]
ctr=0
n=int(input("enter no of tries: "))
if n>2:
    while ctr<n:
        x=input("enter guess: ")
        if x.isalpha():
         if x.lower()==secw.lower():
            print("you won!")
            break
         elif x!=secw:
             for i in x:
              if i in secw:
                 print(i, end="")
             ctr+=1
         else:
            ctr+=1
         if ctr==2:
            r=input("do you want a hint?: ").lower()
            if r=="y":
                print("%c",endl = "\n") % (secw[0])
        else:
            print("Invalid input")
    if ctr==n:
     print("you lost!")
