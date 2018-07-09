def checkPalindrome(inputString):
    """ Given any string, check if it is a palindrome. -> boolean """
    
    stringLen = len(inputString)
    if (stringLen == 1):
        return True
    l = stringLen//2
    for i in list(range(l)):    
        if (inputString[i] == inputString[-i-1]):
            pass
        else:
            return False
    return True
    
