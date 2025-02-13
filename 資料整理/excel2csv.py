import pandas as pd

# 讀取 Excel 檔案
excel_file = r"C:\Users\TMP214\Desktop\資料庫建Table\建table的CSV\複製\新的綜合損益表.xlsx"  # 替換為你的 Excel 文件路徑
df = pd.read_excel(excel_file)

# 將 Excel 儲存為 CSV 檔案
csv_file = "綜合損益表複製用.csv"  # 替換為你希望的 CSV 文件名稱
df.to_csv(csv_file, index=False)  # index=False 避免輸出索引欄位

print(f"Excel 檔案已成功轉換為 CSV: {csv_file}")