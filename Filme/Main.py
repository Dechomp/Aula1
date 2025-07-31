def main():
    idade = int (input(""))

    if idade >= 18:
        print("L")
    elif idade >=16:
        acomp = input("")

        if acomp == "Sim" or acomp == "S":
            print("L")
        else:
            print("N") 
    else:
        print("N")

    return 0
main()