# FF
## 2.5
def is_leveon(player):
    if player.lower() == "le'veon bell":
        return True
    else:
        return False

def commentary(score):
    if score >= 100:
        return f'{score} is a good score'
    else:
        return f'{score} is not a good score'

positions = ['QB', 'RB', 'WR', 'TE', 'K', 'DST']