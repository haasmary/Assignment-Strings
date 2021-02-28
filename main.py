# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player1='Ruud Gullit' 
player2='Marco van Basten'

goal_0= 32
goal_1= 54

scorers= player1 +" "+str(goal_0) +", "+ player2 +" "+str(goal_1)

report = f'{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute'

player='Frank Rijkaard'
first_name=player[player.find("Frank"):5]
last_name_len=len(player[player.find("R"):14])
name_short=player[0:1]+". "+player[6:]
chant=(player[0:5]+'! ')*4 +player[0:5]+'!'
good_chant= chant[-1]!=' '
