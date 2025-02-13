def process_txt_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 使用正則表達式提取括號內的部分，保留括號
    import re
    lines = re.findall(r'\((.*?)\)', content)

    processed_lines = []
    for line in lines:
        # 按逗號分隔，並加上引號
        values = line.split(',')
        processed_line = '(' + ','.join(f'"{value.strip()}"' for value in values) + ')'
        processed_lines.append(processed_line)

    # 寫入新檔案
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(processed_lines))

# 使用範例
input_file = r'C:\Users\TMP214\Desktop\資料整理\現金流量表.txt'
output_file = r'C:\Users\TMP214\Desktop\資料整理\現金流量表2.txt'
process_txt_file(input_file, output_file)
