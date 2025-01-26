def calculator():
    print("Willkommen beim Taschenrechner!")
    print("Wählen Sie eine der folgenden Operationen:")
    print("1. Addition (+)")
    print("2. Subtraktion (-)")
    print("3. Multiplikation (*)")
    print("4. Division (/)")

    
    operation = input("Geben Sie die Nummer oder das Symbol der Operation ein, du netter Mensch: ")

    if operation in ['1', '+', '2', '-', '3', '*', '4', '/']:
        try:
            num1 = float(input("Geben Sie die erste Zahl ein: "))
            num2 = float(input("Geben Sie die zweite Zahl ein: "))

            if operation in ['1', '+']:
                result = num1 + num2
                print(f"Ergebnis: {num1} + {num2} = {result}")
            elif operation in ['2', '-']:
                result = num1 - num2
                print(f"Ergebnis: {num1} - {num2} = {result}")
            elif operation in ['3', '*']:
                result = num1 * num2
                print(f"Ergebnis: {num1} * {num2} = {result}")
            elif operation in ['4', '/']:
                if num2 != 0:
                    result = num1 / num2
                    print(f"Ergebnis: {num1} / {num2} = {result}")
                else:
                    print("Fehler: Division durch Null ist nicht möglich du Affe.")
        except ValueError:
            print("Fehler: Bitte gib gültige Zahlen ein.")
    else:
        print("Ungültige Operation. Versuche es erneut.")


calculator()
