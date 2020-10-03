#! /bin/python3

# Andrew Barlow
# Solve for a given variable in the Solow production model

# for advanced input
import pyinputplus as pyin
import sys

# Define a class for the Solow model
class solow:
    def __init__(self, labor, productivity, saveRate, depreciationRate):
        self.labor = labor
        self.productivity = productivity
        self.saveRate = saveRate
        self.depreciationRate = depreciationRate

    # Solving for Capital
    def solveK(self):
        numerator = self.saveRate * self.productivity
        return self.labor * pow( (numerator / self.depreciationRate), (3/2) )

    # Solving for Production
    def solveY(self):
        part1 = pow( self.productivity, (3/2) )
        part2 = pow( (self.saveRate * self.productivity) / self.depreciationRate, (1/2) )
        return part1 * part2 * self.labor
    
    # Solving for Investment
    def solveI(self):
        part1 = self.saveRate * pow(self.productivity, (3/2) )
        part2 = pow( ( (self.saveRate * self.productivity) / self.depreciationRate), (1/2) )
        return part1 * part2 * self.labor

    # Solving for Consumption
    def solveC(self):
        part1 = (1 - self.saveRate) * pow(self.productivity, (3/2))
        part2 = pow( ((self.saveRate * self.productivity) / self.depreciationRate), (1/2) )
        return part1 * part2 * self.labor

    # Solve for x, aka call appropriate function based on string
    def solveX(self, x):
        if x == 'K':
            return self.solveK()
        elif x == 'Y':
            return self.solveY()
        elif x == 'I':
            return self.solveI()
        elif x == 'C':
            return self.solveC()

# Print a usage statement on error
def usage():
    print("USAGE:")
    print("./solow.py $1 $2 $3 $4  with number arguments")
    print("OR")
    print("./solow.py to enter the cli")

def init():
    print("Andrew Barlow")
    print("Type h to get usage")

# Get input for which variable to solve for
def getInput():
    result = input()
    if (result not in [ 'K', 'Y', 'I', 'C', 'h'] ):
        print("Error: invalid input")
        return getInput()
    else:
        return result

# Ask the user for input and validate using pyinputplus
def getParams():
    labor = pyin.inputNum("Enter labor: ")
    productivity = pyin.inputNum("Enter productivity factor: ")
    saveRate = pyin.inputNum("Enter savings rate: ")
    depreciationRate = pyin.inputNum("Enter depreciation rate: ")
    
    params = {
        "labor" : float (labor),
        "productivity" : float (productivity),
        "saveRate" : float (saveRate),
        "depreciationRate" : float (depreciationRate)
        }

    return params

def cli():
    init()
    while (1):
        print("Enter the variable to be solved (K, Y, I, C)")
        process = getInput()

        # if user asks for help, display usage, restart loop
        if process == 'h':
            usage()
            break

        params = getParams()
        result = solow( params["labor"], params["productivity"], params["saveRate"], params["depreciationRate"] )
        print ( result.solveX(process) )


def main():
    # if called from command line, go ham
    if len (sys.argv) == 5:
        arg1 = float ( sys.argv[1] )
        arg2 = float ( sys.argv[2] )
        arg3 = float ( sys.argv[3] )
        arg4 = float ( sys.argv[4] )

        #args = float ( sys.argv[1]::sys.argv[4] )
        result = solow(arg1, arg2, arg3, arg4)
        for i in ['K', 'Y', 'I', 'C']:
            print(i, ' = ', result.solveX(i) )

    elif len(sys.argv) == 1:
        cli()
    else:
        usage()

try:
    main()
except KeyboardInterrupt:
    print()
    print("Continue being excellent")
