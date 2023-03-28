alphabet =  'AĀBCČDEĒFGĢHIĪJKĶLĶMNŅOPQRSŠTUŪVWXYZ'
key = int(input("Uzrakstiet šifrēšanas soli: "))
textToCode = str(input("Uzrakstiet, lai šifrētu ziņojumu: ")).upper()
CodedText = ''
for char in textToCode:
    place = alphabet.find(char)
    new_place = place + key
    if char in alphabet:
        CodedText += alphabet[new_place]
    else:
        CodedText += char
print(CodedText)
