# cuantas vocales y cuantas consonantes tiene una palabra que ingresas
vowels = ("a","e","i","o","u")
consonants = ("b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","x","z","w","y")
countVowels = 0
countConsonants = 0

value = input("Enter some phrase: ")

for e in value:
    if e.lower() in vowels:
        countVowels = countVowels + 1
    if e.lower() in consonants:
        countConsonants = countConsonants + 1

print(f"The number of vowels in the string is: {countVowels}")
print(f"The number of consonants in the string is: {countConsonants}")
