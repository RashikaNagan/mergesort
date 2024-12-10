numbers = [3,7,12,42,66,32,1,65,23]

def desendingnr():
    for i in range(0,len(numbers)-1):
        for a in range(0,len(numbers)-1-i):
            if numbers[a] < numbers[a+1]:
                numbers[a], numbers[a+1] = numbers[a+1], numbers[a]
                
    print(numbers)

desendingnr()

