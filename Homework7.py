#Question 1
def decimal_to_binary(decimalValue):
    decimalCopy = decimalValue
    binaryValue = []
    binaryNum = 0
    finalBinaryValue = ""
    while decimalCopy != 0:
        binaryNum = decimalCopy % 2
        if binaryNum > 0:
            binaryValue.append(1)
        else:
            binaryValue.append(0)
        decimalCopy = decimalCopy // 2
    for num in reversed(binaryValue):
        if num == 1:
            finalBinaryValue = finalBinaryValue + "1"
        elif num == 0:
            finalBinaryValue = finalBinaryValue + "0"
    return finalBinaryValue

#Question 2
def binary_to_decimal(binaryValue):
    finalEquation = []
    intBinary = []
    for char in binaryValue:
        intBinary.append(int(char))
    for index,num in enumerate(reversed(intBinary)):
        finalEquation.append(num*(2**index))
    return sum(finalEquation)

if __name__ == "__main__":
    print("start")
    #Question 1
    print(decimal_to_binary(1))
    print(decimal_to_binary(2))
    print(decimal_to_binary(6))
    print(decimal_to_binary(5))
    print(decimal_to_binary(8))
    print(decimal_to_binary(10))
    #Question 2
    print(binary_to_decimal("1"))
    print(binary_to_decimal("10"))
    print(binary_to_decimal("110"))
    print(binary_to_decimal("101"))
    print(binary_to_decimal("1000"))
    print(binary_to_decimal("1010"))
    print(binary_to_decimal(decimal_to_binary(760)))
    print("done")