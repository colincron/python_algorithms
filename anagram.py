def anagram(string1,string2):
    reversed = string1[::-1]
    if reversed == string2:
        return True
    else:
        return False