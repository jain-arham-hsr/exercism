from collections import defaultdict


def tally(rows):
    score_tally = defaultdict(lambda: defaultdict(int))
    for row in rows:
        team_1, team_2, result = row.split(';')
        score_tally[team_1]['MP'] += 1
        score_tally[team_2]['MP'] += 1
        if result == 'win':
            score_tally[team_1]['W'] += 1
            score_tally[team_1]['P'] += 3
            score_tally[team_2]['L'] += 1
        if result == 'loss':
            score_tally[team_2]['W'] += 1
            score_tally[team_2]['P'] += 3
            score_tally[team_1]['L'] += 1
        if result == 'draw':
            score_tally[team_1]['D'] += 1
            score_tally[team_2]['D'] += 1
            score_tally[team_1]['P'] += 1
            score_tally[team_2]['P'] += 1
    res = ["Team                           | MP |  W |  D |  L |  P"]
    for team_name, team_tally in sorted(score_tally.items(), key=lambda pair: (pair[1]['P']*(-1), pair[0])):
        res.append(
            f"{team_name+(31-len(team_name))*' '}|"
            f"  {team_tally['MP']} |"
            f"  {team_tally['W']} |"
            f"  {team_tally['D']} |"
            f"  {team_tally['L']} |"
            f"  {team_tally['P']}"
        )
    return res
