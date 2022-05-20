from flask import Flask
from flask import render_template
import pymysql
#import py <a href="https://www.796t.com/category.php?cid=18">Mysql</a>
'''
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run()
'''
app = Flask(__name__)


@app.route('/')
def index():
  conn = pymysql.connect(host='localhost', user='test123',
                         password='test123', db='aiotdb')
  cur = conn.cursor()
  sql = "SELECT `id`,`time`,`value`,`temp`,`humi`,`status` FROM sensors WHERE 1"
  cur.execute(sql)
  u = cur.fetchall()
  conn.close()
  return render_template('chart.html', u=u)  # index還沒改好


if __name__ == '__main__':
  app.debug = True
  app.run(port=8003)
