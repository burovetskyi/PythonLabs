def encoder (text ,key):
    encryptedText = ''
    for i in range(len(text)):
            encryptedText += str(chr(ord(text[i]) + int(key)))
    return encryptedText

def decoder (text,key):
    decodedText = ''
    for i in range(len(text)):
        decodedText += str(chr(ord(text[i]) - int(key)))
    return decodedText

text = 'Привіт. Сьогодні чудовий день для нападу на галлів'
key = 8
encryptedText = encoder(text, key)
print('encrypted text:\t', encryptedText)
print('decoded text:\t',decoder(encryptedText, key))
