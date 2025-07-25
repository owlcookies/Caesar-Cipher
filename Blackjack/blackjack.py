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
   allowed_bets = {1, 5, 100, 500}
   
   bet = 0
   
   while True:
        current_bet = 0
        user_input =  input(f"Money Remaining: {starting_amount} \nPlace your bet (1, 5, 100, 500) or type 'exit' to quit or type 'start' to start the game: ").strip().lower()
       
        if user_input == "start" and bet == 0 :
            print("Invalid. You haven't bet anything.")
            continue
        elif user_input == "start":
            print("Exiting the betting system. Time to play!!")
            return starting_amount
        elif user_input == "exit":
            print("Exiting the game. Thanks for playing!")
            return "exit"
       
        try:
            current_bet = int(user_input)
            print(current_bet)
            if current_bet in allowed_bets:
                print(f"You have bet {current_bet}.")
                bet += current_bet
                
            else:
                print(f"Invalid bet amount. Please choose from {allowed_bets}.") 
        except ValueError:
            print("Invalid input. Please enter a number (1, 5, 100, 500) or 'exit'.")
         
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
        bet_money = bet(money_brought) 
        
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
    
