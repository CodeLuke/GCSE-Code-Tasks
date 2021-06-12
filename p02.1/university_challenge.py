"""
Problem:

    
On the TV show, University Challenge, teams compete against each other
    
to answer as many questions as possible correctly, which gives each
    
team points. The winner always progress to the next round. However,
    
a few losers also go through if they score enough points, in this case
    
120.

    The function challenge takes in the scores of both teams.
    
If team1 wins -> print "Team 1 progresses"
    
If team2 wins -> print "Team 2 progresses"
    
However, if the losing team scores 120 points or more, or there is a
    
draw, instead print: "Both teams progress"

Tests:

    
>>> challenge(110, 85)
Team 1 progresses
    
>>> challenge(90, 140)
Team 2 progresses
    
>>> challenge(135, 125)    
Both teams progress

>>> challenge(105, 105)
Both teams progress
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def challenge(score1, score2):
    """
    Simple solution
    """
    cutoff = 120
    if score1 > score2 and score2 < cutoff:
        print("Team 1 progresses")
    elif score2 > score1 and score1 < cutoff:
        print("Team 2 progresses")
    else:
        print("Both teams progress")

def challenge_advan(score1, score2):
    """
    More advanced solution
    """
    cutoff = 120
    team1, team2 = {"name": "Team 1", "score": score1}, {"name": "Team2", "score": score2}
    winner, loser = (team1, team2) if team1["score"] >= team2["score"] else (team2, team1)
    
    if winner["score"] == loser["score"] or loser["score"] >= cutoff:
        print("Both teams progress")
    else:
        print(winner["name"], "progresses")


if __name__ == "__main__":
    run_tests()