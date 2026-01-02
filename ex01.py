import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "Malgun Gothic"

plt.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame({
    "hour" : [9,12,15,17,21],
    "views" : [120,340,560,430,290]
})

plt.plot(df["hour"],df["views"])
plt.title("시간대별 조회수")
plt.xlabel("시간")
plt.ylabel("조회수")

plt.show()