#---------------------------------------
#  User Experience
#    Student C
#---------------------------------------


#---------------------------------------
import random
def choose_difficulty():
    """
    Allows players to choose the difficulty level of the questionsThe user is going to input their choice.

    Parameters: None
    Returns:
    - str: Valid difficulty levels are ('easy', 'medium', 'hard').
    """
    #------------------------
    dif_level=input("Enter the difficulty level of the game (easy , medium , hard ) :")
    return dif_level
    #------------------------
    #------------------------
    


#---------------------------------------

def display_leaderboard(leaderboard):
    """
    Displays the leaderboard, showing top scores in descending order.

    Parameters:
    - leaderboard (dict): A dictionary containing player names as keys and their scores as values.

    Returns: None

    The function sorts the leaderboard by scores in descending order and prints the names and scores of the top players. If the leaderboard is empty, it prints a message indicating that there are no scores to display.
    """
    #------------------------
    # Add your code here
    if leaderboard=={}:
        print("there are no scores to display.")
    else:
        new=sorted(leaderboard.items(),key=lambda x:x[1],reverse=True)
        for i in range(3):
            print(f"player {new[i][0]} scores {new[i][1]}")
    #------------------------
    #------------------------

#---------------------------------------

def save_score(player_name, score, file_path='scores.txt'):
    """
    Saves the player's score to a file.

    Parameters:
    - player_name (str): The name of the player.
    - score (int): The score achieved by the player.
    - file_path (str): The file path to save the score.

    Returns: None
    """
    #------------------------
    # Add your code here
    #------------------------
    try:
        file =open("scores.txt","a")
        file.write(f"{player_name} {score}")
    finally:
        file.close()       
    #------------------------

#---------------------------------------

def load_top_scores(file_path='scores.txt'):
    """
    Loads the top scores from a file into a leaderboard dictionary.

    Parameters:
    - file_path (str): The file path from which to load the scores.

    Returns:
    - dict: The leaderboard dictionary with player names as keys and scores as values.
    """
    #------------------------
    # Add your code here
    d={}
    with open("scores.txt","r") as file:
        c=0
        for line in file:
            name,score=line.split()
            d[name]=int(score)
            c+=1
            if c>2:
                return d 
            
    #------------------------
    #------------------------

#---------------------------------------

def provide_feedback(is_correct):
    """
    Provides feedback to the player after each round.

    Parameters:
    - is_correct (bool): Indicates whether the player's answer was correct.

    Returns: None

    Example:
    - is it correct?   "Well done!"
    - is it incorrect? "Sorry, that's incorrect."
    """
    #------------------------
    # Add your code here
    #------------------------
    if is_correct:
        print("Well done!")
    else:
        print("Sorry, that's incorrect.")
    #------------------------

#---------------------------------------

def fifty_fifty_lifeline(correct_answer, options):
    """
    Provides a 50/50 lifeline by removing two incorrect answers, leaving the correct answer and one other incorrect answer.

    Parameters:
    - correct_answer (str): The correct answer to the current question.
    - options (list): A list containing all possible answers including the correct answer.

    Returns:
    - list: A reduced list of answers containing only the correct answer and one randomly selected incorrect answer.

    This function is designed to be used once per game session by a player who chooses to use the 50/50 lifeline. It randomly selects one incorrect answer to keep along with the correct answer and removes the other options.
    """
    #------------------------
    # Add your code here
    new=[correct_answer]
    while True:
        r=random.randint(0,len(options)-1)
        if options[r] not in new:
            new.append(options[r])
            return new
    #------------------------
    #------------------------

#---------------------------------------

def skip_question(allowed_skips):
    """
    Allows the player to skip a question during the game.

    Parameters:
    - allowed_skips (int): The number of skips available to the player.

    Returns:
    - bool: True if the skip was successful (and a skip was available), False otherwise.

    This function checks if the player has any skips available. If so, it decrements the allowed_skips counter and returns True, indicating the question can be skipped. If no skips are available, it returns False. This function should be called before presenting a new question to the player.
    """
    #------------------------
    # Add your code here
    if allowed_skips>0:
        allowed_skips-=1
        return True
    return False
    #------------------------
    #------------------------

#---------------------------------------



