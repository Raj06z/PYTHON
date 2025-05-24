import random
moves = {"r": "ROCK", "p": "PAPER", "s": "SCISSORS"}
win_count, loss_count, tie_count = 0, 0, 0

print("Welcome to Rock, Paper, Scissors!")
while True:
    user_move = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit\n").lower()
    if user_move == "q":
        print("Thanks for playing!")
        break
    elif user_move in moves:
        computer_move = random.choice(list(moves.keys()))
        print(f"\n{moves[user_move]} versus...\n{moves[computer_move]}")

        if user_move == computer_move:
            print("It's a tie!")
            tie_count += 1
        elif (user_move == "r" and computer_move == "s") or \
             (user_move == "p" and computer_move == "r") or \
             (user_move == "s" and computer_move == "p"):
            print("You win!")
            win_count += 1
        else:
            print("You lose!")
            loss_count += 1

        print(f"{win_count} Wins, {loss_count} Losses, {tie_count} Ties\n")
    else:
        print("Invalid input, please enter 'r', 'p', 's', or 'q'.\n")
