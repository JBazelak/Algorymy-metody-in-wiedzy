import random

def play_game():
    table_sum = 0  # Aktualna suma na stole
    player_turn = True  # Zmienna określająca, czy teraz jest kolej gracza

    while True:
        print("Aktualna suma na stole:", table_sum)

        if player_turn:
            print("Tura gracza:")
            # Gracz wybiera wartość żetonu (4, 5 lub 6)
            player_choice = int(input("Wybierz wartość żetonu (4, 5 lub 6): "))
            while player_choice not in [4, 5, 6]:
                print("Niewłaściwy wybór! Wybierz wartość żetonu (4, 5 lub 6): ")
                player_choice = int(input("Wybierz wartość żetonu (4, 5 lub 6): "))
            table_sum += player_choice
            player_turn = False
        else:
            print("Tura komputera:")
            # Komputer wybiera wartość żetonu (4, 5 lub 6) losowo
            computer_choice = random.choice([4, 5, 6])
            table_sum += computer_choice
            print("Komputer dołożył żeton o wartości:", computer_choice)
            player_turn = True

        # Sprawdź warunki końcowe gry
        if table_sum > 21:
            print("Suma na stole przekroczyła 21! Przegrywasz." if player_turn else "Suma na stole przekroczyła 21! Wygrywasz!")
            break
        elif table_sum == 21:
            print("Suma na stole wynosi dokładnie 21. Remis.")
            break

# Rozpocznij grę
play_game()
