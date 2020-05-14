n=75
num1=int (input("Enter a number : "))
nog=5
while nog>=1:              #nog = no. of guesses

    if num1==n:
        print("//////////////// WINNER /////////////////\n")
        print("Congratulation..You have guess the write number ")
        print("number of gusses taken : "+str(nog))
        break
    else:
        print("Please try again.")
        if num1>n:
            print("Tip: try a smaller number.")
        else:
            print("Tip: Try a larger number. ")
        nog=nog-1
        print("Number of guesses left out of 5 : "+str(nog)+"\n")
        if nog==0:
            print("///////////////GAME OVER/////////////////\nYou loss: Better luck next time.")
        else:
            num1 = int(input("Enter a number : "))
    continue

