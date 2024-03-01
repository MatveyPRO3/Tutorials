import pandas as pd

f_path = "Задача про футбол.xlsx"

df = pd.read_excel(f_path,1)

for team in set(df["HomeTeam"]):


    goals_home = []
    goals_away = []

    for row in df.iterrows():
        # print(row[1]["HomeTeam"])
        if row[1]["HomeTeam"] == team:
            goals_home.append(row[1]["Goals(HomeTeam)"])
        elif row[1]["AwayTeam"] == team:
            goals_away.append(row[1]["Goals(AwayTeam)"])
        # break
        
    # print(sum(goals_away)/len(goals_away))
    # print(sum(goals_home)/len(goals_home))

    print(sum(goals_home)/len(goals_home)<sum(goals_away)/len(goals_away))
