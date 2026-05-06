EncryptOrDecrypt = (input("Encrypt or Decrypt? ").lower())

key = {
    "a": "¢",
    "b": "z12",
    "c": "π9",
    "d": "4^",
    "e": "†1",
    "f": "ºº",
    "g": "8$#",
    "h": "•¶",
    "i": "m≤",
    "j": "¬L",
    "k": "3&",
    "l": "łí",
    "m": "ª¡",
    "n": "pp",
    "o": "øƒ",
    "p": "√≈",
    "q": "][",
    "r": "{'",
    "s": "∆",
    "t": "!@",
    "u": "«}",
    "v": "#%",
    "w": "..",
    "x": "∑",
    "y": "L0",
    "z": "WD",
}

if EncryptOrDecrypt == "encrypt":
    print("Encrypting protocol initiated.")
    InputText = input("What would you like to encrypt?\n").lower()
    words = InputText.split(" ")
    encrypted_sentence = []
    for word in words:
        coded_letters = []
        for char in word:
            if char in key:
                coded_letters.append(key[char])
            else:
                coded_letters.append(char)

        encrypted_sentence.append(" ".join(coded_letters))

    final_code = " | ".join(encrypted_sentence)

    print("\n--- ENCRYPTED MESSAGE ---")
    print(final_code)




elif EncryptOrDecrypt == "decrypt":
    print("Decrypting protocol initiated.")
    reverse_key = {v: k for k, v in key.items()}

    if EncryptOrDecrypt == "decrypt":
        print("Decrypting protocol initiated.")
        InputCode = input("Paste the code to decrypt:\n")

        coded_words = InputCode.split(" | ")
        decoded_sentence = []

        for word in coded_words:
            symbols = word.split(" ")

            decoded_word = ""
            for s in symbols:
                if s in reverse_key:
                    decoded_word += reverse_key[s]
                else:
                    decoded_word += s

            decoded_sentence.append(decoded_word)

        final_message = " ".join(decoded_sentence)

        print("\n--- DECRYPTED MESSAGE ---")
        print(final_message)
