import pymupdf
import glob
import os

# 대상 폴더 (역슬래시 대신 슬래시 사용)
target_dir = "C:/Users/dwigh/slides/images/aml/aml-note/"

# dpi를 높이면 더 선명해집니다 (200~300 추천)
DPI = 300

pdf_files = glob.glob(os.path.join(target_dir, "*.pdf"))

if not pdf_files:
    print(f"'{target_dir}' 안에 pdf 파일이 없습니다.")

for pdf_path in pdf_files:
    pdf_path = pdf_path.replace("\\", "/")
    png_path = pdf_path[:-4] + ".png"  # 확장자만 .pdf -> .png로 교체

    doc = pymupdf.open(pdf_path)

    if len(doc) == 1:
        # 페이지가 한 장이면 파일명 그대로 저장
        page = doc[0]
        pix = page.get_pixmap(dpi=DPI)
        pix.save(png_path)
        print(f"저장 완료: {png_path}")
    else:
        # 페이지가 여러 장이면 각 페이지를 _1, _2... 로 구분해서 저장
        base = png_path[:-4]  # ".png" 제거한 부분
        for i, page in enumerate(doc, start=1):
            pix = page.get_pixmap(dpi=DPI)
            out_path = f"{base}_{i}.png"
            pix.save(out_path)
            print(f"저장 완료: {out_path}")

    doc.close()

print("모든 변환이 끝났습니다.")