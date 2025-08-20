import json

def encode_string(encoded_string):
    encode_map = {
        'a': 'A',
        'e': 'A',
        'i': 'A',
        'o': 'A',
        'u': 'A',
        'b': 'B',
        'c': 'B',
        'd': 'B',
        'f': 'F',
        'g': 'F',
        'h': 'F',
        'j': 'J',
        'k': 'J',
        'l': 'J',
        'm': 'M',
        'n': 'M',
        'p': 'M',
        'q': 'Q',
        'r': 'Q',
        's': 'Q',
        't': 'T',
        'v': 'T',
        'w': 'T',
        'x': 'X',
        'y': 'X',
        'z': 'X',
    }
    encoded = []
    for char in encoded_string:
        if char.lower() in encode_map:
            encoded.append(encode_map[char.lower()])
        else:
            raise ValueError(f"Character '{char}' cannot be encoded.")
    return ''.join(encoded)

def decode_from_wordlist(encoded_words: set, wordlist_path: str) -> dict:
    """
    Decode encoded words using a provided wordlist.
    
    :param encoded_words: A set of encoded words to decode.
    :param wordlist_path: Path to the wordlist file.
    :return: A dictionary mapping encoded words to their original words.
    """
    decoded_words = {}
    
    try:
        with open(wordlist_path, 'r') as file:
            for line in file:
                word = line.strip()
                if word:  # Check if the line is not empty
                    try:
                        encoded_word = encode_string(word)
                        if encoded_word in encoded_words:
                            if encoded_word not in decoded_words:
                                decoded_words[encoded_word] = []
                            decoded_words[encoded_word].append(word)
                    except ValueError as e:
                        print(e)
    except FileNotFoundError:
        print(f"The file '{wordlist_path}' was not found.")
    
    return decoded_words

def decode_string(encoded_string, wordlist_paths, output_str):
    # Set of all unique words in the encoded strings
    words = set(encoded_string.split())

    for wordlist_path in wordlist_paths:
        print("=" * 40)
        print(f"Decoding using wordlist: {wordlist_path}")
        translated_words = decode_from_wordlist(words, wordlist_path)
        
        # Print the results for each wordlist
        print(f"Results from {wordlist_path}:")
        print("-" * 40)
        for encoded_word, original_words in translated_words.items():
            if original_words:
                print(f"{encoded_word}: {', '.join(original_words)}")
            else:
                print(f"{encoded_word}: No matching words found.")
        print("\n")

        # Store results in json file

        with open(f'decoded_results_{wordlist_path.split("_")[0]}_{output_str}.json', 'w') as json_file:
            json.dump(translated_words, json_file, indent=4)

def main():
    # Target encoded strings
    encoded_string_1 = "AFAJATX XM ATAQX QAX QABAMBQ"
    encoded_string_2 = "BAMT FAAJ AFAJATX ABQTABJAQ"
    encoded_string_3 = "BAAMQ FATAM AM AFAJATX JAM BAMMJATAAM"

    wordlist_paths = ['en_long_wordlist.txt']

    decode_string(encoded_string_1, wordlist_paths, "agility_left") 
    decode_string(encoded_string_2, wordlist_paths, "agility_right")
    decode_string(encoded_string_3, wordlist_paths, "agility_bottom")

    encoded_name = "FAJBAM FAATAB"
    decode_string(encoded_name, wordlist_paths, "agility_name")





if __name__ == "__main__":
    main()
