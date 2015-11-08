#balance = 4842
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
#
#totalPaid = 0
#
#for month in range(1, 13):
#    monthlyInterestRate = (annualInterestRate / 12.0)
#    # minimumMonthlyPayment = (monthlyPaymentRate * balance)
#    monthlyUnpaidBalance = (balance - minimumMonthlyPayment)
#    balance = (monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance))
#    totalPaid += minimumMonthlyPayment
#    
#    print "Month: " + str(month)
#    print "Minimum monthly payment: " + "{:.2f}".format((minimumMonthlyPayment))
#    print ("Remaining balance: " + "{:.2f}".format(balance))
#
#print "Total paid: " + "{:.1f}".format(totalPaid)
#print "Remaining balance: " + "{:.1f}".format(balance)



balance = 999999
annualInterestRate = 0.18

def testPayment(monthlyPayment, balance):
    '''
    Accepts two figures, the monthly payment amount and the current balance
    It then tests 12 monthly payments against the annual interest rate (global)
    It turns the balance remaining as an int.
    '''
    for month in range(12):
        monthlyInterestRate = (annualInterestRate / 12.0)
        monthlyUnpaidBalance = (balance - monthlyPayment)
        balance = (monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance))
    return balance

low = (balance / 12)
high = balance * (1 + annualInterestRate/12.0)
epsilon = 0.01

monthlyPayment = (low + high) / 2.0

updatedBalance = testPayment(monthlyPayment, balance)

while abs(updatedBalance) >= epsilon: 
    if updatedBalance < 0:
        high = monthlyPayment
        monthlyPayment = (low + high) / 2.0
    else:
        low = monthlyPayment
        monthlyPayment = (low + high) / 2.0
    updatedBalance = testPayment(monthlyPayment, balance)
 
print "Lowest Payment: " + str("{:.2f}".format(monthlyPayment))