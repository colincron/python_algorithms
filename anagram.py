def anagram(string1,string2):
    reversed = string1[::-1]  # don't use this python magic
    if reversed == string2:
        return True
    else:
        return False