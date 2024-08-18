print("Welcome to my computer quiz!")
playing= input("do you want to play? ")

if playing.lower()!="yes":
    quit()
print("okay !Lets play: )")
score = 0


Question1 = input ("what does CPU stand for? ")
if Question1.lower()=="central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")


Question2 = input ("What does GPU stand for?")
if Question2.lower() =="graphics processing unit":
    print("Correct!")
    score += 1  
else:
    print("Incorrect")


Question3 = input ("What does RAM stand for? ")
if Question3.lower() =="random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")


Question4 = input ("what does PSU stand for?")
if Question4.lower() =="power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%")









