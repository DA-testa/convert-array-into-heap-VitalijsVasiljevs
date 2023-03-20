import re
def build_heap(data):
    swaps = []
    firstSwapIndex = len(data) // 2 - 1
    swaps = swaping(firstSwapIndex, swaps, data)
    return swaps

def swaping(nowSwapIndex, swaps, data):

    
    swapIndex1 = nowSwapIndex * 2 + 1
    swapIndex2 = nowSwapIndex * 2 + 2
    if swapIndex1 == len(data) - 1:
        if data[nowSwapIndex] > data[swapIndex1]:
            data[nowSwapIndex], data[swapIndex1] = data[swapIndex1], data[nowSwapIndex]
            swaps.append([nowSwapIndex, swapIndex1])
            if len(data) // 2 - 1 >= swapIndex1:
                swaps = swaping(swapIndex1, swaps, data)
    elif data[swapIndex1] > data[swapIndex2]:
        if data[nowSwapIndex] > data[swapIndex2]:
            data[nowSwapIndex], data[swapIndex2] = data[swapIndex2], data[nowSwapIndex]
            swaps.append([nowSwapIndex, swapIndex2])
            if len(data) // 2 - 1 >= swapIndex1:
                swaps = swaping(swapIndex2, swaps, data)
    else:
        if data[nowSwapIndex] > data[swapIndex1]:
            data[nowSwapIndex], data[swapIndex1] = data[swapIndex1], data[nowSwapIndex]
            swaps.append([nowSwapIndex, swapIndex1])
            if len(data) // 2 - 1 >= swapIndex1:
                swaps = swaping(swapIndex1, swaps, data)
    nowSwapIndex = nowSwapIndex - 1
    if nowSwapIndex == -1:
        return swaps
    swaps = swaping(nowSwapIndex, swaps, data)
    return swaps

def main():
    mode = input()  
    if ((re.sub("[\r\n]", "", mode) == "I")) :
        n = input()
        n = int(re.sub("[\r\n]", "", n))
        data = list(map(int, input().split()))
        assert len(data) == n
                               
    elif (re.sub("[\r\n]", "", mode) == "F") : 
      
        number_test = input()
        number_test = re.sub("[\r\n]", "", number_test)
        file_name = "tests/" + number_test
        with open(file_name, 'r') as f:
            lines = f.readlines()
            data = [int(num) for num in lines[1].split()]      
    pass
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)



if __name__ == "__main__":
    main()
