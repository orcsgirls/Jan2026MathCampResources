### Luhn Algorithm ###
# this python program implements the Luhn algorithm for credit card number error detection.

cardNumber = "1234367890223456" # <--- you can change this :)

sumOfDigits = 0
doubledNumbers = []

# loop through every other digit in the card number
for i in range(0, 8):	
	# double it, save as a string to doubledNumbers
	doubledNumbers.append(str(2 * int(cardNumber[2*i+1])))
	# add the other digits of the number to sumOfDigits
	sumOfDigits += int(cardNumber[2*i])

# add the digits of each doubled number to sumOfDigits
for n in doubledNumbers:
		for x in n:
			sumOfDigits += int(x)
	
# check if sumOfDigits mod 10 = 0 to determine if the card number is valid
print(str(sumOfDigits) + " is " + ("divisible by 10" if sumOfDigits % 10 == 0 else "not divisible by 10") + " so it " + ("might be valid" if sumOfDigits % 10 == 0 else "is invalid"))
