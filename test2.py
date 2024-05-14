import random

def generuj_random_prvky():
    delka = random.randint(1, 15)
    return [random.randint (1, 100) for _ in range(delka)]

pocet_kol = 5

for i in range(pocet_kol):
    prvek = generuj_random_prvky()
    print(f"zadej prvky pole {i+1}: {prvek}")

    uzivatel_input = input("vaše odpověd: ")
    uzivatel_answer = list(map(int, uzivatel_input.split()))

    if uzivatel_answer == prvek:
        print("Správně")
    else:
        print("špatně")
