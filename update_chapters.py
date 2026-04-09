import os
import json

def update_chapters():
    # 設定 CSV 資料夾路徑與輸出的 JSON 檔名
    data_folder = 'data'
    output_file = 'chapters.json'
    
    # 確保資料夾存在
    if not os.path.exists(data_folder):
        print(f"找不到資料夾: {data_folder}")
        return

    chapters = []
    
    # 掃描資料夾內的所有檔案
    # 我們按檔名排序，確保 Ch1, Ch2 順序正確
    files = sorted([f for f in os.listdir(data_folder) if f.endswith('.csv')])

    for filename in files:
        # 建立顯示名稱，例如 'list1.csv' -> 'Ch list1'
        # 你可以根據喜好修改這裡的命名邏輯
        chapter_id = filename.replace('.csv', '').replace('list', 'Ch')
        chapter_name = f"{chapter_id} 單字表"
        
        chapter_info = {
            "name": chapter_name,
            "url": f"{data_folder}/{filename}"
        }
        chapters.append(chapter_info)
        print(f"已偵測到: {chapter_name} ({filename})")

    # 寫入 JSON 檔案
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(chapters, f, indent=2, ensure_ascii=False)

    print(f"\n✅ 更新完成！共找到 {len(chapters)} 個章節。")
    print(f"結果已存入 {output_file}")

if __name__ == "__main__":
    update_chapters()