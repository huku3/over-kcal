from PIL import Image
import pyocr

tools = pyocr.get_available_tools()
tool = tools[0]

# print(tool.get_name())


# img01 = Image.open("images/01.png", "images/02.png")
img02 = Image.open("images/02.png")
img02.show()


txt = tool.image_to_string(img02, lang="eng+jpn", builder=pyocr.builders.TextBuilder())

print(txt)
