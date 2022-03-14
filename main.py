from functions import play_game, get_top_scores, Result

while True:
    
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")
    if selection.lower() == "a":
        player_name = input('Please type your name: ')
        level  = input("Chose level: easy/hard ")
        play_game(level, player_name)
    elif selection.lower() == "b":
        for score_dict in get_top_scores():
            print(score_dict.get("player_name") + ' --> ' + str(score_dict["score"]) + " attempts, date: " + score_dict.get("date"))
    else:
        break
