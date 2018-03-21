import sys

"""
   _  _     _  _  _  _  _  
 | _| _||_||_ |_   ||_||_|  
 ||_  _|  | _||_|  ||_| _|  
"""

charsTop    = " _     _  _     _  _  _  _  _ "
charsMedium = "| |  | _| _||_||_ |_   ||_||_|"
charsBottom = "|_|  ||_  _|  | _||_|  ||_| _|"

charsTopMoreTwo        = " _     _  _     _  _  _  _  _ "
charsMediumRepMoreTwo  = "| |  |  |  || ||  |    || || |"
charsMediumBaseMoreTwo = "       _  _  _  _  _     _  _ "
charsBottomRepMoreTwo  = "| |  ||    |  |  || |  || |  |"
charsBottomBaseMoreTwo = " _     _  _     _  _     _  _ "

charsListOneElement = [charsTop,charsMedium,charsBottom]

def num(s):
    try:
        return int(s)
    except ValueError:
        return 0

def printNumberToLCD(num, width, height):
    charsList = transformCharList(width, height)  
    printChartsList = map (lambda chars: getLineEachChars(num, chars, width) ,charsList)
    return reduce (lambda str1,str2: str1+"\n"+str2,printChartsList) +"\n"

def transformCharList(width, height):
    charsListHeight = charsListOneElement if height == 1 else createCharListHeight(height)  
    charsListWidthHeight = map(lambda charsHeight: createCharsListWidth(charsHeight, width), charsListHeight)
    return charsListWidthHeight

def createCharListHeight(height):
    charlist = []
    charlist.append(charsTopMoreTwo)
    [charlist.append(charsMediumRepMoreTwo) for _ in xrange(height) ]
    charlist.append(charsMediumBaseMoreTwo)
    [charlist.append(charsBottomRepMoreTwo) for _ in xrange(height) ]
    charlist.append(charsBottomBaseMoreTwo)
    return charlist

def createCharsListWidth(charsHeight, width):
    charts = map(lambda chars: chars,charsHeight)
    newCharts = []
    for n,chart in enumerate(charts):
        repeat = width if ((n+2) % 3) == 0 else 1
        [newCharts.append(chart) for _ in xrange(repeat)] 
    return reduce (lambda chart1, chart2: chart1+chart2, newCharts)

def getLineEachChars(number, chars, width):
    widthEl = width+2
    listNumbers = [int(num) for num in str(number)]
    listPrint   = map (lambda number: chars[number*widthEl:(number+1)*widthEl], listNumbers )
    return  reduce (lambda str1, str2: str1+str2,listPrint)

def main (argv):
    number = num(argv[1]) if len(argv) > 1 else 1234567890
    width  =  num(argv[2]) if len(argv) > 2 else 1
    height =  num(argv[3]) if len(argv) > 3 else 1
    print printNumberToLCD(number,width,height)

if __name__ == "__main__":
    main(sys.argv)  