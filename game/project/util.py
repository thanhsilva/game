class Util():
    def format_score(score):
        if score < 10:
            score = "0" + str(score)
        return str(score)