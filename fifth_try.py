import os

# 폴더 경로 설정
base_folder = "data_ssafy_collection_resized"  # 또는 원하는 경로
labels_folder = os.path.join(base_folder, "labels")
images_folder = os.path.join(base_folder, "images")

# 삭제 대상 개수 카운트
delete_count = 0

# 모든 .txt 파일 확인
for filename in os.listdir(labels_folder):
    if filename.endswith(".txt"):
        txt_path = os.path.join(labels_folder, filename)
        
        # 파일이 비어 있는지 확인
        if os.path.getsize(txt_path) == 0:
            # 대응 이미지 파일 이름
            image_name = os.path.splitext(filename)[0] + ".jpg"
            image_path = os.path.join(images_folder, image_name)

            # .txt 삭제
            os.remove(txt_path)
            print(f"[삭제됨] 라벨 파일: {txt_path}")

            # 이미지도 존재하면 삭제
            if os.path.exists(image_path):
                os.remove(image_path)
                print(f"[삭제됨] 이미지 파일: {image_path}")
            else:
                print(f"[경고] 이미지 없음: {image_path}")
            
            delete_count += 1

print(f"\n총 {delete_count}개의 빈 라벨 및 대응 이미지가 삭제되었습니다.")
