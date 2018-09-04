import sys

_exit0 = "EXIT code:[0]"
_exit1 = "EXIT code:[1]"

def EXIT_no_input():
    #no string entered by user
    print u"\u001b[31m"+_exit0+u"\u001b[0m"
    print ">> Invalid input"
    print "\tError information: Enter key was pressed(No input)"
    return sys.exit("sys.exit executed")

def EXIT_wrong_input():
    #wrong string entered by user when choice of tags given
    print u"\u001b[31m"+_exit1+u"\u001b[0m"
    print ">> Invalid input"
    print "\tError information: Please enter the char in box[]."
    return sys.exit("sys.exit executed")

def EXIT_invalid_url():
    print "Entered invalid url"
    return sys.exit()
