# First Project

DEBUG = 0

letters_to_morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
    'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}

morse_to_letters_dict = {value: key for key, value in letters_to_morse_dict.items()}


def print_dict(n: str, d: dict):
    print(f"{n} dictionary:")
    for i in d.items():
        print(i[0].lower(), i[1])
    print()


def encode():
    msg = input("Type here your message: ").upper()
    encoded_message = ""
    for i in msg:
        if i == " ":
            encoded_message += " "
        else:
            encoded_message += letters_to_morse_dict[i] + " "
            if DEBUG:
                print(i, letters_to_morse_dict[i])
    encoded_message = encoded_message[:-1]
    print(f"Your encoded message: {encoded_message}\n")


def decode():
    msg = input("Type here your message: ").upper().split(" ")
    while msg and msg[-1] in ("", " "):
        msg.pop()
    if DEBUG:
        print(msg)
    decoded_message = ""
    for i in msg:
        if i in ("", " "):
            decoded_message += " "
        else:
            decoded_message += morse_to_letters_dict[i].lower()
            if DEBUG:
                print(i, morse_to_letters_dict[i])
    print(f"Your decoded message: {decoded_message.capitalize()}\n")


def welcome_message():
    text = " Morse Code Converter "
    width = 50
    line = f"\n{text:-^{width}}\n"
    print(line)


def debug_message():
    text = " Debug mode is ON "
    width = 50
    line = f"\n{text:-^{width}}\n"
    print(line)


welcome_message()
if DEBUG:
    debug_message()
    print_dict("letters to morse", letters_to_morse_dict)
    print_dict("morse to letters", morse_to_letters_dict)
    debug_message()

while True:
    mode = input("Do you want to 'encode'(1), or 'decode'(2) the message?"
                 "\nYou can also type 'exit'(0) to close the program: ").lower()
    match mode:
        case "encode" | "1":
            encode()
        case "decode" | "2":
            decode()
        case "exit" | "0":
            break
        case _:
            print("Unknown command, restarting program...\n\n")
