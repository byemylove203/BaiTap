def Diachi(string):
    try:
        x= string.split(",")
        return x[0] + x[1]
    except:
        print("")
    return "Unknown"

def Quan(string):
    try:
        x= string.split(",")
        return x[2]
    except:
        print("")
    return "Unknown"

def Tinhthanh(string):
    try:
        x= string.split(",")
        return x[3]
    except:
        print("")
    return "Unknown"