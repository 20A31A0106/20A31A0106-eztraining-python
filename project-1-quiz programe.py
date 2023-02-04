q1="""who eats more?
a.viswa
b.venky
c.kanakam
d.sriram"""

q2="""who likes to steal all money?
a.roja
b.jagan
c.modi
d.rana"""

q3="""who is the prettiest?
a.pinku
b.laya
c.bittu
c.rejoice"""

q4="""which is the best branch?
a.cse
b.mech
c.eee
d.none"""

q5="""who is the best singer?
a.harry
b.swift
c.priya
d.malone"""

questions={q1:"b",q2:"b",q3:"c",q4:"d",q5:"c"}

name=input(" hi whats ur name")
print("hello",name,"welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag=input("do you want to skip the question(yes or no)")
    if flag=="yes":
          continue
    ans=input("enter your answer")
    if ans== questions[i]:
       print("wow u got one point")
       score=score+1
       print("your current score is :",score)
    else:
        print("wrong ans u lost one mark")
        score=score-1
        print("ur current score is :",score)
    flag2=input("do u want to quit? ")
    if flag=="yes":
        break
    print("your total score",score)
