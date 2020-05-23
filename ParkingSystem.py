# Welcome to this coded pre-release!
# This has all the code and explains what each step is doing
# Hopefully this should be useful during exam prep
# Let's start!

# Import required libraries
# This is just python stuff to allow us to floor values and display decimals to 2.d.p
# I'll explain the floor function later
import math
from decimal import *

# Yeet they gonna keep iterating over this forever
# Let's just put a switch here so they can turn it off
keepOnGoing = True

while (keepOnGoing):
    # Set daily total to 0.
    dailyTotal = 0

    # Set a variable to keep track of whether the day has ended to false
    dayEnded = False

    # If the day has ended we will break out of this loop and stop accepting customers
    while (not dayEnded):

        # Inputting the day
        # I don't get why we don't set this at the start so I think the prerelease is a bit
        # annoying
        # Like the customers could just cheat and it wouldn't harm to put it outside the loop

        # Here we set up a bunch of variables that all depend on what day it is
        # This max hours one will track the maximum amount of hours a customer can stay before
        # 16:00 (4pm)
        maxHrs = 0

        # And this second one will track the price per hour for parking before 16:00
        hourPrice = 0
        
        while (True):
            print("Please input the current day.")
            # This day variable will track what day the customer has input
            day = input()
            # Checking if it's a weekday
            if (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday"):
                # The weekday rate is 10.00 per hour and a maximum of 2 hours before 16:00
                maxHrs = 2
                hourPrice = 10
                # The break statements breaks out of a loop that we are in
                # In this case its a while loop
                # Without a break statement this would go on forever and probably run into
                # memory overflow problems with the computer, and we don't want that
                # We break out of this loop as the customer has input a valid value, so we can move
                # on to the next question
                # One thing you may notice is that this breaks out of the most recent while
                # loop we've created, as this one is inside another while loop.
                # Don't believe me? Scroll up
                # This is the case for the defualt break, but if we wanted to break out of the
                # other one there are ways to do that too
                break
            # Checking if it's a saturday
            elif (day == "Saturday" or day == "saturday"):
                # The saturday rate is 3.00 per hour and a maximum of 4 hours before 16:00
                maxHrs = 4
                hourPrice = 3
                break
            # Checking if it's a sunday
            elif (day == "Sunday" or day == "sunday"):
                # The saturday rate is 2.00 per hour and a maximum of 8 hours before 16:00
                maxHrs = 8
                hourPrice = 2
                break
            # This makes the customer re-enter the value if they put in an answer we can't accept
            else:
                print("Entered day is invalid.")

        # Inputing the hour of arrival
        
        # Here we set up an arrival hour variable
        # This will track what hour the customer arrived
        arrivalHr = 0

        while (True):
            # The hour needs to be an integer so we specify that in the question
            print("Please input your hour of arrival. (int)")
            # Try-except statements are for error catching
            # This means that we run the code in the try part
            # If there is an error, we stop running the code and run the code in the except part
            # instead
            # In this case, the code will error out if we can't convert the customer's input to
            # an integer
            try:
                arrivalHr = int(input())
                # We need to check if the arrival hour is between the valid times a car is
                # allowed to park - between 8:00 and 24:00
                if (arrivalHr >= 8 and arrivalHr < 24):
                    break
                else:
                    print("Entered hour is invalid.")
            # If the code errors out, the customer hasn't put an integer in as the input value
            # Or something wrong with the computer happened
            # But we assume our pre-release computer is perfect
            # Therefore, we need to remind the customer to input an integer
            # If we didn't have this the program would crash and that would not be fun
            except:
                print("Entered value is not an integer.")

        # Inputing the number of hours to leave car

        # Here we set up a parking hours variable
        # This will track how many hours the customer will park
        parkingHrs = 0
        
        while (True):
            # Again, this needs to be an integer
            print("Please input the number of hours to leave your car. (int)")
            # We use the try-except statement again to catch if the customer doesn't input an
            # integer
            try:
                parkingHrs = int(input())
                # This logic is to check that the customer can actually park for the hours they
                # have put in
                # First, we check if the number of hours they want to park is greater than 0
                # I mean, you can't park for negative hours and parking for 0 would be
                # pointless
                if (parkingHrs > 0
                    # Next, we check whether they are exceeding the maximum hours they can park
                    # before 16:00
                    # This first case checks whether they are parking for less than the
                    # maximum hours in total
                    and (maxHrs - parkingHrs >= 0
                         # This second case checks whether they are parking for less than the
                         # maximum hours in the morning, and rolling over to the afternoon
                         or arrivalHr + maxHrs >= 16)
                    # Finally, we check that they aren't staying later than midnight
                    # We don't even have a 25:00 anyways so this should not be accepted
                    and arrivalHr + parkingHrs <= 24):
                    # If they put in a valid answer we break and move to the next question
                    break
                else:
                    # If they put an invalid answer we tell them to input a valid one
                    print("Entered number of hours is invalid.")
            # If they didn't put an integer we catch it again and make them redo the question
            except:
                print("Entered value is not an integer.")

        # Input whether frequent parking number exists

        # Here we set up a discount variable
        # This will track whether the customer avails of a discount or not
        discount = False
        
        while (True):
            # Ask if they have a frequent parking number
            print("Do you have a frequent parking number? (Y/N)")
            answer = input()
            if (answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes"):
                # If they do we ask them to input the number
                print("Please input your frequent parking number. (int)")
                # Try-except again to ensure the number is an integer
                try:
                    # I'm still not sure what modulo 11 checksum method we're using so we'll
                    # assume its derived from the normal one - ISBN-10
                    # The algorithm I'm using is as follows:
                    # Multiply the 1st digit by 5
                    # Then multiply the 2nd digit by 4
                    # The multiply the 3rd digit by 3
                    # Then multiply the 4nd digit by 2
                    # Then leave the 5th (check) digit alone
                    # The sum of all these calculated values should be divisible by 11
                    # Let's give some examples:
                    
                    # Correct frequent parking number example: 12343
                    # 1 * 5 = 5
                    # 2 * 4 = 8
                    # 3 * 3 = 9
                    # 4 * 2 = 8
                    # 3 * 1 = 3
                    # 5 + 8 + 9 + 8 + 3 = 33
                    # 33 / 11 = 3 r 0
                    
                    # Incorrect frequent parking number example: 42069
                    # 4 * 5 = 20
                    # 2 * 4 = 8
                    # 0 * 3 = 0
                    # 6 * 2 = 12
                    # 9 * 1 = 9
                    # 20 + 8 + 0 + 12 + 9 = 49
                    # 49 / 11 = 4 r 5

                    # As the last (check) digit may be 10, the character 'X' is used to
                    # represent 10

                    number = input()

                    # Check if the number only has 5 characters and error if it doesn't
                    if (not (len(number) == 5)):
                        print("Entered frequent parking number is invalid.")

                    # Grabbing the first 4 digits of the checksum
                    checkSum = number[:4]

                    # Grabbing the check digit to check if it needs conversion
                    checkDigit = number[4]

                    # If the check digit is X or x we need to convert it to 10
                    if (checkDigit == "X" or checkDigit == "x"):
                        checkDigit = "10"

                    # Checksum time!
                    if ((
                        # Multiplying the first digit by 5
                        int(checkSum[0]) * 5

                        # Mulitplying the second digit by 4
                        + int(checkSum[1]) * 4

                        # Multiplying the third digit by 3
                        + int(checkSum[2]) * 3

                        # Multiplying the fourth digit by 2
                        + int(checkSum[3]) * 2

                        # Adding the check digit
                        + int(checkDigit))

                        # Checking if it is divisible by 11 and if it is, setting the discount
                        # to be true
                        % 11 == 0):
                        discount = True

                        # Break to next question
                        break

                    # If checksum is invalid repeat asking if the customer has one
                    else:
                        print("Entered frequent parking number is invalid.")

                # If checksum isn't an integer then error out and repeat the question
                except:
                    print("Entered value is not an integer")

            # If they don't have a checksum just continue to the next question
            elif (answer == "N" or answer == "n" or answer == "No" or answer == "no"):
                break

            # If they failed a Yes or No question idk anymore
            else:
                print("Entered answer is invalid.")

        # Now we output the information from step 1
        print("Entered day is " + day + ".")
        print("Entered hour of arrival is " + str(arrivalHr) + ".")
        print("Entered number of parking hours is " + str(parkingHrs) + ".")
        if (discount):
            print("Discount has been applied.")

        else:
            print("No discount has been applied.")

        # We need to check if this information is correct
        while (True):
            print("Is this information correct? (Y/N)")
            
            # Again, collecting their input data
            answer = input()

            # If the information is correct then we move on to the next part
            if (answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes"):
                # Calculating total price
                
                # In step 1 we could just calculate as a whole but as step 3 asks to calculate
                # in parts so I'll just implement that already

                # We set the total price to be 0
                totalPrice = 0
                discountPrice = 0

                # Before 16:00, the prices are the rates for the day
                if (arrivalHr < 16):
                    # If they roll over past 16:00, we just calculate the price of parking
                    # before first
                    if (arrivalHr + parkingHrs > 16):
                        totalPrice += (16 - arrivalHr) * hourPrice

                    # Otherwise, we just calculate the total price
                    else:
                        totalPrice += parkingHrs * hourPrice

                # If they have a discount, it will be applied to the first section
                # This gives them 10% off
                if (discount):
                    discountPrice = totalPrice * 0.1
                    totalPrice = totalPrice * 0.9

                # After 16:00, the flat price is the same no matter what day it is
                # In my opinion this is a very VERY bad system unless the parking prices are in
                # Bitcoin or Gold.
                if (arrivalHr + parkingHrs > 16):

                    # Checking if they arrived before 16:00
                    # In this case we only add the price after 16:00 as the price they need to
                    # pay before is calculated above
                    if (arrivalHr < 16):
                        # If they have a discount we apply it here as well
                        # This gives them 50% off
                        if (discount):
                            totalPrice += 1
                            discountPrice += 1

                        # Else just pay the normal price of 2.00 flat
                        else:
                            totalPrice += 2

                    # Otherwise we just calculate the total price
                    # Same discount rules apply as above
                    else:
                        if (discount):
                            totalPrice += 1
                            discountPrice += 1
                            
                        else:
                            totalPrice += 2

                # Outputting the total price
                # We first have to round it to 2.d.p because thats how you list price
                totalPrice = round(Decimal(totalPrice), 2)
                if (discount):
                    print("Discounted amount: " + str(discountPrice) + ".")
                    
                print("Amount due: " + str(totalPrice) + ".")

                # Inputting amount paid
                # They don't get change because we're scammers

                while (True):
                    print("Please input the amount paid. (number)")

                    # We need the try-except here to catch errors if the input value is not a
                    # number
                    try:
                        # Setting this paid amount to the customer input
                        paidAmount = Decimal(input())

                        # Checking if the paid amount is less than 0 or has more than 2.d.p
                        # Money only comes to 2.d.p
                        if (paidAmount < 0 or paidAmount.as_tuple().exponent < -2):
                            print("Entered amount is invalid.")

                        # Also checking whether it meeds the total price or not
                        # I mean, we don't want to get scammed
                        # We only want to scam others
                        elif (paidAmount < totalPrice):
                            print("Paid amount is insufficient.")

                        # If it passes those tests then we accept the money and add it
                        else:
                            # Updating daily total (no change given)
                            dailyTotal += paidAmount

                            # A nice thank you message and then we break the loop to move onto
                            # the next customer
                            print("Thank you. Your transaction have been successfully processed.")
                            break

                    # Catching errors when the customer doesn't input a number
                    # Surely they would have learn't by now but it's still important
                    except:
                        print("Entered amount is not a number")

                # Checking if the day has ended
                # We could use a light sensor for this or at least have staff input it
                # Or track time using the computer but whatever
                # We're just trying to pass the test here

                while (True):
                    
                    # Unambiguous yes or no question
                    print("Has the day ended? (Y/N)")
                    answer = input()
                    if (answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes"):

                        # If the day has ended we set this variable to true
                        # This will break the outermost while loop and end the program
                        dayEnded = True
                        print("The day has ended.")

                        # Outputting the daily total
                        # 2.d.p cuz we good like that
                        # Hopefully we've made lots of cash money
                        dailyTotal = round(Decimal(dailyTotal), 2)
                        print("Daily total of payments is " + str(dailyTotal) + ".")

                        while (True):
                            print("Continue to next day? (Y/N)")
                            answer = input()

                            if (answer == "Y" or answer == "y" or answer == "Yes" or answer
                                == "yes"):
                                print("Continuing to next day...")
                                break

                            elif (answer == "N" or answer == "n" or answer == "No" or answer
                                  == "no"):

                                # F in chat
                                # Our program's gonna die
                                # It's ok it's just code
                                print("Ending program...")
                                keepOnGoing = False
                                break

                            # NGL if they got a Y/N question wrong at this point I'd disown
                            # them
                            else:
                                print("Entered answer is invalid")
                        
                        break
                    elif (answer == "N" or answer == "n" or answer == "No" or answer == "no"):
                        # If the day hasn't ended then we continue onto the next customer
                        print("Ready to process next customer.")
                        break
                    else:
                        print("Entered answer is invalid.")
                break

            # Ah, back to the while loop outside this while loop
            # If you remember, it's a yes or no question
            # If the customer's answer is no, we need them to reinput their information
            # So this breaks the loop and it will start over again
            elif (answer == "N" or answer == "n" or answer == "No" or answer == "no"):
                print("Please re-enter your information.")
                break

            # Ah, the last few lines of code
            else:
                print("Entered answer is invalid.")
        
# If you've got here, congradulations!
# This should be all the code you need to pass the prerelease
# Hopefully this has cleared some stuff up for you
# If you spot any errors please tell me
