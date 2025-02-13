import os
import pandas as pd

# 資料夾路徑
folder_path = r"C:\Users\TMP214\Desktop\綜合損益表CSV"

# 獲取資料夾內所有 CSV 檔案
file_list = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]

# 讀取並合併
dataframes = []
for file in file_list:
    df = pd.read_csv(file)  # 讀取每個文件
    
    # 確保 '會計科目' 存在
    if '會計科目' not in df.columns:
        raise ValueError(f"'會計科目' 欄位不存在於檔案: {file}")
    
    # 添加檔案名稱作為一個新欄位，方便區分
    df['來源檔案'] = os.path.basename(file)
    
    # 將 DataFrame 添加到列表中
    dataframes.append(df)

# 合併所有 DataFrame
merged_df = pd.concat(dataframes, axis=0, ignore_index=True)

# 將資料以「會計科目」為主鍵進行透視表處理（寬表格式）
final_df = merged_df.pivot_table(
    index='會計科目',  # 將「會計科目」作為索引
    columns='來源檔案',  # 使用「來源檔案」區分不同檔案的數據
    aggfunc='sum',  # 將重複值相加，您可以改為其他函數，如 'first'
    fill_value=0  # 如果某檔案中沒有對應「會計科目」，填充為 0
)

# 重設索引以方便保存為 CSV
final_df.reset_index(inplace=True)

# 輸出結果
print(final_df)

# 將合併結果儲存為新的 CSV 檔案
final_df.to_csv('merged_output.csv', index=False)