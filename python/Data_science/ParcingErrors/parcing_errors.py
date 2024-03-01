import plotly.express as px
import pandas as pd
import re
from time import sleep
print("scanning...")


num_lines = 0
num_lines_error = 0
statistic = []
total_lines = 0


regex = re.compile("[0-9][0-9]:[0-9][0-9]:[0-9][0-9]")


with open("logsms.json", "r") as file:

    line = file.readline()
    matcher = regex.search(line)

    time = str(matcher.group(0))
    time_list = [time, 0]

    while line:
        if "Error" in line:

            matcher = regex.search(line)

            time = str(matcher.group(0))
            if time_list[0] == time:
                time_list[1] += 1
            else:
                statistic.append(time_list)
                time_list = [time, 1]

            num_lines_error += 1
        else:

            num_lines += 1
            pass
        line = file.readline()
        total_lines += 1

    statistic.append(time_list)
df = pd.DataFrame(statistic, columns=["time", "errors"])
print("creating csv file...")
df.to_csv("stat.csv", index=False)

sleep(0.5)
print(f"errors: {num_lines_error}; without: {num_lines}; total: {total_lines}")

fig = px.scatter(df, x="time", y="errors", size="errors",
                 color="errors")  # histogram or bar or line or scatter


fig.update_layout(xaxis_title="Time",
                  yaxis_title="Error logs rate (%)", legend_title="Logs rate")
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([

                dict(
                    args=["type", "scatter"],
                    label="Scatter Plot",
                    method="restyle"
                ),
                dict(
                    args=["type", "bar"],
                    label="Bar Chart",
                    method="restyle"
                )

            ]),
            direction="down",
        ),
    ]
)
fig.show()
input()
