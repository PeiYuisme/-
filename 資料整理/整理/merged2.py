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
    df.set_index('會計科目', inplace=True)  # 將 '會計科目' 設為索引
    dataframes.append(df)



# 合併所有 DataFrame，按行名稱對齊
merged_df = pd.concat(dataframes, axis=1, join='outer')


# 處理欄位名稱重複（自動加上後綴）
merged_df.columns = [f'Value_{i}' for i in range(len(merged_df.columns))]


# 合併索引重複的行（例如對數值進行加總）
merged_df = merged_df.groupby(merged_df.index).sum()

# 輸出結果
print(merged_df)

# 可選：將合併結果儲存為新的 CSV 檔案
merged_df.to_csv('merged_output.csv')