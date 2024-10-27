import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, mode):
    output = ""
    if mode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output += alphabet[shifted_position]

    print(f"Here is the {mode}d result: {output}")

continue_again = "yes"

while continue_again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, mode=direction)
    continue_again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if continue_again == "no":
        print("Shutting Down.")


