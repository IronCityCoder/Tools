'''
Zachary Bailey
Encoder/Decoder for various forensic uses.

Things to be done: 
 - Add command line arguments
 - Allow for multiple passings
'''
#This function enables the calling of a variable. 
def callFunction(fn):
    fn()
    
#Dictionary for hex values.
hex = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9, "A": 10, "B": 11, "C":12, "D":13, "E":14, "F":15}

#Options menu.
options = ["HexToDecimal", "DecimalToHex"]

#The main loop asks the user what they want to decode. 
def mainLoop():
    while True:
        print("What would you like to decode? Options are: ")
        for i, word in enumerate(options):
            print(str(i+1) + "| " + word)
        response = input()
        if response in options:
            callFunction(globals()[response])
            break

def HexToDecimal():
    hexNumber = input("Please enter a hex value starting with x: ")
    if hexNumber[0] != "x":
        print("Please enter a valid hex numer!")
        HexToDecimal()
    total = 0
    for i, value in enumerate(hexNumber[1:]):
        if value in hex:
            total += hex.get(value) * (16**(len(hexNumber[1:])-i-1))
    print(total)
    
def DecimalToHex():
    decNumber = int(input("Please enter a decimal number:"))
    total = []
    final = ""
    while decNumber > 0:
        total.append(decNumber%16)
        decNumber = decNumber // 16
    total.reverse()
    
    for i in total:
        for j in hex:
            if hex.get(j) == i:
                final += str(j)
    print(final)
            

mainLoop()
        