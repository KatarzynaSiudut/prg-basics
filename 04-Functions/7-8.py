def f(amount_to_pay):
    moneta_5 = amount_to_pay // 5
    reszta = amount_to_pay % 5

    moneta_2 = reszta // 2
    moneta_1 = reszta % 2
    return moneta_5 + moneta_2 + moneta_1

amount = 23
wynik = f(23)
print(f"{wynik}")














