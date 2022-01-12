# pip install pdfplumber でインストール
import pdfplumber as pp

# まずp4というフォルダを作る

# 意味は3ページから19ページ、22から23ページ...
target = (3, 19, 22, 23, 90, 91, 152, 163)

# 画質閾値、高いほど画質が良い
resolution = 196

# pdfを導入する
with pp.open('2201.pdf') as pdf:
    index = 0
    for i in range(target[0] - 1, target[1]):
        pdf.pages[i].to_image(resolution=resolution).save(f'p4/toki_{index}.png')
        index += 1
    index = 0
    for i in range(target[2] - 1, target[3]):
        pdf.pages[i].to_image(resolution=resolution).save(f'p4/shi_{index}.png')
        index += 1
    index = 0
    for i in range(target[4] - 1, target[5]):
        pdf.pages[i].to_image(resolution=resolution).save(f'p4/sasami_{index}.png')
        index += 1
    index = 0
    for i in range(target[6] - 1, target[7]):
        pdf.pages[i].to_image(resolution=resolution).save(f'p4/yokoku_{index}.png')
        index += 1
