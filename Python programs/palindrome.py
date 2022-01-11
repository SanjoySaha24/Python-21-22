def pal(stringInp):
    inverted = stringInp[-1::-1]

    if stringInp == inverted:
        return True
    else:
        return False
