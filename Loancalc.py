def myloan():
    prin = float(input('Loan Amount: '))
    intrate = float(input('Interest %: '))/100
    periodsYear = 12
    years = float(input('Years: '))
    mthly = (prin*intrate)/(periodsYear*(1-(1+(intrate/periodsYear))**(-1*years*periodsYear)))
    mthly = round(mthly,2)
    print('$', mthly)
myloan()
print('Program complete')
