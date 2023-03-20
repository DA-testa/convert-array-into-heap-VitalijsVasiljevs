#221RDB265
import re
def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        swaps = swaping(i, swaps, data)
    return swaps

def swaping(nowSwapIndex, swaps, data):
    n = len(data)
    swapIndex1 = nowSwapIndex * 2 + 1
    swapIndex2 = nowSwapIndex * 2 + 2
    if swapIndex1 >= n:
        return swaps
    if swapIndex2 >= n or data[swapIndex1] < data[swapIndex2]:
        minSwapIndex = swapIndex1
    else:
        minSwapIndex = swapIndex2
    if data[nowSwapIndex] > data[minSwapIndex]:
        data[nowSwapIndex], data[minSwapIndex] = data[minSwapIndex], data[nowSwapIndex]
        swaps.append((nowSwapIndex, minSwapIndex))
        swaps = swaping(minSwapIndex, swaps, data)
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
