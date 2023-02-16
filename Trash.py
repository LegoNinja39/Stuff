
def smallest(x: list[int]):
    smallInt: int = x[0]
    for i in range(1, len(x)):
        if x[i] < smallInt: smallInt = x[i]

    return smallInt
lOne = [x for x in range(5)]
lTwo = [x for x in range(5)]
def matrixMaker(A: list[int], B: list[int]):
    numberOfOnes = 0
    matrixRow = []
    for eleA in A:
        for eleB in B:
            
            if eleA > eleB:
                numberOfOnes += 1
                print(eleA, eleB)
            matrixRow.append(1) if eleA > eleB else matrixRow.append(0)
        #print(matrixRow)
        matrixRow.clear()
    
    print(numberOfOnes)

matrixW = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0]
]
matrix1 = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 0, 1]
]

matrix2 = [
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 1]
]

matrix3 = [
    [1, 0, 1],
    [0, 1, 1],
    [0, 1, 0]
]

matrix4 = [
    [0, 1, 0, 1],
    [1, 0, 0, 0],
    [0, 0 , 0, 1],
    [0, 0, 0 , 0]
]

def warshall(M: list[list[int]]):
    for k in range(len(M)):
        for i in range(len(M)):
            for j in range(len(M)):
                M[i][j] |= (M[i][k] & M[k][j])
                
    print(*[l for l in M], sep="\n")

warshall(matrix4)

def myst(A: list[int], index, result):
    if (index < len(A)):
        return myst(A, index+1, result*A[index])
    else:
        return result

thing = [2,3,4,1]
print(myst(thing, 1, 1))

def mf():
    yield 1
    yield 'a'
    yield False

print(mf())

hours = 0
rate = 0
def employeeInformation():
    global hours, rate
    name = input("What is your name ")
    try:
        hours = float(input("Please enter hours worked "))
        rate = float(input("Please enter hourly rate "))

        print(name)
        print("Hours: " + str(hours))
        print(rate)

    except:
        print("Error, please enter a numerical value.")

def overTimePay(totalHours):
    extraTime = totalHours - 40 if totalHours > 40 else 0
    extraPay = 0.5 * rate * extraTime
    return extraPay

employeeInformation()
print(hours)
pay = hours * rate + overTimePay(hours)

print(pay)

score = float(input("Please enter score "))
grade = "F"
if score > 0 and score < 1:
    if score >= 0.9: grade = "A"
    elif score >= 0.8: grade = "B"
    elif score >= 0.7: grade = "C"
    elif score >= 0.6: grade = "D"
    print(grade)
else:
    print("Invalid score")