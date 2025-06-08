import os

# 이미지 폴더 경로
folder = "data_ssafy_collection(1000)"

# 모든 이미지 파일 확인
for filename in os.listdir(folder):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        # 이미지 파일 이름에서 확장자 제거
        img_name = os.path.splitext(filename)[0]
        txt_path = os.path.join(folder, f"{img_name}.txt")

        # 이미 .txt 파일이 없으면 빈 파일 생성
        if not os.path.exists(txt_path):
            with open(txt_path, "w") as f:
                pass  # 빈 파일로 생성
            print(f"빈 파일 생성: {txt_path}")
        else:
            print(f"이미 존재: {txt_path}")

print("모든 이미지에 대한 .txt 파일 생성 완료!")