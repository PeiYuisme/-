import pandas as pd

# 讀取 CSV 檔案
file_path = "merged_output.csv"  # 替換為你的檔案路徑
df = pd.read_csv(file_path)

# 檢查 'Name' 欄位是否有重複的值
duplicated_names = df[df.duplicated(subset=['會計科目'], keep=False)]  # `keep=False` 保留所有重複值

# 顯示重複的行
print("重複的名稱：")
print(duplicated_names)

# 如果只需要重複的名稱列表：
repeated_names = duplicated_names['會計科目'].unique()
print("重複的名稱列表：", repeated_names)