import datetime
import json
import random

class Result():
    def __init__(self, score, player_name, date):
        self.score = score
        self.player_name = player_name
        self.date = date

def get_score_list():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list

def play_game(level, player_name):
    secret = random.randint(1, 30)
    attempts = 0

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        score_list = get_score_list()

        if guess == secret:
            result = Result(attempts, player_name, str(datetime.datetime.now()))
            score_list.append(result.__dict__)        
            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret and level == 'easy':
            print("Your guess is not correct... try something smaller")
        elif guess < secret and level == 'easy':
            print("Your guess is not correct... try something bigger")
        elif guess != secret and level == 'hard':
            print("Your guess is not correct!!")

def get_top_scores():
    top_scorers = sorted(get_score_list(), key = lambda i: (i['score'], i['date']))
    return top_scorers[:3]