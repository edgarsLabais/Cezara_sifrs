alphabet =  'AĀBCČDEĒFGĢHIĪJKĶLĶMNŅOPQRSŠTUŪVWXYZ'
key = int(input("Uzrakstiet dešifrēšanas soli: "))
textToCode = str(input("Uzrakstiet, lai dešifrētu ziņojumu: ")).upper()
DecodedText = ''
for char in textToCode:
    place = alphabet.find(char)
    new_place = place - key
    if char in alphabet:
        DecodedText += alphabet[new_place]
    else:
        DecodedText += char
print(DecodedText)
