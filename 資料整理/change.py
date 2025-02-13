import pandas as pd

# 輸入的 Excel 檔案路徑與名稱
input_excel = '指標\2024Q3-2022Q2 (清理).xlsx'
# 輸出的 CSV 檔案名稱
output_csv = '指標表.csv'

# 讀取 Excel 第一个工作表 (可使用 sheet_name 指定特定工作表)
df = pd.read_excel(input_excel, sheet_name=0)

# 將資料轉置 (欄與列對調)
df_transposed = df.T

# 將轉置後的結果寫出為 CSV 檔案
df_transposed.to_csv(output_csv, index=True)  # 若不需要輸出 index 可改為 index=False