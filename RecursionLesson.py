def recursiveFactorial(integer):
    if integer == 1:
        return 1
    else:
        return integer * recursiveFactorial(integer - 1)
    
def recursiveFibonacciSequence(sequenceValue):
    if sequenceValue == 0:
        return 0
    elif sequenceValue == 1:
        return 1
    else:
        return recursiveFibonacciSequence(sequenceValue - 1) + recursiveFibonacciSequence(sequenceValue - 2)

def recursiveStringReverse(string):
    if len(string) == 1:
        return string
    return string[len(string) - 1] + recursiveStringReverse(string[0:len(string) - 1])


if __name__ == "__main__":
    #Question 1
    print(recursiveFactorial(5))
    print(recursiveFactorial(3))
    print(recursiveFactorial(7))
    print(recursiveFactorial(1))
    print(recursiveFactorial(42))
    #Question 2
    print(recursiveFibonacciSequence(2))
    print(recursiveFibonacciSequence(0))
    print(recursiveFibonacciSequence(5))
    print(recursiveFibonacciSequence(8))
    print(recursiveFibonacciSequence(1))
    #Question 3
    print(recursiveStringReverse("apple"))
    print(recursiveStringReverse("hello"))
    print(recursiveStringReverse("recursive"))
    print(recursiveStringReverse("who"))
    print(recursiveStringReverse("sequence"))

