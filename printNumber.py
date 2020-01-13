import math

class PrintNumber:
# creates word from given Int
# pram: numberGiven - int
# return: string, word created from number
    def __init__(self, numberGiven):
        self.numberGiven = numberGiven
        self.decodedNumber = []
        self.wordFromNum = ''
        self.doubleDigPosition = []
        self.houndredDigPosition = []
        
        self.decodeDig()
        self.makeWordFromNum()

    def __str__(self):
        return self.wordFromNum

    def decodeDig(self):
        # creates list with individual digits from passed number
        divider = 10
        while True:
            self.decodedNumber.append(self.numberGiven % divider)
            divider = divider * 10
            if(divider > self.numberGiven):
                # last digint is outside of the condition
                self.decodedNumber.append(self.numberGiven % divider)
                break
        for i, self.numberGiven in enumerate(self.decodedNumber):
            #print(number, i)
            if (i>=1):
                self.decodedNumber[i] = int(self.round_down((self.decodedNumber[i] - self.decodedNumber[i-1]) / 10**i))


    def round_down(self, n, decimals=0):
        # found this on internet
        # rounds given muber down
        multiplier = 10 ** decimals
        return math.floor(n * multiplier) / multiplier

    def makeWordFromNum(self):
        # goes through items in decodedNumber and creates word based on givenNumber
        decPos = len(self.decodedNumber) - 1
        
        # cretes list with dig positioons that you can say in one word exp. one, six
        # if not decPos is not in this list you have say twelve, forty...   
        curDecPos = 1
        curDecPosIndx = 0
        while (curDecPosIndx <= decPos):
            self.doubleDigPosition.append(curDecPos)
            curDecPos += 3
            curDecPosIndx +=1

        # cretes list with dig  that you can say hounderd
        curDecPos = 2
        curDecPosIndx = 0
        while (curDecPosIndx <= decPos):
            self.houndredDigPosition.append(curDecPos)
            curDecPos += 3
            curDecPosIndx +=1
        
        # goes through items in decodedNumber and decides how would you say given number
        while (decPos >= 0):
            if(decPos not in self.doubleDigPosition):
                self.wordFromNum += self.getUpTwoDig(self.decodedNumber[decPos]) + \
                                    self.getDecPos(self.decodedNumber[decPos], decPos)
                decPos -=1
            else:
                lastDig = (int(self.decodedNumber[decPos - 1])) * 10**(decPos-1)
                secondLastDig = (int(self.decodedNumber[decPos])) * 10**decPos  
                lastDigsCombined = int((lastDig + secondLastDig) * 10**(-(decPos-1)))
                if(decPos > 1):
                    self.wordFromNum += self.getUpTwoDig(lastDigsCombined) + self.getDecPos(self.decodedNumber[decPos], decPos)
                else:
                    self.wordFromNum += self.getUpTwoDig(lastDigsCombined)
                decPos -= 2

    
    def getDecPos(self, dig, dec_pos):
        # returns string based on digit position
        if(dec_pos == 0):
            return ''
        elif (dec_pos == 1):
            return self.getUpTwoDig(dig)
        elif (dec_pos in self.houndredDigPosition):
            return 'houndred '
        elif (dec_pos < 6):
            return 'tousand '
        elif (dec_pos < 9):
             return 'milion '
    
    def getUpTwoDig(self, number):
        # returns string based on input number
        stringToReturn = ''
        if (number == 0):
            return ''
        elif (number == 1):
            return 'one '
        elif (number == 2):
            return 'two '
        elif (number == 3):
            return 'three '
        elif (number == 4):
            return 'four '
        elif (number == 5):
            return 'five '
        elif (number == 6):
            return 'six '
        elif (number == 7):
            return 'seven '
        elif (number == 8):
            return 'eight '
        elif (number == 9):
            return 'nine '  
        elif (number == 10):
            return 'ten '
        elif (number == 11):
            return 'eleven '
        elif (number == 12):
            return 'twelve '
        elif (number == 13):
            return 'threteen '
        elif (number == 14):
            return self.getUpTwoDig(4) + 'teen '
        elif (number == 15):
            return  self.getUpTwoDig(5) + 'teen '
        elif (number == 16):
            return  self.getUpTwoDig(6) + 'teen '
        elif (number == 17):
            return  self.getUpTwoDig(7) + 'teen '
        elif (number == 18):
            return  self.getUpTwoDig(8) + 'teen '
        elif (number == 19):
            return  self.getUpTwoDig(9) + 'teen ' 
        elif (number <= 29):
            numberToPass = number - 20
            stringToReturn += 'twenty ' + self.getUpTwoDig(numberToPass)
            return stringToReturn 
        elif (number <= 39):
            numberToPass = number - 30
            stringToReturn += 'threety ' + self.getUpTwoDig(numberToPass)
            return stringToReturn     
        elif (number <= 49):
            numberToPass = number - 40
            stringToReturn += 'forty ' + self.getUpTwoDig(numberToPass)
            return stringToReturn     
        elif (number <= 59):
            numberToPass = number - 50
            stringToReturn += 'fifty ' + self.getUpTwoDig(numberToPass)
            return stringToReturn
        elif (number <= 69):
            numberToPass = number - 60
            stringToReturn += 'sixty ' + self.getUpTwoDig(numberToPass)
            return stringToReturn
        elif (number <= 79):
            numberToPass = number - 70
            stringToReturn += 'seventy ' + self.getUpTwoDig(numberToPass)
            return stringToReturn     
        elif (number <= 89):
            numberToPass = number - 80
            stringToReturn += 'eighty ' + self.getUpTwoDig(numberToPass)
            return stringToReturn
        elif (number <= 99):
            numberToPass = number - 90
            stringToReturn += 'ninty ' + self.getUpTwoDig(numberToPass)
            return stringToReturn


if (__name__ == "__main__"):
    myOrgMun = 200655102
    myMun = PrintNumber(myOrgMun)
    print(myMun)
    print(PrintNumber(45687))

