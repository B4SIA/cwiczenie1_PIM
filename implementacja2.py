def szyfruj_cezara(tekst: str, przesuniecie: int) -> str:
    przesuniecie = przesuniecie % 26
    wynik = []
    for znak in tekst:
        if "A" <= znak <= "Z":
            nowy_kod = (ord(znak) - ord("A") + przesuniecie) % 26 + ord("A")
            wynik.append(chr(nowy_kod))
        elif "a" <= znak <= "z":
            nowy_kod = (ord(znak) - ord("a") + przesuniecie) % 26 + ord("a")
            wynik.append(chr(nowy_kod))
        else:
            wynik.append(znak)
    return "".join(wynik)

if __name__ == "__main__":
    testy = [
        ("HELLO", 3),
        ("MERITO", 3),
    ]
    for tekst_wejsciowy, klucz in testy:
        zaszyfrowany = szyfruj_cezara(tekst_wejsciowy, klucz)
        print(f"Tekst: '{tekst_wejsciowy}' | Klucz: {klucz} -> Wynik: '{zaszyfrowany}'")