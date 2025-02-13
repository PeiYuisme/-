import os
import pandas as pd

# 設定輸入資料夾和輸出資料夾
input_folder = r"C:\Users\TMP214\Desktop\資料整理\綜合損益表"
output_folder = os.path.join(input_folder, "new")
os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith('.xls'):
        xls_path = os.path.join(input_folder, file)
        xlsx_path = os.path.join(output_folder, file.replace('.xls', '.xlsx'))

        try:
            # 嘗試讀取文件
            try:
                df = pd.read_excel(xls_path, engine='xlrd')
            except Exception:
                tables = pd.read_html(xls_path)
                df = tables[0]

            # 處理 MultiIndex 列名
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = ['_'.join(map(str, col)).strip() for col in df.columns]

            # 保存為 .xlsx
            df.to_excel(xlsx_path, index=False, engine='openpyxl')
            print(f"成功轉換: {file} -> {xlsx_path}")
        except Exception as e:
            print(f"轉換失敗: {file}, 錯誤: {e}")

print(f"所有文件已處理完成，結果存儲於: {output_folder}")
