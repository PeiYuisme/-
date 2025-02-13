import pandas as pd

# 定義文件路徑
input_csv = r"C:\Users\TMP214\Desktop\資料整理\merged_現金流量表.csv"  # 原始檔案名稱
output_csv = r"C:\Users\TMP214\Desktop\資料整理\changed_現金流量表.csv"  # 轉置後的檔案名稱

try:
    # 讀取原始 CSV 文件
    df = pd.read_csv(input_csv)

    # 轉置資料框架（交換行和列）
    transposed_df = df.transpose()

    # 將索引變回普通列
    transposed_df.reset_index(inplace=True)

    # 儲存轉置後的 CSV 文件
    transposed_df.to_csv(output_csv, index=False, header=False)  # 不需要索引和標題

    print(f"CSV 檔案已成功轉置，結果保存至: {output_csv}")

except Exception as e:
    print(f"處理過程中發生錯誤: {e}")
