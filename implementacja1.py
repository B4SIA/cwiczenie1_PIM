def znajdz_wzorzec(tekst: str, wzorzec: str) -> list[int]:
    if not wzorzec or len(wzorzec) > len(tekst):
        return []
    wyniki = []
    granica = len(tekst) - len(wzorzec)
    for i in range(granica + 1):
        dopasowanie = True
        for j in range(len(wzorzec)):
            if tekst[i + j] != wzorzec[j]:
                dopasowanie = False
                break
        if dopasowanie:
            wyniki.append(i)
    return wyniki

def pokaz_dopasowania(tekst: str, wzorzec: str) -> None:
    pozycje = znajdz_wzorzec(tekst, wzorzec)
    znaczniki = ["^" if i in pozycje else " " for i in range(len(tekst))]
    print(f"Wzorzec: {wzorzec}")
    print(f"Tekst:   {tekst}")
    print(f"Znaki:   {''.join(znaczniki)}")
    if pozycje:
        print(f"Znaleziono na indeksach: {pozycje}\n")
    else:
        print("Nie znaleziono wzorca.\n")

testy = [
    ("She sells sea shells by the sea shore", "sea shells"),
    ("A quick brown fox jumped over a lazy dog", "fox"),
    ("Yesterday all my troubles seemed so far away", "away"),
    ("Abra cabra cadabra", "Cabra"),
    ("The internet connects millions of devices worldwide", "thousands"),
]

for tekst_testowy, wzorzec_testowy in testy:
    pokaz_dopasowania(tekst_testowy, wzorzec_testowy)