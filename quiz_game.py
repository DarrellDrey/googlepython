print("Welcome to my computer quiz")

playing = input("Do you want to play my game? " )

if playing != "yes":
    quit()

print("Okay let's play!")
score= 0


answer= input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!") 
    score += 1
else:
    print("Incorrect!")

answer= input("What does ROM stand for? ").lower()
if answer == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer= input("What does OS stand for? ").lower()
if answer == "operating system":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer= input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer= input("What does GPU stand for? ").lower()
if answer == "graphics Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("you got " + str(score) + " answers correct")
print("you got " + str((score / 4) * 100) + "%" )