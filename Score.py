from Utils import Path


def add_score(chosen_difficulty):
    global score
    points_of_winning = str((chosen_difficulty * 3) + 5)

    try:
        score = open(Path("Scores.txt"), "r")
        score = open(Path("Scores.txt"), "a")
        score.write(f" ,{points_of_winning}")
        score.close()
    except:
        score = open(Path("Scores.txt"), "x")
        score.write(f" ,{points_of_winning}")
        score.close()
    finally:
        score.close()
