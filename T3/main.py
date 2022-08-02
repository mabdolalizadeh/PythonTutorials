firsNames = []
lastNames = []


def calc_tax(name, income=0):
    newName = name.split(' ')
    firsNames.append(newName[0])
    lastNames.append(newName[1])
    print(firsNames)
    print(lastNames)
    if income == 0:
        income = int(input("Enter income: "))
    if income >= 36000000:
        print("tax price is %d", income * 0.12)
    else:
        print("tax price is %d", income * 0.09)


calc_tax("ali sabory")
