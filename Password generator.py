Lowercase = "qwertyuioplkjhgfdsazxcvbnm"
Uppercase = "QWERTYUIOPLKJHGFDSAZXCVBNM"
Numbers = "1234567890"
Symbols = "!£$%^&*?:;,.<#>_@"

Allowed = Lowercase + Uppercase + Numbers + Symbols


def Confirm(Password):    #this is the code for input password confirmation
    try:
        Password_1 = input("Confirm Password: ")
        if Password == Password_1:
            print("Password Confirmed")
            print("Password is " + Password_1)
        else:
            raise ValueError
    except ValueError:
        print("Password Doesnt Match")
        return Confirm(Password)


def input_password(Allowed):      #this is the process for password inputting according to stipulations
        Pass = input("input Desired Password: ")
        if len(Pass) < 9:
           print("Password too short. \nPassword must be above 9 Characters")
           return input_password(Allowed)
        else:
            for i in Pass:
                if i not in Allowed:
                    print("Password contains Forbidden symbols. \nallowed symbols include: " + Symbols)
                    return input_password(Allowed) 
    
        Confirm(Pass) #this is a predefined code within a defined code
    

#Actual program starts here

Type = input("Do you want a random Password? ")
if Type.upper() == "NO":

    input_password(Allowed) #this was previously defined

if Type.upper() == "YES":     #code for random generation
    import random  #important                           #not that difficult though
    length = 9
    Pass = "".join(random.sample(Allowed,length))

    print("Your Password is " + Pass)