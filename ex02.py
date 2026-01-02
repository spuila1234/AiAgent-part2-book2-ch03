import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame({
    "hour" : [9,12,15,17,21],
    "views" : [120,340,560,430,290]
})

# 1행 3열 서브플롯 구성
fig, axes = plt.subplots(1, 3, figsize=(15, 4))  # 3개 축을 가로로 배치

# 1) 꺾은선 그래프
axes[0].plot(df["hour"], df["views"])
axes[0].set_title("시간대별 조회수 - plot")
axes[0].set_xlabel("시간")
axes[0].set_ylabel("조회수")

# 2) 막대 그래프
axes[1].bar(df["hour"], df["views"])
axes[1].set_title("시간대별 조회수 - bar")
axes[1].set_xlabel("시간")
axes[1].set_ylabel("조회수")

# 3) 산점도 (scatter)
axes[2].scatter(df["hour"], df["views"])
axes[2].set_title("시간대별 조회수 - scatter")
axes[2].set_xlabel("시간")
axes[2].set_ylabel("조회수")

plt.tight_layout()
plt.show()
