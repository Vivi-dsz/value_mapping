# Define the sentiment function
def score_to_sentiment(score):
    """
    We have a column score, like star, that user gives as a review score.
    We could get a sentiment out of these scores. That is eg 3 neutral, >3 is positive, and <3 is negative.
    """
    score = int(score)
    if score >= 4:
        return "POSITIVE"
    elif score == 3:
        return "NEUTRAL"
    else:
        return "NEGATIVE"
