import random as rd

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 10 , 10, 10]

# Td : (Bet in chips)
# Better Terminal graphical display
''' Score displayer and high score 
def save_score(score, filename="scores.txt"):
    """Saves the current score to a file.
    """
    try:
        with open(filename, 'r') as file:
            best_score = int(file.readline())
    except FileNotFoundError:
        best_score = 0
    except ValueError:
      best_score = 0

    if score > best_score:
        best_score = score

    with open(filename, 'w') as file:
        file.write(str(best_score))

def load_score(filename="scores.txt"):
    """Loads the best score from a file.
    """
    try:
        with open(filename, 'r') as file:
            return int(file.readline())
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0
'''

def bet(starting_amount):
    
    bet_amount = 0
    
    while True:
        
        current_bet = input(f"How much do you want to bet? \nYou have {starting_amount} left.\n You have bet {bet_amount}.\n Type 'exit' if you are done.\n ") #Might be wasteful
        
        if current_bet == "exit":
            return bet_amount
        elif current_bet == "1" or current_bet == "5" or current_bet == "100" or current_bet == "500":
            current_bet = int(current_bet)
        else:
            print("Think you've typed wrong")
            
        match current_bet:
            case 1 if starting_amount - current_bet > 0:
                bet_amount += current_bet
                starting_amount -= current_bet
                continue
            case 5 if starting_amount - current_bet > 0:
                bet_amount += current_bet
                starting_amount -= current_bet
                continue
            case 100 if starting_amount - current_bet > 0:
                bet_amount += current_bet
                starting_amount -= current_bet
                continue
            case 500 if starting_amount - current_bet > 0:
                bet_amount += current_bet
                starting_amount -= current_bet
                continue
            case _:
                print("Think you must've typed wrong")
                continue
                
                
                
                
    
def bet_menu(starting_amount):
    
    bet_amount = 0
    
    while starting_amount > 0:
        current_bet = 0
        
        choice = input(f"Welcome to Blackjack! Type 'bet' to bet or Type 'start' to start game or Type 'exit' to leave. \nMoney left : {starting_amount} \nMoney bet: {bet_amount}\n")
        if choice == "start" and bet_amount == 0:
            print("Invalid. You haven't bet anything.")
            continue
        elif choice == "bet":
            current_bet = bet(starting_amount)
            starting_amount -= current_bet
            bet_amount += current_bet
        elif choice == "start":
            return bet_amount
        elif choice == "exit":
            return "exit"
        else:
            print("Invalid. You didn't choose one of the following choices.")
            continue
            
        
def hit():
    return rd.choice(cards)

def calculate_score(deck):
    score = sum(deck)
    
    while score > 21 and 11 in deck:
        deck[deck.index(11)] = 1
        score = sum(deck)
    return score

def display_hands(player_deck, cpu_deck, reveal_cpu=False):
    print(f"\nYour hand: {player_deck} | Total: {calculate_score(player_deck)}")
    if reveal_cpu:
        print(f"CPU hand: {cpu_deck} | Total: {calculate_score(cpu_deck)}")
    else:
        print(f"CPU shows: [{cpu_deck[0]}, '?']")

def player_turn(player_deck, cpu_deck):
    while True:
        display_hands(player_deck, cpu_deck)
        if calculate_score(player_deck) >= 21:
            break
        choice = input("Do you want another card? (y/n): ").lower()
        if choice == 'y':
            player_deck.append(hit())
        elif choice == 'n':
            break
        else:
            print("Please enter 'y' or 'n'.")

def cpu_turn(cpu_deck):
    while calculate_score(cpu_deck) < 17:
        cpu_deck.append(hit())

def determine_winner(player_deck, cpu_deck, cash, bets):
    player_score = calculate_score(player_deck)
    cpu_score = calculate_score(cpu_deck)
    
    print("\n--- Final Results ---")
    display_hands(player_deck, cpu_deck, reveal_cpu=True)

    if player_score > 21:
        print("You busted. CPU wins!")
        cash -= bets
        return cash
    elif cpu_score > 21:
        print("CPU busted. You win!")
        cash = cash + (2 * bets)
        return cash
    elif player_score > cpu_score:
        print("You win!")
        cash = cash + (2 * bets)
        return cash
    elif player_score < cpu_score:
        print("CPU win!")
        cash -= bets
        return cash
    else:
        print("It's a draw!")           
            
   

def main():
    money_brought = 2500
   
    while money_brought > 0:
        bet_money = bet_menu(money_brought) 
        
        if bet_money == "exit":
            break
        else: 
            player_deck = [hit(), hit()]
            cpu_deck = [hit(), hit()]
        
        # Run player's turn
            player_turn(player_deck, cpu_deck)

        # CPU's turn only if player didn't bust
            if calculate_score(player_deck) <= 21:
                cpu_turn(cpu_deck)
                
        #Determines winner and adds or deducts money based on result
            money_brought = determine_winner(player_deck, cpu_deck, money_brought, bet_money)
    
if __name__ == "__main__":
    main()
    
