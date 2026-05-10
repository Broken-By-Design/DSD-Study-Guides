#collects and validates the Client_ID number
def get_check_client_ID ()
    
    valid = False

    while valid == False:
        clientID = input('Please enter the Client ID number: ')
        if len(clientID) > 10 :
            print('Client ID must be 10 characters long')

            valid = False
        else:
            print('Client ID accepted')
            
            return clientID
           
  
#collects and validates the investment amount
def get_check_investment_amount ():
    
    valid = False

    while valid == False:
        amount = input('Please enter the amount to be invested per year: £ ')
        try:
            float(amount)
        except:
            print('You did not enter an appropriate number format.')
            print('Please try again')
            valid = False
        else:
            print('Investment amount accepted')

            return amount


#collects and checks types of investment
def investment_type (investmentAmount):

    valid = False

    while valid == False:
        print('Please choose an investment type:')
        print('1. Savings plan')
        print('2. Managed stock investments')
        choice = input('Enter choice here: ')

        if choice == "1" and investmentAmount >= 20000:
            print('The amount you wish to invest is too high for the standard savings plan.')
            print('You will be shown an example for managed stock investments instead')   
            choice = 2
            return choice
        else:
            return choice
        


#add each year's investment and calculates the returns, fees and profits for the savings plan option
def savings_plan (investmentAmount):
    maximumValue = 0
    minimumValue = 0
    feesMax = 0
    feesMin = 0

    for i in range (1,5):

        maximumValue = maximumValue + investmentAmount
        maximumValue = maximumValue + (maximumValue * 0.024)


        minimumValue = minimumValue + investmentAmount
        minimumValue = minimumValue + (minimumValue * 0.012)


        feesMax = feesMax + (maximumValue * 0.0025)
        feesMin = feesMin + (minimumValue * 0.0025) 

    maxProfit = maximumValue - ((investmentAmount * 5) + feesMax)
    minProfit = minimumValue - ((investmentAmount * 5) + feesMin)

    print('****************************************')
    print('********* Savings plan summary *********')
    print('Initial Investment: £ {}'.format(investmentAmount))
    print('')
    print('If the savings plan performs at the highest rate after 5 years you can expect:')
    print('Value of investment: £ {:.2f}'.format(maximumValue))
    print('Fees paid: £ {:.2f}'.format(feesMax))
    print('Profit made: £ {:.2f}'.format(maxProfit))
    print('')
    print('If the savings plan performs at the lowest rate after 5 years you can expect:')
    print('Value of investment: £ {:.2f}'.format(minimumValue))
    print('Fees paid: £ {:.2f}'.format(feesMin))
    print('Profit made: £ {:.2f}'.format(minProfit))

#calculates the returns, fees and profits for the managed stocks investment plan option
def managed_stocks (investmentAmount):
    maximumValue = 0
    minimumValue = 0
    feesMax = 0
    feesMin = 0

    for i in range (0,5):

        maximumValue = maximumValue + investmentAmount
        maximumValue = maximumValue + (maximumValue * 0.23)


        minimumValue = minimumValue + investmentAmount
        minimumValue = minimumValue + (minimumValue * 0.40)


        feesMax = feesMax + (maximumValue * 0.013)
        feesMin = feesMin + (minimumValue * 0.013) 

    maxProfit = maximumValue - ((investmentAmount * 5) + feesMax)
    minProfit = minimumValue - ((investmentAmount * 5) + feesMin)

    print('****************************************')
    print('** Managed Stocks Investment Summary ***')
    print('Initial Investment: £ {}'.format(investmentAmount))
    print('')
    print('If the managed stocks plan performs at the highest rate after 5 years you can expect:')
    print('Value of investment: £ {}'.format(maximumValue))
    print('Fees paid: £ {}'.format(feesMax))
    print('Profit made: £ {}'.format(maxProfit))
    print('')
    print('If the managed stocks plan performs at the lowest rate after 5 years you can expect:')
    print('Value of investment: £ {}'.format(minimumValue))
    print('Fees paid: £ {}'.format(feesMin))
    print('Profit made: £ {}'.format(minProfit))




def main ():
    name = input('Please enter the name of the client: ')
    clientID = get_check_client_ID()
    investmentAmount = get_check_investment_amount() 
    investmentTypeChoice = investment_type (investmentAmount)
    print('********** Investment summary **********')
    print('Client name:', name)
    print('Client ID:', clientID)
    if investmentTypeChoice == "1":
        savings_plan(investmentAmount)
    else:
        managed_stocks(investmentAmount)

man()

