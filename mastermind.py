import random

print(f"{'MASTERMIND':^48}")
print(f"{'CREATIVE COMPUTING':^48}")
print(f"{'MORRISTOWN, NEW JERSEY':^48}")
print("\n\n")

print("THE GAME OF MASTERMIND\n")

print("COLOR CODES:")
print("               R=RED     O=ORANGE     Y=YELLOW")
print("               G=GREEN   B=BLUE       P=PURPLE\n")

code_colors = {
    'R': 'Red',
    'O': 'Orange',
    'Y': 'Yellow',
    'G': 'Green',
    'B': 'Blue',
    'P': 'Purple'
}

def generate_code():
    code = ''
    for _ in range(4):
        code += random.choice(list(code_colors.keys()))
    return code

def count_black_pegs(guess, code):
    count = 0
    for i in range(len(guess)):
        if guess[i] == code[i]:
            count += 1
    return count

def count_white_pegs(guess, code):
    guess_counts = [0] * len(code_colors)
    code_counts = [0] * len(code_colors)
    white_pegs = 0
    
    for i in range(len(guess)):
        if guess[i] == code[i]:
            continue
        guess_counts[list(code_colors.keys()).index(guess[i])] += 1
        code_counts[list(code_colors.keys()).index(code[i])] += 1
    
    for i in range(len(guess_counts)):
        white_pegs += min(guess_counts[i], code_counts[i])
    
    return white_pegs

def print_board_summary(guesses, blacks, whites):
    print("GUESS\tBLACKS\tWHITES")
    print("-----\t------\t------")
    for i in range(len(guesses)):
        print(guesses[i], blacks[i], whites[i])

def main():
    code = generate_code()
    guesses = []
    blacks = []
    whites = []
    
    for p in range(10):
        print()
        print("MOVE NUMBER", p + 1, " ?")
        guess = input("")
        
        if guess == "BOARD":
            print_board_summary(guesses, blacks, whites)
            continue
        elif guess == "QUIT":
            break
        
        guesses.append(guess)
        blacks.append(count_black_pegs(guess, code))
        whites.append(count_white_pegs(guess, code))
        
        print(blacks[-1], "BLACK PEGS")
        print(whites[-1], "WHITE PEGS")
        
        if blacks[-1] == 4:
            print("\nYOU WIN!!")
            break
    
    else:
        print("\nSORRY, YOU LOSE")
    
    print("THE CORRECT CODE WAS:", code)
    play_again = input("Do you want to play again? (yes/no): ")
    
    if play_again.lower() == "yes":
        main()

if __name__ == "__main__":
    main()
