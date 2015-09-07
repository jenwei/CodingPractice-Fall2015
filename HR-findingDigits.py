def  findingDigits( foo):
    """ findingDigits takes foo, an int array, and for each int, prints count, 
    the number of digits in the int that int can be divided by (with remainder 0), 
    where duplicate numbers count twice (i.e. 22 will have a count of 2), 
    and zeros don't count (i.e. 10 has a count of 1) """

    """ this solution has not been optimized yet """
    digits = []
    for f in foo:
        count = 0
        a = []
        ints = str(f)
        a+=ints
        for digit in a:
            digit = int(digit)
            if digit > 0:
                if (f % digit == 0):
                    count += 1
        print count
    return digits