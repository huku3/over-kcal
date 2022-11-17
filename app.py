from PIL import Image
import pyocr
import csv
import glob
import pyocr.builders


tools = pyocr.get_available_tools()
tool = tools[0]

# print(tool.get_name())


# img01 = Image.open("images/01.png", "images/02.png")
# img = Image.open("images/05.png")
# img02.show()


def image_to_text(file_path):
    txt = tool.image_to_string(
        Image.open(file_path),  # OCRする画像
        lang="eng",  # 学習済み言語データ
        builder=pyocr.builders.TextBuilder(),  # 期待される出力のタイプを指定
    )

    return txt


def main():
    file_paths = glob.glob("images/*")

    for file_path in file_paths:
        txt = image_to_text(file_path)

    print(txt)
    with open("sample.txt", mode="w") as f:
        f.writelines(txt)


# print(f.read())
# f.close()

if __name__ == "__main__":
    main()
