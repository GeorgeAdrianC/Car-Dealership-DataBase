def is_isogram(string):
    for letter in string:
        if letter == letter:
            print("Is not isogram")
        else:
            print("Is isogram")
            
a = "abcdefg"
b = "avac"

is_isogram(a)
is_isogram(b)
