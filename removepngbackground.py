from PIL import Image
import glob
import os

# 대상 폴더 (역슬래시 대신 슬래시 사용)
target_dir = "C:/Users/dwigh/slides/images/general/"

# 이 값보다 밝은(흰색에 가까운) 픽셀을 전부 투명하게 처리합니다.
# 255 = 완전한 흰색만 제거, 240 정도로 낮추면 살짝 회색빛이 도는 "거의 흰색"도 같이 제거됩니다.
THRESHOLD = 240


def remove_white_background(input_path: str, output_path: str, threshold: int = THRESHOLD):
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for r, g, b, a in datas:
        if r >= threshold and g >= threshold and b >= threshold:
            new_data.append((r, g, b, 0))  # 알파값 0 = 완전 투명
        else:
            new_data.append((r, g, b, a))

    img.putdata(new_data)
    img.save(output_path, "PNG")


if __name__ == "__main__":
    # png_files = glob.glob(os.path.join(target_dir, "*.png"))
    png_files = [target_dir + "bs_05_c.png", target_dir + "PRISM.png", target_dir + "sswu_logo.jpeg"]

    if not png_files:
        print(f"'{target_dir}' 안에 png 파일이 없습니다.")

    for path in png_files:
        path = path.replace("\\", "/")
        remove_white_background(path, path)  # 같은 파일에 덮어쓰기
        print(f"배경 제거 완료: {path}")

    print("모든 작업이 끝났습니다.")