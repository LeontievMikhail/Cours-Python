import json
filename= "user_settings.txt"
myfile = open(filename, 'w')

player1= {
    'PlayerName': "Egor",
    'Score': 3434534,
    'awards': ["or", "nv", "ny"]
}

player2 = {
    'PlayerName': "Nikita",
    'Score': 345345345,
    'awards': ["or", "nv"]
}

myplayer=[]
myplayer.append(player1)
myplayer.append(player2)

json.dump(myplayer, myfile)


#______________ open file for view

myfile = open(filename, mode='r')
json_data=json.load(myfile)
for user in json_data:
    print("Player name is: "+ str(user['PlayerName']))
    for awards in user['awards']:
        print(awards)