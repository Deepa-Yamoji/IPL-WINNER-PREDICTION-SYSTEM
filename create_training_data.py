import json
import csv
import os

DATA_FOLDER = "ipl_json"
OUTPUT_FILE = "live_match_training_data.csv"

rows = []

for filename in os.listdir(DATA_FOLDER):

    if not filename.endswith(".json"):
        continue

    filepath = os.path.join(DATA_FOLDER, filename)

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            match = json.load(f)

        info = match.get("info", {})

        teams = info.get("teams", [])
        if len(teams) != 2:
            continue

        team1 = teams[0]
        team2 = teams[1]

        toss = info.get("toss", {})
        toss_winner = toss.get("winner", "")

        outcome = info.get("outcome", {})
        winner = outcome.get("winner", "")

        if not winner:
            continue

        venue = info.get("venue", "")
        city = info.get("city", "")

        innings_list = match.get("innings", [])

        for innings in innings_list:

            team = innings.get("team", "")

            if team not in teams:
                continue

            opponent = team2 if team == team1 else team1

            score = 0
            wickets_lost = 0
            balls = 0

            overs_list = innings.get("overs", [])

            for over in overs_list:

                deliveries = over.get("deliveries", [])

                for delivery in deliveries:

                    runs = delivery.get("runs", {})

                    batter_runs = runs.get("batter", 0)
                    extras = runs.get("extras", 0)

                    score += batter_runs + extras

                    wickets = delivery.get("wickets", [])

                    for wicket in wickets:
                        player_out = wicket.get("player_out")

                        if player_out:
                            wickets_lost += 1

                    balls += 1

                    overs_completed = balls // 6
                    remaining_balls = balls % 6

                    overs_decimal = overs_completed + (remaining_balls / 6)

                    if overs_decimal > 0:
                        run_rate = score / overs_decimal
                    else:
                        run_rate = 0

                    rows.append({
                        "team": team,
                        "opponent": opponent,
                        "toss_winner": toss_winner,
                        "venue": venue,
                        "city": city,
                        "score": score,
                        "wickets_lost": wickets_lost,
                        "overs_completed": round(overs_decimal, 2),
                        "run_rate": round(run_rate, 2),
                        "winner": winner
                    })

    except Exception as e:
        print(f"Error reading {filename}: {e}")


fieldnames = [
    "team",
    "opponent",
    "toss_winner",
    "venue",
    "city",
    "score",
    "wickets_lost",
    "overs_completed",
    "run_rate",
    "winner"
]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:

    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

print()
print("======================================")
print("Training data created successfully!")
print("======================================")
print(f"Total training rows: {len(rows)}")
print(f"Output file: {OUTPUT_FILE}")