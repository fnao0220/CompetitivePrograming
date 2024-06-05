import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# データの読み込み
data = pd.read_csv('data.csv', parse_dates=['timestamp'])

# データの確認
print(data.head())

# データの加工
# 例として、プロセスステップごとの平均歩留まりと欠陥数を計算
grouped_data = data.groupby('process_step').agg({
    'yield': 'mean',
    'defects': 'sum'
}).reset_index()

print(grouped_data)

# データの可視化
# 歩留まりの推移
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='timestamp', y='yield', marker='o')
plt.title('Yield Over Time')
plt.xlabel('Time')
plt.ylabel('Yield (%)')
plt.grid(True)
plt.show()

# プロセスステップごとの平均歩留まりと欠陥数の棒グラフ
fig, ax1 = plt.subplots(figsize=(10, 6))

ax2 = ax1.twinx()
sns.barplot(data=grouped_data, x='process_step', y='yield', ax=ax1, color='b', alpha=0.6)
sns.barplot(data=grouped_data, x='process_step', y='defects', ax=ax2, color='r', alpha=0.6)

ax1.set_xlabel('Process Step')
ax1.set_ylabel('Average Yield (%)', color='b')
ax2.set_ylabel('Total Defects', color='r')

plt.title('Average Yield and Total Defects per Process Step')
plt.show()

# 基本的な統計解析
# プロセスステップごとの歩留まりの標準偏差を計算
std_yield = data.groupby('process_step')['yield'].std()
print(std_yield)

# 解析結果の改善点の例示
for step, std in std_yield.items():
    if std > 2:  # ここでは標準偏差が2を超える場合を改善点としています
        print(f"Process step {step} has high variability in yield (std: {std:.2f}). Consider investigating this step.")

