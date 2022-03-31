from Utils import Path


def add_score(chosen_difficulty):
    points_of_winning = int((chosen_difficulty * 3) + 5)


    try:
        s_file = open(Path("Scores.txt"), "r")
        old_score = s_file.read()
        old_score = int(old_score)
        s_file = open(Path("Scores.txt"), "w")
        score = str(old_score + points_of_winning)
        s_file.write(str(score))

        s_file.close()

    except:
        s_file = open(Path("Scores.txt"), "x")
        s_file.write(str(points_of_winning))
        s_file.close()

