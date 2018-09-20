moves = 0
solution = "SSNWES"
direction = ""
lives = 3

while True:
    nsew = input ("You are in the magic maze. Which way to go? N,S,E,W")
    direction += nsew
    moves += 1


    if moves % 10 == 0:
        lives -= 1
        print ("you have ",lives, "more to go")

        if lives == 0:
            print ("you lost, LOSER")
            break


    if direction.__contains__(solution):
        print("You have escaped the maze in ", moves, "moves")
        break