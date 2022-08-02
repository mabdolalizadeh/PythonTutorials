# methods

def checkRange(age, rangeN1, rangeN2):
    if rangeN1 <= age <= rangeN2:
        return True
    else:
        return False


def checkMale(gender):
    if gender[0] == 'm':
        return True
    else:
        return False


def checkMovie(kind):
    if kind[0] == 'm':
        return True
    else:
        return False


# base codes

age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
kind = input("What type do you want? ")

if checkRange(age, 0, 16) and checkMale(gender) and checkMovie(kind):
    print("You should see Coco")
elif checkRange(age, 0, 16) and checkMale(gender) and not checkMovie(kind):
    print("You should see Stranger Things")
elif checkRange(age, 0, 16) and not checkMale(gender) and checkMovie(kind):
    print("You should see Frozen")
elif checkRange(age, 0, 16) and not checkMale(gender) and not checkMovie(kind):
    print("You should see Madereseh Mushha")
elif checkRange(age, 17, 35) and checkMale(gender) and checkMovie(kind):
    print("You should see Fight Club")
elif checkRange(age, 17, 15) and checkMale(gender) and not checkMovie(kind):
    print("You should see Peaky Blinders")
elif checkRange(age, 17, 35) and not checkMale(gender) and checkMovie(kind):
    print("You should see Titanic")
elif checkRange(age, 17, 35) and not checkMale(gender) and not checkMovie(kind):
    print("You should see Friends")
elif checkRange(age, 36, 50) and checkMale(gender) and checkMovie(kind):
    print("You should see Its a WonderFul Life")
elif checkRange(age, 36, 50) and checkMale(gender) and not checkMovie(kind):
    print("You should see Fargo")
elif checkRange(age, 36, 50) and not checkMale(gender) and checkMovie(kind):
    print("You should see Gone with the wind")
elif checkRange(age, 36, 50) and not checkMale(gender) and not checkMovie(kind):
    print("You should see Sharzad")
