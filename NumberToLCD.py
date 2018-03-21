import sys

"""
   _  _     _  _  _  _  _  
 | _| _||_||_ |_   ||_||_|  
 ||_  _|  | _||_|  ||_| _|  
"""

charsTop    = " _     _  _     _  _  _  _  _ "
charsMedium = "| |  | _| _||_||_ |_   ||_||_|"
charsBottom = "|_|  ||_  _|  | _||_|  ||_| _|"

charsList = [charsTop,charsMedium,charsBottom]

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def getLineEachChars(number,chars):
    listNumbers = [int(num) for num in str(number)]
    listPrint   = map (lambda number: chars[number*3:number*3+3], listNumbers )
    return  reduce (lambda str1, str2: str1+str2,listPrint)

def printNumberToLCD(num):
    printChartsList = map (lambda chars: getLineEachChars(num, chars) ,charsList)
    return reduce (lambda str1,str2: str1+"\n"+str2,printChartsList) +"\n"

def main (argv):
    number = num(argv[1]) if len(argv) > 1 else 1234567890 
    print printNumberToLCD(number)

if __name__ == "__main__":
    main(sys.argv)  