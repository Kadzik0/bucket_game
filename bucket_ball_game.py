
from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():

    guess=''

    while guess not in ['0','1','2']:
        guess=input('Pick a numver: 0,1 or 2: ')
        if guess not in ['0','1','2']:
            print('Input correct number!')
        else:
            pass
    return int(guess)

def bucket_ball_game(GameResult, PlayersGuess):
    for num,blank in enumerate(GameResult):
        if blank=="0":
            index_result=num

    if GameResult[PlayersGuess]=="0":
        print('congratulations! Your guess at {} was correct!'.format(PlayersGuess))
    else:
        print('Unfortunately, your guess at {} wasnt correct\nCorret number was {}'.format(PlayersGuess,index_result))



game_list = [" ", "0", " "]

game_result = shuffle_list(game_list)

myindex = player_guess()

bucket_ball_game(game_result, myindex)
