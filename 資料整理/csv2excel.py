import pandas as pd

# 讀取 CSV 文件
csv_file_path = '新增指標 - 數據.csv'  # 替換為您的 CSV 文件路徑
df = pd.read_csv(csv_file_path)

# 將資料保存為 Excel 文件
excel_file_path = '新增指標數據.xlsx'  # 輸出 Excel 文件的路徑
df.to_excel(excel_file_path, index=False)

print(f"CSV 文件已成功轉換為 Excel 文件，保存於 {excel_file_path}")
