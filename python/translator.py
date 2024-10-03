import sys  # Import sys module

# Define Braille mappings
BRAILLE_ALPHABET = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', '0': '.O.OOO', '1': 'O.....', '2': 'O.O...',
    '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..',
    '8': 'O.OO..', '9': '.OO...'
} 

# Reverse mappings
ENGLISH_ALPHABET = {value: key for key, value in BRAILLE_ALPHABET.items()}

def is_braille(input_string):
    """Check Braille format."""
    return all(char in "O." for char in input_string)  # Validate characters

def translate_to_braille(input_string):
    """Translate to Braille."""
    output = []
    number_mode = False  # Track if we are in number mode

    for char in input_string:
        if char.isdigit() and not number_mode:
            output.append(BRAILLE_ALPHABET['0'])  # Number follows symbol
            number_mode = True  # Switch to number mode

        if char.isdigit():
            output.append(BRAILLE_ALPHABET[char])  # Append Braille for number
        elif char == ' ':
            output.append(BRAILLE_ALPHABET[' '])  # Add space
            number_mode = False  # Reset number mode on space
        elif char.lower() in BRAILLE_ALPHABET:
            output.append(BRAILLE_ALPHABET[char.lower()])  # Append Braille for letters
            number_mode = False  # Reset number mode for letters
        else:
            raise ValueError(f"Character '{char}' cannot be translated.")

    return ''.join(output)


def translate_to_english(input_string):
    """Translate Braille text."""
    output = []  # Initialize output list
    # Split input string
    for i in range(0, len(input_string), 6):
        braille_char = input_string[i:i+6]  # Get Braille chunk
        if braille_char in ENGLISH_ALPHABET:
            output.append(ENGLISH_ALPHABET[braille_char])  # Append English
        else:
            raise ValueError(f"Braille '{braille_char}' cannot be translated.")  # Raise error
    return ''.join(output)  # Join to string

def main():
    # Check arguments
    if len(sys.argv) != 2:
        print("Usage: python3 translator.py <string>")
        sys.exit(1)  # Exit program

    input_string = sys.argv[1]  # Get input string

    # Determine translation direction
    if is_braille(input_string):
        translated_string = translate_to_english(input_string)  # Translate Braille
    else:
        translated_string = translate_to_braille(input_string)  # Translate English

    print(translated_string)  # Print result

if __name__ == '__main__':
    main()
