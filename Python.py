import random
rock='🪨'
paper='📄'
scissor='✂'
game={"rock":rock,"paper":paper,"scissor":scissor}
i=input("Enter the player1 object").lower()
l=['rock','paper','scissor']
j=random.choice(l)
print("Users Choice",game[i])
print("Computers choice",game[j])
print(i,j)
if i==j:
    print("No one wins")
elif (i=="rock" and j=="scissor") or (i=="paper" and j=="rock") or (i=="scissor" and j=="paper"):
    print("Player1 wins")
else:
    print("Player2 wins")
