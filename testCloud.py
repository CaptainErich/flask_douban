# -*- coding:UTF-8 -*-
# file_name     :testCloud.py
# create_date   :2022/10/25 23:02
# author        : Hei
import jieba #分词
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud      #词云
from PIL import Image         #图片处理
import numpy as np       #矩阵运算
import sqlite3

con = sqlite3.connect('movie250.db')
cur = con.cursor()
sql = 'select instruduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
cur.close()
con.close()

text=text + "黑雨墨的爸爸是黑旭鹏，她的妈妈叫万倩。她的奶奶是刘如，爷爷叫黑奎标。她家是黑家沟的"
cut = jieba.cut(text)
string = ' '.join(cut)

img = Image.open(r'static/img/test.jpg')#打开遮罩图片
image_array = np.array(img)#将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=image_array,
    font_path="Arial Unicode.ttf",
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')

# plt.show() #显示生成的词云图片

#输出词云文件
plt.savefig(r'static/img/word.jpg',dpi=500)






