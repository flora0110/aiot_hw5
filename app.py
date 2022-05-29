from flask import Flask, render_template, jsonify
import pandas as pd
from six.moves import urllib
import json

app = Flask(__name__)

@app.route("/")
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
