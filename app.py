from PIL import Image
import pyocr
import csv
import glob
import datetime
import pyocr.builders
import os


tools = pyocr.get_available_tools()
tool = tools[0]

# print(tool.get_name())


# img01 = Image.open("images/01.png", "images/02.png")
# img = Image.open("images/05.png")
# img02.show()


def image_to_text(file_path):
    txt = tool.image_to_string(
        Image.open(file_path),  # OCRする画像
        lang="jpn",  # 学習済み言語データ
        builder=pyocr.builders.DigitBuilder(tesseract_layout=6),  # 期待される出力のタイプを指定
    )

    return txt


def main():
    file_paths = glob.glob("images/*")
    to_dir = "outputs"

    for file_path in file_paths:
        txt = image_to_text(file_path)

        filename = os.path.splitext(os.path.basename(file_path))[0]
        # 出力先のパスの生成
        to_path = os.path.join(to_dir, filename + ".txt")

        with open(to_path, mode="w") as f:
            f.writelines(txt)


# print(f.read())
# f.close()
def read():
    file_paths2 = glob.glob("outputs/*")
    a = []
    for file_path2 in file_paths2:
        with open(file_path2, mode="r") as f:
            s = f.read()
            s = int(s)
            a.append(s)
    sum_number = 0
    for r in range(0, len(a)):
        number = int(a[r])
        sum_number += number
    return sum_number


def text():
    now = datetime.datetime.now()
    d = now.date().strftime("%Y/%m/%d")
    print(f"{d}の摂取カロリーは{read()}kcalです。")


if __name__ == "__main__":
    main()
    text()
