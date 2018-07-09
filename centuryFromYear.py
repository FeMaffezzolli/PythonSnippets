def centuryFromYear(year):
    """ Given a year, return the century it is in. -> int """

    iter = year//100 + 1
    sec = 0
    
    for i in list(range(iter)):
        if (sec+100 >= year):    
            return i+1
        else:
            sec += 100
