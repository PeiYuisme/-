import pandas as pd

# 載入 Excel 檔案
file_path = r'C:\Users\TMP214\Desktop\資料庫建Table\建table的CSV\複製\綜合損益表.xlsx'  # 替換為您的檔案路徑
sheet_name = '工作表1'  # 替換為您的工作表名稱


data = pd.read_excel(file_path, sheet_name=sheet_name)

# 將數據從第二欄開始到最後一欄進行單位轉換（億轉為千元）
conversion_factor = 100000
columns_to_convert = data.columns[1:]  # 從第二欄開始到最後一欄

for column in columns_to_convert:
    if data[column].dtype in ['int64', 'float64']:
        data[column] = data[column] * conversion_factor

# 儲存到新的 Excel 檔案
output_path = '新的綜合損益表.xlsx'
data.to_excel(output_path, index=False)

print(f"已完成單位轉換，檔案儲存為 {output_path}")
