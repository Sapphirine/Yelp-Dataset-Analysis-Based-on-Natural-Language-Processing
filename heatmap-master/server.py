import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

DATABASEURI = "postgresql://zw2423:1231@35.196.90.148/proj1part2"
#
# This line creates a database engine that knows how to connect to the URI above.
#
engine = create_engine(DATABASEURI)
metadata = MetaData(bind=engine)
cuisine = Table('cuisine',metadata,autoload=True)

@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request.

  The variable g is globally accessible.
  """
  try:
    g.conn = engine.connect()
  except:
    print ("uh oh, problem connecting to database")
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't, the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass



app = Flask(__name__)
'''
def return_img_stream(img_local_path):  
    """ 
    工具函数: 
    获取本地图片流 
    :param img_local_path:文件单张图片的本地绝对路径 
    :return: 图片流 
    """  
    import base64  
    img_stream = ''  
    with open(img_local_path,encoding='utf-16','r') as img_f:  
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream)  
    return img_stream  
'''
@app.route('/')
def index():
	#img_path = '/Users/mingzhixu/Documents/Study/Bigdata/finalproject/code/rf/heatmap-master/templates/pic/yelplogo.jpg'
	#img_stream = return_img_stream(img_path)
	return render_template('index.html')  




@app.route('/heatmap', methods=['POST'])
def heatmap():
    return render_template('heatmap.html')

@app.route('/popular', methods=['POST'])
def popular():
    return render_template('popular.html')

@app.route('/prediction', methods=['POST'])
def prediction():
	return render_template('prediction.html')

@app.route('/evaluation', methods=['POST'])
def evaluation():
	return render_template('evaluation.html')


@app.route('/api/v1/<event>')
def event_handler(event, methods=['POST']):
    with open('events/sample.json', 'r') as container:
        data = container.read()

    return data



if __name__ == '__main__':
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=5000, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using:

        python server.py

    Show the help text using:

        python server.py --help

    """

    HOST, PORT = host, port
    print("running on %s:%d" % (HOST, PORT))
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


  run()