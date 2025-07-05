alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

# direction = input("Encode or Decode?\n").lower()
# text = input("Type your message\n").lower()
# shift = int(input("Type the shift number\n"))


# ##################################################################################################
#                                         encrypting text
# ##################################################################################################

# def encrypt(original_text, shift_amount):
#     # 3. creating an empty string to store the shifted letters
#     cipher_text = ""

#     # 1.looping each letter through the original_text
#     # let's say the original text is "hello"
#     # this will loop through each letters one by one
#     for letter in original_text:
#         # 2. we want to shift each letters' position
#         # first we have to get the letters' postion from the alphabet list (`alphabet.index(letter)`)
#         # then we'll shift the letters, let's say by 2
#         # so shifting `h` by 2 would be `j` and so on
#         # then we need to store these letters somewhere
#         # so shifte positiong for letter "h" would be :
#         # alphabet.index("h") which is at position 7 and then + shift amout, let's say 2 = 9 which is the letter "j"
#         shifted_position = alphabet.index(letter) + shift_amount
#         # NOTE : alphabet has 26 letters. so the length is 26
#         # but we know counting starts from 0 in programming so the index number for overal is 25
#         # so the overall number is 25
#         # now what happens when the shifted_position goes about 25?
#         # we have to get the remainings by using modulo `%`
#         # Example : lets say the user pick the letter "Z" and the shift number is "9"
#         # so the shifted posotion would be :
#         # alphabet.index(letter) + shift_amount :
#         # 25 + 9 = 34 which goes about the alphabet.
#         # so now we need to use modulo to get the remaining of 34
#         # so what we need to do is :
#         # shifted_position - len(alphabet) :
#         # alphabet length is : 26
#         # : 34 % 26 = 8 and then it'd start from the beginning = "i"
#         shifted_position %= len(alphabet)
#         # 4. storing the new letters
#         cipher_text += alphabet[shifted_position]
#     # 5. printing out the result
#     print(f"The encpryptd word is: {cipher_text}")


# encrypt(original_text=text, shift_amount=shift)


# # ##################################################################################################
#                                         decrypting text
# ##################################################################################################
# def decrypt(original_text, shift_amount):

#     decrypted_word = ""

#     for letter in original_text:
#         # in decpryption we are shifting backwards so we have to subtract the shift amout
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         decrypted_word += alphabet[shifted_position]

#     print(f"The decpryptd word is: {decrypted_word}")


# decrypt(original_text=text, shift_amount=shift)


# ###################################################################################################
# puttng these two functions inside one function
# ##################################################################################################


def ceasar(original_text, shift_amount, encode_or_decode):

    output = ""

    for letter in original_text:

        if letter not in alphabet:
            output += letter
        else:
            # most of the codes in both functions are basically the same
            # except this line
            # so how can we make it work of their cases? for both encrypting and decrypting?
            # I could use the if else statment
            # and say if the direction is "encode", then add up to the shift amount
            # and say if the direction is "decode", then subtract the shift amount
            if direction == "encode":
                shifted_position = alphabet.index(letter) + shift_amount
            else:
                shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            output += alphabet[shifted_position]

    print(f"The {encode_or_decode}d is: {output}")


# restarting the game
should_continue = True

while should_continue:

    direction = input("Encode or Decode?\n").lower()
    text = input("Type your message\n").lower()
    shift = int(input("Type the shift number\n"))

    ceasar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    start_over = input("Do you want to start over? Yes or No?\n").lower()
    if start_over == "no":
        should_continue = False
        print("Ending the game")
