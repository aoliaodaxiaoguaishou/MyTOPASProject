import os
import pandas as pd

def convert_phsp_to_excel(base_dir):
    """
    读取 base_dir 目录下的所有 .phsp 文件，
    转换为 Excel 格式并保存在 base_dir/excel 目录下，
    并汇总所有数据到 total.xlsx。
    """
    output_dir = os.path.join(base_dir, "excel")
    os.makedirs(output_dir, exist_ok=True)
    
    # 获取所有 .phsp 文件
    phsp_files = [f for f in os.listdir(base_dir) if f.endswith(".phsp")]
    total_data = []
    
    for phsp_file in phsp_files:
        phsp_path = os.path.join(base_dir, phsp_file)
        
        # 读取文件内容
        with open(phsp_path, "r", encoding="utf-8", errors="ignore") as file:
            lines = file.readlines()
        
        # 解析数据，每行按空格拆分
        data = [list(filter(None, line.strip().split())) for line in lines]
        df = pd.DataFrame(data)
        
        # 生成 Excel 文件
        excel_filename = os.path.splitext(phsp_file)[0] + ".xlsx"
        excel_path = os.path.join(output_dir, excel_filename)
        df.to_excel(excel_path, index=False, header=False)
        
        # 追加到总数据列表
        total_data.append(df)
    
    # 汇总所有数据到 total.xlsx
    if total_data:
        total_df = pd.concat(total_data, ignore_index=True)
        total_excel_path = os.path.join(output_dir, "total.xlsx")
        total_df.to_excel(total_excel_path, index=False, header=False)
    
    print(f"转换完成，Excel 文件保存在: {output_dir}")
    
if __name__ == "__main__":
    base_dir = "."  # 当前目录
    convert_phsp_to_excel(base_dir)
