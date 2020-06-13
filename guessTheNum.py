#                 GUESS THE NUMBER GAME
import random

def guessmain(nog):
    while nog >= 1:
        try:
            num1 = int(input("Enter a number : "))
        except Exception as e:
            print("!!!!!!!!Rules!!!!!!!!!!!")
            print("1. Enter integer values only.\n2. The range of number should not exceed 999.\n")
        else:
            if num1 == n:
                print("//////////////// WINNER /////////////////\n")
                print("Congratulation..You have guess the write number ")
                print("number of gusses taken : "+str(5-nog+1))
                break
                pass
            else:
                print("Please try again.")
                if num1 > n:
                    print("Tip: try a smaller number.")
                else:
                    print("Tip: Try a larger number. ")
                nog = nog-1
                print("Number of guesses left out of 5 : "+str(nog)+"\n")
                if nog == 0:
                    print("///////////////GAME OVER/////////////////\nYou loss: Better luck next time.")
                else: continue
            continue

if __name__ == '__main__':
    exit = False
    while exit is False:
        print("\n///////////////////GUESS THE NUMBER///////////////////")
        print(("\t\t\t\t\t s -- > Start\n\t\t\t\t\t r --> Rules\n\t\t\t\t\t e --> Exit"))
        rules = input("Enter your choice : ")
        if rules == "r":
            print("!!!!!!!!Rules!!!!!!!!!!!")
            print("1. Enter integer values only.\n2. The range of number should not exceed 999.\n")
            continue
        elif rules == "s":
            print("\n!!!!!!!!Start!!!!!!!!!!!")
            n = random.randint(0, 999)     # generating random number to guess
            # print(n)
            nog = 5                        # nog = no. of guesses
            guessmain(nog)
        elif rules == "e":
            exit = True
        else: print("Invalid input!")
