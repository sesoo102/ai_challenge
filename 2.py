from PIL import Image
import os

# 폴더 경로
input_folder = "data_ssafy_collection(1000)"
output_folder = "data_ssafy_collection_resized"

# 출력 폴더 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 지원하는 이미지 확장자 목록
image_extensions = (".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG")  # 대소문자 모두 포함

# 모든 이미지 처리
for filename in os.listdir(input_folder):
    if filename.lower().endswith(image_extensions):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert("RGB")

        # 원본 크기
        orig_width, orig_height = img.size
        target_size = 640

        # 비율 유지 리사이즈
        ratio = min(target_size / orig_width, target_size / orig_height)
        new_width = int(orig_width * ratio)
        new_height = int(orig_height * ratio)

        img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # 패딩 추가
        new_img = Image.new("RGB", (target_size, target_size), (0, 0, 0))
        paste_x = (target_size - new_width) // 2
        paste_y = (target_size - new_height) // 2
        new_img.paste(img_resized, (paste_x, paste_y))

        # 리사이즈된 이미지 저장
        output_img_path = os.path.join(output_folder, filename)
        new_img.save(output_img_path, quality=95)

        # 대응하는 .txt 파일 처리
        img_name = os.path.splitext(filename)[0]
        input_txt_path = os.path.join(input_folder, f"{img_name}.txt")
        output_txt_path = os.path.join(output_folder, f"{img_name}.txt")

        # 패딩 및 리사이즈에 따른 좌표 변환
        new_width, new_height = 640, 640
        scaled_width = orig_width * ratio
        scaled_height = orig_height * ratio
        padding_x = (new_width - scaled_width) / 2
        padding_y = (new_height - scaled_height) / 2

        if os.path.exists(input_txt_path):
            # 기존 .txt 파일이 있으면 변환
            with open(input_txt_path, "r") as f_in, open(output_txt_path, "w") as f_out:
                for line in f_in:
                    data = line.strip().split()
                    if len(data) == 0:  # 빈 줄은 스킵
                        continue
                    class_id = int(data[0])
                    x_center = float(data[1])
                    y_center = float(data[2])
                    width = float(data[3])
                    height = float(data[4])

                    # 원본 좌표를 픽셀 단위로 변환
                    x_center_px = x_center * orig_width
                    y_center_px = y_center * orig_height
                    width_px = width * orig_width
                    height_px = height * orig_height

                    # 리사이즈 및 패딩 적용
                    x_center_scaled = x_center_px * ratio
                    y_center_scaled = y_center_px * ratio
                    width_scaled = width_px * ratio
                    height_scaled = height_px * ratio

                    x_center_new = (x_center_scaled + padding_x) / new_width
                    y_center_new = (y_center_scaled + padding_y) / new_height
                    width_new = width_scaled / new_width
                    height_new = height_scaled / new_height

                    new_line = f"{class_id} {x_center_new} {y_center_new} {width_new} {height_new}\n"
                    f_out.write(new_line)
        else:
            # .txt 파일이 없으면 빈 파일 생성
            with open(output_txt_path, "w") as f_out:
                pass
            print(f"빈 파일 생성: {output_txt_path}")

print("이미지 리사이징 및 라벨 처리 완료!")