import os
import pandas as pd

# 指定資料夾路徑
folder_path = r"C:\Users\TMP214\Desktop\資料整理\綜合損益表\new\csv"


# 讀取所有 CSV 檔案
all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]

# 儲存所有資料
dataframes = []

for file in all_files:
    try:
        # 讀取每個 CSV 檔案
        df = pd.read_csv(file)
        dataframes.append(df)
    except Exception as e:
        print(f"Error reading {file}: {e}")

# 合併所有資料
if dataframes:
    merged_df = pd.concat(dataframes, ignore_index=True)
    
    # 確保 "本業獲利" 欄位存在
    if "本業獲利" in merged_df.columns:
        # 合併重複的 "本業獲利"，保留非空值
        merged_df = merged_df.groupby("本業獲利", as_index=False).first()
        
        # 儲存結果
        output_file = os.path.join("cry", "merged綜合損益表.csv")
        merged_df.to_csv(output_file, index=False, encoding='utf-8-sig')
        output_file
    else:
        "Error: 找不到 '本業獲利' 欄位，請確認資料格式。"
else:
    "資料夾中無有效的 CSV 檔案。"
