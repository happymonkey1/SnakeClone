from math import ceil
#Question 1
def my_zip(*args):
    returnList = []
    argsCopy = [i for i in args]
    while True:
        tempList = []
        for arg in argsCopy:
            if len(arg) == 0:
                return returnList
            else:
                tempList.append(arg.pop(0))
        tempTuple = tuple(tempList)
        returnList.append(tempTuple)


#Question 2
def lerp(minPos, maxPos, smoothing):
    determineXValue = ceil(minPos[0] * (1 - smoothing) + maxPos[0] * smoothing)
    determineYValue = ceil(minPos[1] * (1 - smoothing) + maxPos[1] * smoothing)
    return (determineXValue, determineYValue)

if __name__ == "__main__":
    #Question 1
    print(my_zip([1,2,3], ["a","b","c"]))
    print(my_zip([0, 0, 0], [1,1,1], ["a","a","a"]))
    print(my_zip([1,2,3], ["a"]))
    print(my_zip([], [1,2,3,4,5]))
    #Question 2
    print(lerp((0,0), (2,2), 0.5))
    print(lerp((0,0), (5,5), 0.2))
    print(lerp((0,0), (8,8), 0.2))