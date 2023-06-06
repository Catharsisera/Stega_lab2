ArrayBinaryCode = ["11000", "10011", "01110", "10010", "10000", "10110", "01011", "00101", "01100",
                 "11010", "11110", "01001", "00111", "00110", "00011", "01101", "11101", "01010",
                 "10100", "00001", "11100", "01111", "11001", "10111", "10101", "10001"]

BigArrayLatinLet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

SmallArrayLatinLet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

BigArrayRusLet = ['А', 'Б', 'Ц', 'Д', 'Е', 'Ф', 'Г', 'Х', 'И', 'Й', 'К', 'Л', 'М',
                  'Н', 'О', 'П', 'Я', 'Р', 'С', 'Т', 'У', 'Ж', 'В', 'Ь',  'Ы', 'З']

SmallArrayRusLet = ['а', 'б', 'ц', 'д', 'е', 'ф', 'г', 'х', 'и', 'й', 'к', 'л', 'м',
                   'н', 'о', 'п', 'я', 'р', 'с', 'т', 'у', 'ж', 'в', 'ь',  'ы', 'з']

BigArraySpecialSymb = ['-', '?', ':', '', '3', 'Э', 'Ш', 'Щ', '8', 'Ю', '(', ')', '.', ',',
                  '9', '0', '1', '4', '\'', '5', '7', '=', '2', '/', '6', '+']

SmallArraySpecialSymb = ['-', '?', ':', '', '3', 'э', 'ш', 'щ', '8', 'ю', '(', ')', '.', ',',
                   '9', '0', '1', '4', '\'', '5', '7', '=', '2', '/', '6', '+']

ArrayChoiceBinaryCode = ["11111", "00000", "11011", "00100", "00010", "01000"]

def Encode(text):
    ArrBytes = ""
    symb = 0

    for i in range(len(text)):
        if (text[i] in BigArrayLatinLet or text[i] in SmallArrayLatinLet) and symb != 0:
            symb = 0
            ArrBytes += ArrayChoiceBinaryCode[0]
        elif (text[i] in BigArrayRusLet or text[i] in SmallArrayRusLet) and symb != 1:
            symb = 1
            ArrBytes += ArrayChoiceBinaryCode[1]
        elif (text[i] in BigArraySpecialSymb or text[i] in SmallArraySpecialSymb) and symb != 2:
            symb = 2
            ArrBytes += ArrayChoiceBinaryCode[2]
        elif text[i] == ' ':
            ArrBytes += ArrayChoiceBinaryCode[3]
        elif text[i] == '\r':
            ArrBytes += ArrayChoiceBinaryCode[4]
        elif text[i] == '\n':
            ArrBytes += ArrayChoiceBinaryCode[5]

        if symb == 0:
            for j in range(len(BigArrayLatinLet)):
                if text[i] == BigArrayLatinLet[j] or text[i] == SmallArrayLatinLet[j]:
                    ArrBytes += ArrayBinaryCode[j]
        elif symb == 1:
            for j in range(len(BigArrayRusLet)):
                if text[i] == BigArrayRusLet[j] or text[i] == SmallArrayRusLet[j]:
                    ArrBytes += ArrayBinaryCode[j]
        elif symb == 2:
            for j in range(len(BigArraySpecialSymb)):
                if text[i] == BigArraySpecialSymb[j] or text[i] == SmallArraySpecialSymb[j]:
                    ArrBytes += ArrayBinaryCode[j]

    return ArrBytes

def Decode(ArrBytes):
    text = ""
    symb = 0

    while len(ArrBytes) % 5 != 0:
        ArrBytes += ' '
    for i in range(0, len(ArrBytes), 5):
        ArrBytesAfterDivis = ArrBytes[i:i + 5]
        # print(ArrBytesAfterDivis)
        if ArrBytesAfterDivis == ArrayChoiceBinaryCode[0]:
            symb = 0
        elif ArrBytesAfterDivis == ArrayChoiceBinaryCode[1]:
            symb = 1
        elif ArrBytesAfterDivis == ArrayChoiceBinaryCode[2]:
            symb = 2
        elif ArrBytesAfterDivis == ArrayChoiceBinaryCode[3]:
            text += ' '
        elif ArrBytesAfterDivis == ArrayChoiceBinaryCode[4]:
            text += '\r'
        elif ArrBytesAfterDivis == ArrayChoiceBinaryCode[5]:
            text += '\n'
        else:
            for i in range(len(ArrayBinaryCode)):
                if ArrBytesAfterDivis == ArrayBinaryCode[i]:
                    if symb == 0:
                       text += BigArrayLatinLet[i]
                    elif symb == 1:
                        text += BigArrayRusLet[i]
                    elif symb == 2:
                        text += BigArraySpecialSymb[i]
    return text

# text = "My boy с номером 88"
# text = "1 k"
# print(text)
# print(Encode(text))
# print(Decode(Encode(text)))