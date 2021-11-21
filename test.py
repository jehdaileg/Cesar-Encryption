import random 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ecrypt(message, shift):

	value = ""

	for letter in message:
		position = alphabet.index(letter)

		new_position = position + shift 

		value += alphabet[new_position]

	print(value)



def decrypt(message, shift):

	value = ""

	for letter in message:
		position = alphabet.index(letter)

		new_position = position - shift

		value += alphabet[new_position]

	print(value)





should_continue = True 

while should_continue:

	direction = input("Code or decode ?").lower()

	message = input("Enter the concerned message").lower()

	shift = int(input("Enter the shift value for the codage or decodeage"))


	if direction == "decode":

		decrypt(message,shift)

	else:

		ecrypt(message,shift)

	choice = input("Do you want to play again ?").lower()

	if choice == "no":

		should_continue = False

		print("Bye")




