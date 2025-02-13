# import csv

# # 定義文件路徑
# input_csv = r"C:\Users\TMP214\Desktop\資料整理\merged_綜合損益表.csv"  # 原始檔案路徑
# output_csv = r"C:\Users\TMP214\Desktop\資料整理\changed_綜合損益表.csv"  # 輸出檔案路徑

# try:
#     # 打開原始文件進行讀取
#     with open(input_csv, mode='r', encoding='utf-8') as infile:
#         reader = csv.reader(infile)
#         rows = list(reader)  # 將所有行讀取為列表
        
#         # 從第二行開始為每個值加上雙引號
#         for i in range(1, len(rows)):  # 遍歷第二行到最後一行
#             rows[i] = [f'"{value}"' for value in rows[i]]

#     # 打開文件進行寫入
#     with open(output_csv, mode='w', encoding='utf-8', newline='') as outfile:
#         writer = csv.writer(outfile)
#         writer.writerows(rows)  # 寫入所有行

#     print(f"從第二行開始已成功為值加上雙引號，結果已保存至 {output_csv}")

# except Exception as e:
#     print(f"處理過程中發生錯誤: {e}")


import csv

# 讀取原始 CSV 檔案
input_csv = r"C:\Users\TMP214\Desktop\資料庫建Table\建table的CSV\模糊搜尋\公式 - search.csv"  # 原始檔案名稱
output_csv = r"C:\Users\TMP214\Desktop\資料庫建Table\建table的CSV\模糊搜尋\模糊搜尋複製用.csv"  # 輸出檔案名稱

try:
    # 讀取並修改內容
    with open(input_csv, mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        # 手動處理每個值，加上雙引號
        rows = [[f'"{value}"' for value in row] for row in reader]

    # 手動輸出修改後的內容
    with open(output_csv, mode='w', encoding='utf-8', newline='') as outfile:
        for row in rows:
            outfile.write(",".join(row) + "\n")

    print(f"已將值加上引號，儲存至 {output_csv}")

except Exception as e:
    print(f"處理過程中發生錯誤: {e}")