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
            table_sum += player_choice
            player_turn = False
        else:
            print("Tura komputera:")
            # Komputer wybiera wartość żetonu (4, 5 lub 6)
            computer_choice = min(4, 5, 6, key=lambda x: minmax(table_sum + x, True))
            table_sum += computer_choice
            player_turn = True

        print("Gracz dołożył żeton o wartości:", player_choice if player_turn else computer_choice)

        # Sprawdź warunki końcowe gry
        if table_sum > 21:
            print("Suma na stole przekroczyła 21! Przegrywasz." if player_turn else "Suma na stole przekroczyła 21! Wygrywasz!")
            break
        elif table_sum == 21:
            print("Suma na stole wynosi dokładnie 21. Remis.")
            break

def minmax(table_sum, is_maximizing):
    if table_sum > 21:
        return -1 if is_maximizing else 1
    elif table_sum == 21:
        return 0

    if is_maximizing:
        best_value = float('-inf')
        for choice in [4, 5, 6]:
            value = minmax(table_sum + choice, False)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for choice in [4, 5, 6]:
            value = minmax(table_sum + choice, True)
            best_value = min(best_value, value)
        return best_value

# Rozpocznij grę
play_game()
