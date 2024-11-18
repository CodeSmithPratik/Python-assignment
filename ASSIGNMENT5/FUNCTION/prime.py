def checkPrime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return 0

        else:
            return 1

if __name__ == "__main__":
    numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,17]
    ansList = []
    for num in numberList:
        if num == 0 or num == 1:
            continue
        if checkPrime(num):
            ansList.append(num)
    if len(ansList):

        print("Prime Number of given list: ", end=" ")
        for ans in ansList:
            print(ans, end=", ")

    else:
        print("No any number from the given list is Prime")