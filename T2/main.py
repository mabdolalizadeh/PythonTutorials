# methods

def checkRange(age, rangeN1, rangeN2):
    if rangeN1 <= age <= rangeN2:
        return True
    else:
        return False


def checkMail(gender):
    if gender[0] == 'm':
        return True
    else:
        return False


def checkMovie(type):
    if type[0] == 'm':
        return True
    else:
        return False


# base codes

age = input("Enter your age: ")
gender = input("Enter your gender: ")
type = input("What type do you want? ")

if checkRange(age, 0, 16) and checkMail(gender) and checkMovie():
    print("You should see Coco")
elif checkRange(age, 0, 16) and checkMail(gender) and not checkMovie():
    print("You should see Stranger Things")
elif checkRange(age, 0, 16) and not checkMail(gender) and checkMovie():
    print("You should see Frozen")
elif checkRange(age, 0, 16) and not checkMail(gender) and not checkMovie():
    print("You should see Madereseh Mushha")
elif checkRange(age, 17, 35) and checkMail(gender) and checkMovie():
    print("You should see Fight Club")
elif checkRange(age, 17, 15) and checkMail(gender) and not checkMovie():
    print("You should see Peaky Blinders")
elif checkRange(age, 17, 35) and not checkMail(gender) and checkMovie():
    print("You should see Titanic")
elif checkRange(age, 17, 35) and not checkMail(gender) and not checkMovie():
    print("You should see Friends")
elif checkRange(age, 36, 50) and checkMail(gender) and checkMovie():
    print("You should see Its a WonderFul Life")
elif checkRange(age, 36, 50) and checkMail(gender) and not checkMovie():
    print("You should see Fargo")
elif checkRange(age, 36, 50) and not checkMail(gender) and checkMovie():
    print("You should see Gone with the wind")
elif checkRange(age, 36, 50) and not checkMail(gender) and not checkMovie():
    print("You should see Sharzad")
