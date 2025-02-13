import os
import pandas as pd

# 指定資料夾路徑
folder_path = "三大\三大表各季檔案\資產負債表csv檔"

# 讀取所有 CSV 檔案
all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]

# 處理每個 CSV 檔案
for file in all_files:
    try:
        # 讀取每個 CSV 檔案
        df = pd.read_csv(file)

        # 去除空格並左移
        for col in df.columns:
            df[col] = df[col].astype(str).str.strip()  # 移除字串中的空格
        df = df.apply(lambda x: pd.Series(x.dropna().values), axis=1)  # 左移數值

        # 儲存處理後的 CSV
        output_file = os.path.join(folder_path, f"processed_{os.path.basename(file)}")
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"已處理並儲存: {output_file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")
