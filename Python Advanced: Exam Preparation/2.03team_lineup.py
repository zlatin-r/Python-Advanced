def team_lineup(*data):
    teams = {}
    result = ""
    for player, country in data:

        if country not in teams.keys():
            teams[country] = []

            if player not in teams[country]:
                teams[country].append(player)

        else:
            teams[country].append(player)

    teams = sorted(teams.items(), key=lambda x: (-len(x[1]), x[0]))

    for k, v in teams:
        result += f"{k}:\n"
        for player in v:
            result += f"  -{player}\n"

    return result


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))

print(team_lineup(

   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))
