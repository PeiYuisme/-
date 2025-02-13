import pandas as pd

# 讀取 CSV 文件
file_path = '指標表.csv'  # 替換為您的 CSV 文件路徑
df = pd.read_csv(file_path)

# 添加 seasonsID 欄位並從 1 開始編號
df.insert(0, 'seasonsID', range(1, len(df) + 1))

# 將結果保存回新的 CSV 文件
output_path = '指標表ID.csv'  # 輸出文件的路徑
df.to_csv(output_path, index=False)

print(f"添加完成，已保存至 {output_path}")
