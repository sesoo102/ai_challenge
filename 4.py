import os
import shutil

# 원본 폴더 경로
source_folder = "data_ssafy_collection_resized"  # 또는 "data_ssafy_collection(1000)" 등
images_folder = os.path.join(source_folder, "images")
labels_folder = os.path.join(source_folder, "labels")

# 폴더가 없으면 생성
os.makedirs(images_folder, exist_ok=True)
os.makedirs(labels_folder, exist_ok=True)

# 파일 분류
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)
    if os.path.isfile(file_path):
        if filename.lower().endswith(".jpg"):
            shutil.move(file_path, os.path.join(images_folder, filename))
        elif filename.lower().endswith(".txt"):
            shutil.move(file_path, os.path.join(labels_folder, filename))

print("이미지와 라벨 파일 분류 완료!")
