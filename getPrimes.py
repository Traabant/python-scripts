from random import randint
from printNumber import PrintNumber


class getPrimes:
    # expects maximum as parametr
    # then it creates lsit self.primeNumList
    # list is filled up wit just prime numbers with method self.calPrimes
    # parm: maxNun - int
    # return: string 
    def __init__(self, maxNum):
        self.primeNumList = [2]
        self.maxNum = maxNum
        self.lastPrime = None
        self.calcPrimes()

    def __str__(self):
        return (
            f'Found {PrintNumber(len(self.primeNumList))}({len(self.primeNumList)}) '
            f'prime numbers \nhere is '
            f'random one: {self.primeNumList[randint(0,len(self.primeNumList))]}'
            )
    
    def calcPrimes(self):
    # fillup list with just prime numbers
        curNum = 3        
        while (curNum <= self.maxNum):
            isPrime = True
            for num in self.primeNumList:
                if (curNum % num == 0):
                    isPrime = False
                    break
            if(isPrime is True):
                self.primeNumList.append(curNum)
            curNum += 1 


if (__name__ == "__main__"):
    myPrime = getPrimes(1000)
    print(myPrime)
        