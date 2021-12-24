print("welcome to python quiz");

playing=input("Do you want to play :");

if playing.lower() != "yes":
    quit()
print("okay!lets play...");
score=0
answer=input("who developed python?")
if answer.lower() == "guido van rossum" :
    print("correct!")
    score=+1
else:
    print("incorrect!")
    
answer=input("what is the correct extension of python file?")
if answer.lower() == ".py":
    print("the second answer is right!")
    score=score+1
else:
    print("incorrect answer!")
    
answer = input("what do we use to define a block of code in python?")
if answer.lower() == "indentation":
    print("the third answer is right !")
    score=score+1
else:
    print("incorrect answer!")
    
answer=input("what are collections of objects called?")
if answer.lower() == "classes":
    print("the fourth answer is right!")
    score=score +1
else:
    print("incorrect!")

answer=input("what are methods inside the class in python")
if answer.lower() =="functions":
    print("the fifth answer is correct!")
    score=score+1
else:
    print("incorrect!")
answer=input("what are syntax errors also called as?")
if answer.lower() =="parsing errors":
    print("the sixth answer is correct!")
    score=score+1
else:
    print("incorrect!")
answer=input("what is a sequence of characters that form a search pattern?")
if answer.lower() =="regular expressions":
    print("the seventh answer is correct!")
    score=score+1
else:
    print("incorrect!")
answer=input("what are entity of a class")
if answer.lower() =="objects":

    print("the eight answer is correct!")
    score=score+1
    
else:
    print("incorrect!")
answer=input("what are the functions called which calls itself repeatedly?")
if answer.lower() ==" recursive functions":
    print("the ninth answer is correct!")
    score=score+1
else:
    print("incorrect!")
answer=input("what are specified after function name,inside parameters")
if answer.lower() =="arguments":
    print("the tenth answer is correct!")
    score=score+1
else:
    print("incorrect!")
print("you got "+str(score)+" questions correct!")
print("you have got:"+str((score/10)*100)+"%")
