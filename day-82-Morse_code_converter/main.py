MORSE_CODE_DICT = {

    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',

    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',

    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',

    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',

    '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',

    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',

    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'

}


def encode_to_morse():
    morse_code = []
    for str_value in user_text:
        if str_value != ' ':
            morse_code.append(MORSE_CODE_DICT.get(str_value, ''))
        else:
            morse_code.append('/')

    return ' '.join(morse_code)


def morse_to_decode():
    text_code = []
    for char in encode_text:
        if char != ' ':
            text_code.append(MORSE_CODE_DICT.get('', char))
        else:
            text_code.append('')
    return ' '.join(text_code)


choice = int(input("Enter 1 to Encode and 2 to Decode: "))
if choice == 1:
    user_text = input("Enter your prompt: ").upper()
    our_morse_code = encode_to_morse()
    print(our_morse_code)

elif choice == 2:
    encode_text = input("Enter the code that need to be decoded: ")
    decode_to_text = morse_to_decode()
    print(decode_to_text)
