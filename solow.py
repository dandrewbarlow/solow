# Andrew Barlow
# Solve for a given variable in the Solow production model

# for advanced/easy input checking
import pyinputplus as pyin

# Solving for Capital
def solveK(labor, productivity, saveRate, depreciationRate):
    numerator = saveRate * productivity
    return labor * pow( (numerator / depreciationRate), (3/2) )

# Solving for Production
def solveY(labor, productivity, saveRate, depreciationRate):
    part1 = pow( productivity, (3/2) )
    part2 = pow( (saveRate * productivity) / depreciationRate, (1/2) )
    return part1 * part2 * labor

# Solving for Investment
def solveI(labor, productivity, saveRate, depreciationRate):
    part1 = saveRate * pow(productivity, (3/2) )
    part2 = pow( ( (saveRate * productivity) / depreciationRate), (1/2) )
    return part1 * part2 * labor

# Solving for Consumption
def solveC(labor, productivity, saveRate, depreciationRate):
    part1 = (1 - saveRate) * pow(productivity, (3/2))
    part2 = pow( ((saveRate * productivity) / depreciationRate), (1/2) )
    return part1 * part2 * labor

def getInput():
    result = input()
    if (result not in [ 'K', 'Y', 'I', 'C'] ):
        print("Error: invalid input")
        return getInput()
    else:
        return result

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
    while (1):
        print("Enter the variable to be solved (K, Y, I, C)")
        process = getInput()
        params = getParams()
        if (process == "K"):
            result = solveK( params["labor"], params["productivity"], params["saveRate"], params["depreciationRate"] )
        if (process == "Y"):
            result = solveY( params["labor"], params["productivity"], params["saveRate"], params["depreciationRate"] )
        if (process == "I"):
            result = solveI( params["labor"], params["productivity"], params["saveRate"], params["depreciationRate"] )
        if (process == "C"):
            result = solveC( params["labor"], params["productivity"], params["saveRate"], params["depreciationRate"] )
        print( result )


def main():
    cli()

try:
    main()
except KeyboardInterrupt:
    print("")
    print("Have a nice day, ace that shit")
