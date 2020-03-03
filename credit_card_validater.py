#This is a python script that was created by Malvern Shaurwa
#The script checks if a credit card or debit card is valid using Luhn Algorithm

def creditcard():
    creditCardNum = input("Enter the credit card ")
    listCreditCardNum=list(creditCardNum) #Converting input from creditCardNum string into a list

    calculatedValue=[] #This is an array variable that store the calculated value
    firstStorageVar =0 #Interger verify number>10

    sumAllCreditNumbers =0 #variable will store the sum of all digits which are found in credit card

    if len(listCreditCardNum) !=16:  #here we are validating the length of the credit card
        print("This is not a valid credit card number")
        quit()

    else:
        for countVarible in range(len(listCreditCardNum)):
            if((countVarible%2)==0): #for loop for even number
                secondStorageVar=int((listCreditCardNum[countVarible]))*2 #Multiply number by 2

                if(secondStorageVar>=10):
                    firstStorageVar=secondStorageVar%10+1 #if value in the secondStorageVar>10, do mod 10 which help split num

                    calculatedValue.append(firstStorageVar)
                else:
                    calculatedValue.append(secondStorageVar)
            else:

                calculatedValue.append(int(listCreditCardNum[countVarible]))

    print("The credit card number you have entered in a list", listCreditCardNum)
    print("The converted credit card number list", calculatedValue)
    for newCountVariable in range(len(calculatedValue)):
        sumAllCreditNumbers=sumAllCreditNumbers+calculatedValue[newCountVariable]
    if(sumAllCreditNumbers%10 == 0):
        print("This credit card number is valid")
        return("This credit card number is valid")
    else:
        print("This credit card number is invalid")
        return("This credit card number is invalid")

creditcard()

# credit card 4137894711755904 = valid credit card
# credit card 6499802450273568 = invalid credit card
# credit card 8504172191273888 = valid credit card
# credit card 0043668783485480 = invalid credit card
