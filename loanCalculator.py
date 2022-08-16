# loan calculating program
print('XX'*70)
print(' ')
print('WELCOME TO LOAN CALCULATOR')
print(' ')
print('XX'*70)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# declaring variables (setting deafalut password and username)
yuza = "user1"
pasiwedi = "123456"
print(" ")
chances = 3
while chances >= 0 :
# prompting user to enter username and password
    print("Please provide your username and your password to log in to the system:")
    print("_________________________________________________________________________________________________________")
    username = input("Please enter your Username :\n")
    password = input("Please enter your Password :\n")
    print("_________________________________________________________________________________________________________")
    # validating the username and the password
    if username == yuza and password == pasiwedi:
        print("Login successful. Welcome Boss, please proceed with other transactions")
        print("--"*60)

        #get customer details
        customer_firstname = input("Please enter customer's first name :\n")
        customer_surname = input("Please enter customer's username :\n")
        print(":"*70)
        print("Below are work grades against salary ranges\nPlease enter customer's gross salary")
        print("________________________________________________________________________________")
        print("__________________________________")
        print("Work Grade  |\tSalary range\t |")
        print("__________________________________")
        print("H\t    |\t460001 - 550000\t |\nI\t    |\t400001 - 460000\t |\nJ\t    |\t350001 - 400000\t |\nK\t    |\t250001 - 350000\t |\nL\t    |\t170001 - 250000\t |\nM\t    |\t100000 - 170000\t |")
        print("________________________________________________________________________________")

        print(customer_firstname," ",customer_surname,", please enter your Salary :\n")
        cus_gross_pay = int(input())
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if cus_gross_pay >= 460001 and cus_gross_pay <= 550000:
            paye = 0.25
            taxable =  (cus_gross_pay - 100000)
            tax = taxable * paye
            net_salary = cus_gross_pay - tax
            # displaying customer details 
            print("________________________________________________________________________________________________")
            print("Here are customer and income details :\n")
            print("First Name :  ",customer_firstname,"\nSurname  :  ",customer_surname,"\nWork Grade:\tH")
            print("------------------------------------------------------------------------------------------------------")
            print("Your gross pay is : ",cus_gross_pay , "\nPay as you earn Tax is :",tax,"\nNet pay or take home salary is :", net_salary) 
            print("------------------------------------------------------------------------------------------------------")
            # processing the loan
            # Prompting customer whether he or she wants to get a loan
            print("Do you want to get loan?\n")
            want_loan = input("Press Y to access loan\nPress N or any key to quit program\n")
            print("")
            print("------------------------------------------------------------------------------------------------------")
            
            if want_loan == 'Y' or want_loan == 'y':
                needed_loan_amount = int(input("Enter the amount of loan you want to lend \n"))
                # checking laon amount. loan to get shoud not be more than salary times 7
                if needed_loan_amount < net_salary*7:
                    pay_back_months = int(input("Enter payback period in months :\n"))
                    # validating payback months , should be less than 48 mnths (less than 4 years)
                    if pay_back_months <= 48:
                        # calculating interest per month
                        
                        rate = 0.30  # 8 percent per month
                        service_fee = 550 # about 1 percent per month
                        minimum_take_home = 65873
                        interest = needed_loan_amount * pay_back_months/12 * rate
                        loan_amount = interest + service_fee + needed_loan_amount 
                        monthly_installment = loan_amount/pay_back_months
                        take_home = net_salary - monthly_installment

                        if take_home >= minimum_take_home:
                            # displsying loan details
                            print("Loan processing successful !!!!!!!!\nBelow are the details of the loan")
                            print("*"*30)
                            print("Here are customer and income details :\n")
                            print(customer_surname,"You have been granted a loan amounting to :  ",loan_amount)
                            print(" ")
                            print("Actual loan amount requested  : ",needed_loan_amount,"\n")
                            print("Monthly pay back Installment  : ",monthly_installment,"\n")
                            print("Take home pay after installment : ",take_home,"\n")
                            print("Pay back duration in months  : ",pay_back_months,"\n")
                            print("Total service fee for whole period  : ",service_fee,"\n")
                            print("Total interest for whole period  : ",interest,"\n")
                            print("Total loan amount is : ",loan_amount," to be paid in :",pay_back_months," months")
                            print("-------------------------------------------------------------------------------------------------------")
                            print("Thank you for choosing and trusting us. Please come back for other services. Safe journey!")
                            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%         GOOD DAY         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                        else:
                            print(".."*30)  
                            print(" ")  
                            print("Loan proccessing not successful !!!!\nThe customer is not eligible for loan requested")
                            print(customer_surname,"You have been denied loan for the following reasons")
                            print("The loan monthly installment for the loan you requested will cause your")
                            print("take home pay to be lower than the limit set aside by the government.")
                            print("Please try again with a lower amount")
                            print("  End  "*10)
                    else:
                        print("+"*30,"\nSorry, pay back months are higher than the maximum months set by the institution") 
                        print("***"*30)
                    
                else:
                    print(">"*30,"\nSorry, loan amount is four times higher than your salary. Its against company policy\n")  
                    print("Try again with a lower amaount\n")
                    print("*"*70)              
            else:
                print("***"*30)
                print("Thanks for visiting us. I hope next time you will get a loan !")
                print("   Good day   "*5)
            
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        elif cus_gross_pay >= 400001 and cus_gross_pay <= 460000:
            paye = 0.25
            taxable =  (cus_gross_pay - 100000)
            tax = taxable * paye
            net_salary = cus_gross_pay - tax
            # displaying customer details 
            print("________________________________________________________________________________________________")
            print("Here are customer and income details :\n")
            print("First Name :  ",customer_firstname,"\nFirst Name :  ",customer_surname,"\nWork Grade:\tI")
            print("------------------------------------------------------------------------------------------------------")
            print("Your gross pay is : ",cus_gross_pay , "\nPay as you earn Tax is :",tax,"\nNet pay or take home salary is :", net_salary) 
            print("------------------------------------------------------------------------------------------------------")
            # processing the loan
            want_loan = input("Do you want to get loan?\nEnter Y to access loan\nEnter N to quit program\n")

            if want_loan == 'Y' or want_loan == 'y':
                needed_loan_amount = int(input("Enter the amount of loan you want to lend \n"))
                
                if needed_loan_amount < net_salary*7:
                    pay_back_months = int(input("Enter payback period in months :\n"))
                    
                    if pay_back_months <= 48:
                        # calculating interest per month
                        
                        rate = 0.30  # 8 percent per month
                        service_fee = 550 # about 1 percent per month
                        minimum_take_home = 65873
                        interest = needed_loan_amount * pay_back_months/12 * rate
                        loan_amount = interest + service_fee + needed_loan_amount 
                        monthly_installment = loan_amount/pay_back_months
                        take_home = net_salary - monthly_installment

                        if take_home >= minimum_take_home:
                            # displsying loan details
                            print("Loan processing successful !!!!!!!!\nBelow are the details of the loan")
                            print("*"*30)
                            print("Here are customer and income details :\n")
                            print(customer_surname,"You have been granted a loan amounting to :  ",loan_amount)
                            print(" ")
                            print("Actual loan amount requested  : ",needed_loan_amount,"\n")
                            print("Monthly pay back Installment  : ",monthly_installment,"\n")
                            print("Take home pay after installment : ",take_home,"\n")
                            print("Pay back duration in months  : ",pay_back_months,"\n")
                            print("Total service fee for whole period  : ",service_fee,"\n")
                            print("Total interest for whole period  : ",interest,"\n")
                            print("Total loan amount is : ",loan_amount," to be paid in :",pay_back_months," months")
                            print("-------------------------------------------------------------------------------------------------------")
                            print("Thank you for choosing and trusting us. Please come back for other services. Safe journey!")
                            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%         GOOD DAY         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                        else:
                            print(".."*30)  
                            print(" ")  
                            print("Loan proccessing not successful !!!!\nThe customer is not eligible for loan requested")
                            print(customer_surname,"You have been denied loan for the following reasons")
                            print("The loan monthly installment for the loan you requested will cause your")
                            print("take home pay to be lower than the limit set aside by the government.")
                            print("Please try again with a lower amount")
                            print("  End  "*10)
                    else:
                        print("+"*30,"\nSorry, pay back months are higher than the maximum months set by the institution") 
                        print("***"*30)
                    
                else:
                    print(">"*30,"\nSorry, loan amount is four times higher than your salary. Its against company policy\n")  
                    print("Try again with a lower amaount\n")
                    print("*"*70)             
            else:
                print("***"*30)
                print("Thanks for visiting us. I hope next time you will get a loan !")
                print("   Good day   "*5)
        
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # defining and determining salary range    grade_H = 301989;    grade_I = 287531;    grade_J = 255763;    grade_K = 197876;    grade_L = 165112
        elif cus_gross_pay >= 350001 and cus_gross_pay <= 400000:
            paye = 0.25
            taxable =  (cus_gross_pay - 100000)
            tax = taxable * paye
            net_salary = cus_gross_pay - tax
            # displaying customer details 
            print("________________________________________________________________________________________________")
            print("Here are customer and income details :\n")
            print("First Name :  ",customer_firstname,"\nFirst Name :  ",customer_surname,"\nWork Grade:\tJ")
            print("------------------------------------------------------------------------------------------------------")
            print("Your gross pay is : ",cus_gross_pay , "\nPay as you earn Tax is :",tax,"\nNet pay or take home salary is :", net_salary) 
            print("------------------------------------------------------------------------------------------------------")
            # processing the loan
            want_loan = input("Do you want to get loan?\nEnter Y to access loan\nEnter N to quit program\n")

            if want_loan == 'Y' or want_loan == 'y':
                needed_loan_amount = int(input("Enter the amount of loan you want to lend \n"))
                
                if needed_loan_amount < net_salary*7:
                    pay_back_months = int(input("Enter payback period in months :\n"))
                    
                    if pay_back_months <= 48:
                        # calculating interest per month
                        
                        rate = 0.30  # 8 percent per month
                        service_fee = 550 # about 1 percent per month
                        minimum_take_home = 65873
                        interest = needed_loan_amount * pay_back_months/12 * rate
                        loan_amount = interest + service_fee + needed_loan_amount 
                        monthly_installment = loan_amount/pay_back_months
                        take_home = net_salary - monthly_installment

                        if take_home >= minimum_take_home:
                            # displsying loan details
                            print("Loan processing successful !!!!!!!!\nBelow are the details of the loan")
                            print("*"*50)
                            print("Here are customer and income details :\n")
                            print(customer_surname,"You have been granted a loan amounting to :  ",loan_amount)
                            print(" ")
                            print("Actual loan amount requested  : ",needed_loan_amount,"\n")
                            print("Monthly pay back Installment  : ",monthly_installment,"\n")
                            print("Take home pay after installment : ",take_home,"\n")
                            print("Pay back duration in months  : ",pay_back_months,"\n")
                            print("Total service fee for whole period  : ",service_fee,"\n")
                            print("Total interest for whole period  : ",interest,"\n")
                            print("Total loan amount is : ",loan_amount," to be paid in :",pay_back_months," months")
                            print("-------------------------------------------------------------------------------------------------------")
                            print("Thank you for choosing and trusting us. Please come back for other services. Safe journey!")
                            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%         GOOD DAY         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                        else:
                            print(".."*30)  
                            print(" ")  
                            print("Loan proccessing not successful !!!!\nThe customer is not eligible for loan requested")
                            print(customer_surname,"You have been denied loan for the following reasons")
                            print("The loan monthly installment for the loan you requested will cause your")
                            print("take home pay to be lower than the limit set aside by the government.")
                            print("Please try again with a lower amount")
                            print("  End  "*10)
                    else:
                        print("+"*30,"\nSorry, pay back months are higher than the maximum months set by the institution") 
                        print("***"*30)
                    
                else:
                    print(">"*30,"\nSorry, loan amount is four times higher than your salary. Its against company policy\n")  
                    print("Try again with a lower amaount\n")
                    print("*"*70)              
            else:
                print("***"*30)
                print("Thanks for visiting us. I hope next time you will get a loan !")
                print("   Good day   "*5)
        
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # defining and determining salary range    grade_H = 301989;    grade_I = 287531;    grade_J = 255763;    grade_K = 197876;    grade_L = 165112
        elif cus_gross_pay >= 250001 and cus_gross_pay <= 350000:
            paye = 0.25
            taxable =  (cus_gross_pay - 100000)
            tax = taxable * paye
            net_salary = cus_gross_pay - tax
            # displaying customer details 
            print("________________________________________________________________________________________________")
            print("Here are customer and income details :\n")
            print("First Name :  ",customer_firstname,"\nFirst Name :  ",customer_surname,"\nWork Grade:\tK")
            print("------------------------------------------------------------------------------------------------------")
            print("Your gross pay is : ",cus_gross_pay , "\nPay as you earn Tax is :",tax,"\nNet pay or take home salary is :", net_salary) 
            print("------------------------------------------------------------------------------------------------------")
            # processing the loan
            want_loan = input("Do you want to get loan?\nEnter Y to access loan\nEnter N to quit program\n")

            if want_loan == 'Y' or want_loan == 'y':
                needed_loan_amount = int(input("Enter the amount of loan you want to lend \n"))
                
                if needed_loan_amount < net_salary*7:
                    pay_back_months = int(input("Enter payback period in months :\n"))
                    
                    if pay_back_months <= 48:
                        # calculating interest per month
                        
                        rate = 0.30  # 8 percent per month
                        service_fee = 550 # about 1 percent per month
                        minimum_take_home = 65873
                        interest = needed_loan_amount * pay_back_months/12 * rate
                        loan_amount = interest + service_fee + needed_loan_amount 
                        monthly_installment = loan_amount/pay_back_months
                        take_home = net_salary - monthly_installment

                        if take_home >= minimum_take_home:
                            # displsying loan details
                            print("Loan processing successful !!!!!!!!\nBelow are the details of the loan")
                            print("*"*30)
                            print("Here are customer and income details :\n")
                            print(customer_surname,"You have been granted a loan amounting to :  ",loan_amount)
                            print(" ")
                            print("Actual loan amount requested  : ",needed_loan_amount,"\n")
                            print("Monthly pay back Installment  : ",monthly_installment,"\n")
                            print("Take home pay after installment : ",take_home,"\n")
                            print("Pay back duration in months  : ",pay_back_months,"\n")
                            print("Total service fee for whole period  : ",service_fee,"\n")
                            print("Total interest for whole period  : ",interest,"\n")
                            print("Total loan amount is : ",loan_amount," to be paid in :",pay_back_months," months")
                            print("-------------------------------------------------------------------------------------------------------")
                            print("Thank you for choosing and trusting us. Please come back for other services. Safe journey!")
                            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%         GOOD DAY         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                        else:
                            print(".."*30)  
                            print(" ")  
                            print("Loan proccessing not successful !!!!\nThe customer is not eligible for loan requested")
                            print(customer_surname,"You have been denied loan for the following reasons")
                            print("The loan monthly installment for the loan you requested will cause your")
                            print("take home pay to be lower than the limit set aside by the government.")
                            print("Please try again with a lower amount")
                            print("  End  "*10)
                    else:
                        print("+"*30,"\nSorry, pay back months are higher than the maximum months set by the institution") 
                        print("***"*30)
                    
                else:
                    print(">"*30,"\nSorry, loan amount is four times higher than your salary. Its against company policy\n")  
                    print("Try again with a lower amaount\n")
                    print("*"*70)              
            else:
                print("***"*30)
                print("Thanks for visiting us. I hope next time you will get a loan !")
                print("   Good day   "*5)
        
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        elif cus_gross_pay >= 170001 and cus_gross_pay <= 250000:
            paye = 0.25
            taxable =  (cus_gross_pay - 100000)
            tax = taxable * paye
            net_salary = cus_gross_pay - tax
            # displaying customer details 
            print("________________________________________________________________________________________________")
            print("Here are customer and income details :\n")
            print("First Name :  ",customer_firstname,"\nFirst Name :  ",customer_surname,"\nWork Grade:\tL")
            print("------------------------------------------------------------------------------------------------------")
            print("Your gross pay is : ",cus_gross_pay , "\nPay as you earn Tax is :",tax,"\nNet pay or take home salary is :", net_salary) 
            print("------------------------------------------------------------------------------------------------------")
            # processing the loan
            want_loan = input("Do you want to get loan?\nEnter Y to access loan\nEnter N to quit program\n")

            if want_loan == 'Y' or want_loan == 'y':
                needed_loan_amount = int(input("Enter the amount of loan you want to lend \n"))
                
                if needed_loan_amount < net_salary*7:
                    pay_back_months = int(input("Enter payback period in months :\n"))
                    
                    if pay_back_months <= 48:
                        # calculating interest per month
                        
                        rate = 0.30  # 8 percent per month
                        service_fee = 550 # about 1 percent per month
                        minimum_take_home = 65873
                        interest = needed_loan_amount * pay_back_months/12 * rate
                        loan_amount = interest + service_fee + needed_loan_amount 
                        monthly_installment = loan_amount/pay_back_months
                        take_home = net_salary - monthly_installment

                        if take_home >= minimum_take_home:
                            # displsying loan details
                            print("Loan processing successful !!!!!!!!\nBelow are the details of the loan")
                            print("*"*30)
                            print("Here are customer and income details :\n")
                            print(customer_surname,"You have been granted a loan amounting to :  ",loan_amount)
                            print(" ")
                            print("Actual loan amount requested  : ",needed_loan_amount,"\n")
                            print("Monthly pay back Installment  : ",monthly_installment,"\n")
                            print("Take home pay after installment : ",take_home,"\n")
                            print("Pay back duration in months  : ",pay_back_months,"\n")
                            print("Total service fee for whole period  : ",service_fee,"\n")
                            print("Total interest for whole period  : ",interest,"\n")
                            print("Total loan amount is : ",loan_amount," to be paid in :",pay_back_months," months")
                            print("-------------------------------------------------------------------------------------------------------")
                            print("Thank you for choosing and trusting us. Please come back for other services. Safe journey!")
                            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%         GOOD DAY         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                        else:
                            print(".."*30)  
                            print(" ")  
                            print("Loan proccessing not successful !!!!\nThe customer is not eligible for loan requested")
                            print(customer_surname,"You have been denied loan for the following reasons")
                            print("The loan monthly installment for the loan you requested will cause your")
                            print("take home pay to be lower than the limit set aside by the government.")
                            print("Please try again with a lower amount")
                            print("  End  "*10)
                    else:
                        print("+"*30,"\nSorry, pay back months are higher than the maximum months set by the institution") 
                        print("***"*30)
                    
                else:
                    print(">"*30,"\nSorry, loan amount is four times higher than your salary. Its against company policy\n")  
                    print("Try again with a lower amaount\n")
                    print("*"*70)              
            else:
                print("***"*30)
                print("Thanks for visiting us. I hope next time you will get a loan !")
                print("   Good day   "*5)
        
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        elif cus_gross_pay >= 100000 and cus_gross_pay <= 170000:
            paye = 0.25
            taxable =  (cus_gross_pay - 100000)
            tax = taxable * paye
            net_salary = cus_gross_pay - tax
            # displaying customer details 
            print("________________________________________________________________________________________________")
            print("Here are customer and income details :\n")
            print("First Name :  ",customer_firstname,"\nFirst Name :  ",customer_surname,"\nWork Grade:\tM")
            print("------------------------------------------------------------------------------------------------------")
            print("Your gross pay is : ",cus_gross_pay , "\nPay as you earn Tax is :",tax,"\nNet pay or take home salary is :", net_salary) 
            print("------------------------------------------------------------------------------------------------------")
            # @@@@@@@@@@@@@@@@@             processing the loan         @@@@@@@@@@@@@@@@
            want_loan = input("Do you want to get loan?\nEnter Y to access loan\nEnter N to quit program\n")
            # prompting the customer if he/she wants to get loan  
            if want_loan == 'Y' or want_loan == 'y':
                #  prompt user to enter  the amount of loan needed
                needed_loan_amount = int(input("Enter the amount of loan you want to lend \n"))
                
                if needed_loan_amount < net_salary*7:
                    pay_back_months = int(input("Enter payback period in months :\n"))
                    
                    if pay_back_months <= 48:
                        # calculating interest per month
                        
                        rate = 0.30  # 8 percent per month
                        service_fee = 550 # about 1 percent per month
                        minimum_take_home = 65873
                        interest = needed_loan_amount * pay_back_months/12 * rate
                        loan_amount = interest + service_fee + needed_loan_amount 
                        monthly_installment = loan_amount/pay_back_months
                        take_home = net_salary - monthly_installment

                        if take_home >= minimum_take_home:
                            # displsying loan details
                            print("Loan processing successful !!!!!!!!\nBelow are the details of the loan")
                            print("*"*30)
                            print("Here are customer and income details :\n")
                            print(customer_surname,"You have been granted a loan amounting to :  ",loan_amount)
                            print(" ")
                            print("Actual loan amount requested  : ",needed_loan_amount,"\n")
                            print("Monthly pay back Installment  : ",monthly_installment,"\n")
                            print("Take home pay after installment : ",take_home,"\n")
                            print("Pay back duration in months  : ",pay_back_months,"\n")
                            print("Total service fee for whole period  : ",service_fee,"\n")
                            print("Total interest for whole period  : ",interest,"\n")
                            print("Total loan amount is : ",loan_amount," to be paid in :",pay_back_months," months")
                            print("-------------------------------------------------------------------------------------------------------")
                            print("Thank you for choosing and trusting us. Please come back for other services. Safe journey!")
                            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%         GOOD DAY         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                        else:
                            print(".."*30)  
                            print(" ")  
                            print("Loan proccessing not successful !!!!\nThe customer is not eligible for loan requested")
                            print(customer_surname,"You have been denied loan for the following reasons")
                            print("The loan monthly installment for the loan you requested will cause your")
                            print("take home pay to be lower than the limit set aside by the government.")
                            print("Please try again with a lower amount")
                            print("  End  "*10)
                    else:
                        print("+"*30,"\nSorry, pay back months are higher than the maximum months set by the institution") 
                        print("***"*30)
                    
                else:
                    print(">"*30,"\nSorry, loan amount is four times higher than your salary. Its against company policy\n")  
                    print("Try again with a lower amaount\n")
                    print("*"*70)             
            else:
                print("***"*30)
                print("Thanks for visiting us. I hope next time you will get a loan !")
                print("   Good day   "*5)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        else:
            print("Salary out of range! Try again with correct salary range.") 

    elif username != yuza and password != pasiwedi: 
    
        chances -= 1
        print("Ooops! Sorry, wrong password or username! Please Try again")
        print(" ")

else:

    print("\nPassword trial beyond limit. You cannot access the system.\nPlease contact your administrator.")
    print("@@@@@   ???????   End of program   ????????   @@@@@")

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


###### ######################                @@@@@   End of program   @@@@@   ***************************************************************
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
