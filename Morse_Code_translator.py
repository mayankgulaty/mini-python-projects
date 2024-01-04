class Solution:

    def run(self, morseToEnglish, textToTranslate):
        # Morse code dictionary
        morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',

            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.',

            '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
            '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
            '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
        }

        # Inverse dictionary for Morse-to-English
        inv_morse_dict = {v: k for k, v in morse_dict.items()}

        if morseToEnglish:
            # Morse-to-English translation
            try:
                words = textToTranslate.split('   ')
                translatedText = ''
                for word in words:
                    for symbol in word.split():
                        translatedText += inv_morse_dict.get(symbol, 'Invalid Morse Code Or Spacing')
                    translatedText += ' '
                return translatedText.strip()
            except KeyError:
                return 'Invalid Morse Code Or Spacing'
        else:
            # English-to-Morse translation
            translatedText = ''
            for char in textToTranslate.upper():
                if char == ' ':
                    translatedText += '   '  # Space between words
                else:
                    translatedText += morse_dict.get(char, 'Invalid Morse Code Or Spacing') + ' '
            return translatedText.strip()

# Example usage
solution = Solution()
translated_text = solution.run(False, "The wizard quickly jinxed the gnomes before they vaporized.")
print(translated_text)
