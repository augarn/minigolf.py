consonants = [ "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X", "Z"]
new_sentence = ""
def main():
    global new_sentence
    sentence = input("Skriv in din mening med stora bokstäver ")
    for i in sentence:
        if i in consonants:
            new_sentence += i + str("O") + i
        else:
            new_sentence += i
    print(new_sentence)
main()