import os
import pandas as pd

def combine_and_clean_excel(input_folder, output_file):
    print("=" * 50)
    print("      Excel Data Automation & Merger Script      ")
    print("=" * 50)
    
    all_data = []
    
    # قراءة كل ملفات الاكسل داخل المجلد
    for file in os.listdir(input_folder):
        if file.endswith('.xlsx') or file.endswith('.xls'):
            file_path = os.path.join(input_folder, file)
            print(f"[*] Processing file: {file}...")
            
            # قراءة البيانات
            df = pd.read_excel(file_path)
            all_data.append(df)

    if not all_data:
        print("[!] No Excel files found in the folder.")
        return

    # دمج جميع البيانات في جدول واحد
    combined_df = pd.concat(all_data, ignore_index=True)
    
    # تنظيف البيانات: حذف الصفوف المكررة
    initial_count = len(combined_df)
    combined_df.drop_duplicates(inplace=True)
    cleaned_count = len(combined_df)
    
    print(f"\n[+] Total rows merged: {initial_count}")
    print(f"[+] Duplicate rows removed: {initial_count - cleaned_count}")

    # حفظ الملف النهائي المدمج
    combined_df.to_excel(output_file, index=False)
    print(f"\n[✓] Successfully saved master report to: {output_file}")
    print("=" * 50)

if __name__ == "__main__":
    # إنشاء مجلد تجريبي للملفات إن لم يكن موجوداً
    folder_name = "reports"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    combine_and_clean_excel(input_folder=folder_name, output_file="Master_Report.xlsx")