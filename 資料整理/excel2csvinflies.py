import os
import pandas as pd

# 設定來源資料夾路徑和目標資料夾路徑
source_folder = r"C:\Users\TMP214\Desktop\資料庫建Table\建table的CSV\複製"  # 替換為來源 Excel 資料夾路徑
target_folder = r"C:\Users\TMP214\Desktop\資料庫建Table\建table的CSV\複製\CSV" # 替換為目標 CSV 資料夾路徑

# 如果目標資料夾不存在，則創建它
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 獲取來源資料夾內所有 Excel 文件
excel_files = [f for f in os.listdir(source_folder) if f.endswith('.xlsx') or f.endswith('.xls')]

# 轉換每個 Excel 文件為 CSV，並存到目標資料夾
for excel_file in excel_files:
    # 讀取 Excel 文件
    source_file_path = os.path.join(source_folder, excel_file)
    df = pd.read_excel(source_file_path)

    # 生成對應的 CSV 文件名稱並儲存到目標資料夾
    csv_file_name = os.path.splitext(excel_file)[0] + ".csv"  # 保留文件名，改副檔名為 .csv
    target_file_path = os.path.join(target_folder, csv_file_name)

    # 儲存為 CSV 文件
    df.to_csv(target_file_path, index=False)
    print(f"已將 {excel_file} 轉換並儲存為 {csv_file_name} 到目標資料夾")