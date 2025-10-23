while(True):
    x = input("Podaj liczbe:")
    if(x == "stop"):
         break
    try:
        x=float(x)
        print("x=", x,"x^3=", pow(x, 3))
    except ValueError:  
        print("niepoprawne dane")
