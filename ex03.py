import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams['axes.unicode_minus'] = False

df = pd.DataFrame({
    "hour" : [9,12,15,17,21],
    "views" : [120,340,560,430,290]
})

# 새 그림 생성
plt.figure(figsize=(15, 4))

# 1) 꺾은선 그래프 (왼쪽)
ax1 = plt.subplot(1, 3, 1)
ax1.plot(df["hour"], df["views"])
ax1.set_title("시간대별 조회수 - plot")
ax1.set_xlabel("시간")
ax1.set_ylabel("조회수")

# 2) 막대 그래프 (가운데)
ax2 = plt.subplot(1, 3, 2)
ax2.bar(df["hour"], df["views"])
ax2.set_title("시간대별 조회수 - bar")
ax2.set_xlabel("시간")
ax2.set_ylabel("조회수")

# 3) 산점도 (오른쪽)
ax3 = plt.subplot(1, 3, 3)
ax3.scatter(df["hour"], df["views"])
ax3.set_title("시간대별 조회수 - scatter")
ax3.set_xlabel("시간")
ax3.set_ylabel("조회수")

plt.tight_layout()
plt.show()
