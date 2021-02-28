from sudoku import Sudoku
def main():
    print("-----------{ SUDOKU SOLVER }-----------\n(Voer AUB elke rij zo in: \"012345678\")\n") 
    #sudoku bord voordat er nummers zijn ingevoerd:

    board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    ]
    
    #sudoku bord zelf invoeren door je nummers in een lijst te zetten:

    rij0 =input("Voer hier het eerste rij in:  ")
    rij0String = str(rij0)
    rij0Map = map(int, rij0String)
    rij0List = list(rij0Map)
    board[0] = list(rij0List)

    rij1 =input("Voer hier het tweede rij in:  ")
    rij1String = str(rij1)
    rij1Map = map(int, rij1String)
    rij1List = list(rij1Map)
    board[1] = list(rij1List)

    rij2 =input("Voer hier het derde rij in:   ")
    rij2String = str(rij2)
    rij2Map = map(int, rij2String)
    rij2List = list(rij2Map)
    board[2] = list(rij2List)

    rij3 =input("Voer hier het vierde rij in:  ")
    rij3String = str(rij3)
    rij3Map = map(int, rij3String)
    rij3List = list(rij3Map)
    board[3] = list(rij3List)

    rij4 =input("Voer hier het vijfde rij in:  ")
    rij4String = str(rij4)
    rij4Map = map(int, rij4String)
    rij4List = list(rij4Map)
    board[4] = list(rij4List)

    rij5 =input("Voer hier het zesde rij in:   ")
    rij5String = str(rij5)
    rij5Map = map(int, rij5String)
    rij5List = list(rij5Map)
    board[5] = list(rij5List)

    rij6 =input("Voer hier het zevende rij in: ")
    rij6String = str(rij6)
    rij6Map = map(int, rij6String)
    rij6List = list(rij6Map)
    board[6] = list(rij6List)

    rij7 =input("Voer hier het achtste rij in: ")
    rij7String = str(rij7)
    rij7Map = map(int, rij7String)
    rij7List = list(rij7Map)
    board[7] = list(rij7List)

    rij8 =input("Voer hier het negende rij in: ")
    rij8String = str(rij8)
    rij8Map = map(int, rij8String)
    rij8List = list(rij8Map)
    board[8] = list(rij8List)

    #jou ingevoerde sudoku puzzel uitprinten met de sudoku library

    puzzle = Sudoku(3,3, board=board)
    print("Dit is jou puzzel:")
    print(puzzle)


    #dit begint de invoer process opnieuw als je niet zeker bent:
    zekerWeten = input("Weet je zeker dat je de sudoku goed hebt ingevoerd? (j/n) ").lower()
    if zekerWeten == "j":
        #de sudoku library gebruiken om de sudoku te solven
        solution = Sudoku(3,3, board=board).solve()
        print(solution)
    else:
        print("Probeer opnieuw:")
        main()
    #brengt je weer naar het invoer process als je opnieuw wilt beginnen
    opnieuw = input("Wil je opnieuw beginnen? (j/n)").lower()
    if opnieuw == "j":
        main()
    else:
        exit()

main()

