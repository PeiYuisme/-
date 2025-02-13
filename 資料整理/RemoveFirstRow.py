import csv

# 定義文件路徑
input_csv = r"C:\Users\TMP214\Desktop\資料整理\merged_現金流量表.csv"  # 原始檔案名稱
output_csv = r"C:\Users\TMP214\Desktop\資料整理\changed_現金流量表.csv"  # 處理後的檔案名稱

try:
    # 打開原始 CSV 文件
    with open(input_csv, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)  # 讀取所有行

        # 移除第一行
        if rows:
            rows = rows[1:]  # 移除第一行

    # 將處理後的數據寫入新文件
    with open(output_csv, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

    print(f"已成功移除第一行，結果保存至: {output_csv}")

except Exception as e:
    print(f"處理過程中發生錯誤: {e}")
