import os
import pandas as pd

# 設定資料夾路徑
input_folder = r"C:\Users\TMP214\Desktop\資料整理\綜合損益表"  # 替換為您的資料夾路徑
output_file = r"C:\Users\TMP214\Desktop\資料整理\綜合損益表\merged綜合損益表.csv"  # 合併後的輸出檔案名

# 初始化空的 DataFrame，用於合併
merged_df = pd.DataFrame()

# 遍歷資料夾中的所有 CSV 檔案
for file in os.listdir(input_folder):
    if file.endswith('.csv'):  # 確保處理的是 CSV 檔案
        file_path = os.path.join(input_folder, file)

        # 讀取 CSV 檔案，指定第一列為索引列
        try:
            df = pd.read_csv(file_path, index_col=0, header=0)
        except Exception as e:
            print(f"讀取文件失敗: {file}, 錯誤: {e}")
            continue

        # 清理列名中的空格
        df.columns = df.columns.str.strip()
        df.index = df.index.str.strip()  # 去掉會計科目中的多餘空格

        # 打印檢查每個文件的內容
        print(f"讀取文件: {file}")
        print(df.head())

        # 合併數據，按索引（會計科目）進行外部合併
        if merged_df.empty:
            merged_df = df
        else:
            merged_df = pd.merge(merged_df, df, left_index=True, right_index=True, how='outer')

# 檢查最終的合併結果
print("合併後的數據：")
print(merged_df.head())

# 將合併後的數據保存為新的 CSV 檔案
try:
    merged_df.to_csv(output_file, encoding='utf-8-sig')
    print(f"所有檔案已合併完成，結果儲存在: {output_file}")
except Exception as e:
    print(f"保存文件失敗，錯誤: {e}")
