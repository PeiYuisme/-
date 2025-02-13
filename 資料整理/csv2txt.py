import csv

# 定義檔案路徑
input_csv = r"C:\Users\TMP214\Desktop\資料整理\added_綜合損益表2.csv"  # 原始 CSV 檔案
output_txt = r"C:\Users\TMP214\Desktop\資料整理\綜合損益表.txt"  # 輸出文字檔

try:
    # 讀取原始 CSV 檔案
    with open(input_csv, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = list(reader)  # 讀取所有行為列表

    # 寫入文字檔，為每行內容加上括號
    with open(output_txt, mode='w', encoding='utf-8') as outfile:
        for row in rows:
            # 將行內容用逗號拼接，並加上括號
            line = f"({','.join(row)})"
            outfile.write(line + "\n")

    print(f"已成功將 CSV 檔轉換為文字檔並加上括號，儲存至 {output_txt}")

except Exception as e:
    print(f"處理過程中發生錯誤: {e}")
