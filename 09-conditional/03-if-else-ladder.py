age = input("What is your present age? ")
integer_age = int(age)

if integer_age < 5:
    print("Oh come'on are you serious!")
elif integer_age < 18 and integer_age >= 5:
    print("Not eligible")
else:
    print("Eligible")   