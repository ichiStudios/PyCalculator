numbera = float(input("Enter Number"))
operator = input("Enter A Operator")
numberb = float(input("Enter Number"))

if operator == "+":
    print(numbera+numberb)
elif operator == "-":
    print(numbera - numberb)
elif operator == "/" or "÷":
    print(numbera / numberb)
elif operator == "*":
    print(numbera*numberb)
else:
    print("Incorrect Operator")
print("Thank" + " You!")
feedback = input("Did you like that?")
print("Thanks For You Feedback-You Said; " + feedback)