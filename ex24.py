
def check_voewls(letter):
    vowels_list = [ "a", "e", "i", "o", "u" ]
    for vowel in vowels_list:
        if vowel == letter:
            return True
    return False

print("a", check_voewls("a"))
print("b", check_voewls("b"))
