# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    import random

    if prev_play:
        opponent_history.append(prev_play)

    counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}

    pattern_size = 3  # Look at last 3 opponent moves
    if len(opponent_history) < pattern_size:
        return random.choice(['R', 'P', 'S'])

    # Build pattern history
    patterns = {}
    for i in range(len(opponent_history) - pattern_size):
        pattern = ''.join(opponent_history[i:i+pattern_size])
        next_move = opponent_history[i + pattern_size]
        if pattern not in patterns:
            patterns[pattern] = {'R': 0, 'P': 0, 'S': 0}
        patterns[pattern][next_move] += 1

    # Use the most recent pattern to predict
    last_pattern = ''.join(opponent_history[-pattern_size:])
    if last_pattern in patterns:
        prediction = max(patterns[last_pattern], key=patterns[last_pattern].get)
        return counter_moves[prediction]
    else:
        return random.choice(['R', 'P', 'S'])

