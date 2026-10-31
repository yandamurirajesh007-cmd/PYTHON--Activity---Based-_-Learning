texts = ["aaabbbcccd", "abcd", "aaaaaaaaaa", "aabbaa", ""]

for text in texts:
    if len(text) == 0:
        print("Empty string - nothing to encode\n")
    else:
        encoded = ""
        count = 1
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                count = count + 1
            else:
                encoded = encoded + text[i - 1] + str(count)
                count = 1
        encoded = encoded + text[len(text) - 1] + str(count)

        print("Original :", text, "(length", len(text), ")")
        print("Encoded  :", encoded, "(length", len(encoded), ")")
        if len(encoded) < len(text):
            print("Result   : Compression is beneficial")
        else:
            print("Result   : Encoding NOT beneficial, keep original")
        print()
