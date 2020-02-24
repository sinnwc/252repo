# Simple bouncer program written as a project for Udemy Python Course

# ask for age
age = input("How old are you: ")
if age != "":
    age = int(age)
    if age >= 18 and age < 21: #compares ages within constraint of 18 - 21, need wristband
        print("You can enter, but need a wristband.")
    elif age >= 21: # checks for people who do not need wristbands
        print("You are good to enter, and can drink.")
    # otherwise, too young
    else:
        print("You can't come in, friend. :(")
else:
    print("You didn't enter your age.") # makes sure that there is a valid, non-null entry for age