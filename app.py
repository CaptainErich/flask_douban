from flask import Flask,render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here 
    return render_template("index.html")

@app.route('/index.html')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/about_fengmian.html')
def about_fengmian():  # put application's code here
    return render_template("about_fengmian.html")

@app.route('/team.html')
def team():
    return render_template("team.html")

@app.route('/dongtai.html')
def dongtai():
    datalist = []
    con = sqlite3.connect("movie250.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
         datalist.append(item)
    cur.close()
    con.close()

    return render_template("dongtai.html", movies = datalist)

@app.route('/xueshu.html')
def xueshu():
    return render_template("xueshu.html")

@app.route('/echarts')
def echarts():
    return render_template("test/test_echart.html")


@app.route('/score')
def score():
    score = []
    num = []
    con = sqlite3.connect("movie250.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])

    cur.close()
    con.close()

    return render_template("test/test_echart.html", score = score,num=num)

if __name__ == '__main__':
    app.run()
