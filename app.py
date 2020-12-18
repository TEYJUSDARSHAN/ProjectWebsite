from flask import Flask,render_template,request,redirect
#from flask_sqlalchemy import SQLAlchemy
import imagecrawler as imgcrl

app = Flask(__name__)



post_list = [
    {
        'title' : 'my first post',
        'author' : 'teyjus darshan the great',
        'content' : 'hey that was a great post by the great one'
    },
    {
        'title' : 'my second post',
        'content' : 'hey that was a greatest post'
    }
]
@app.route('/home')
def homepage():
    return render_template('homepage.html')

@app.route('/image_crawler',methods = ['GET','POST'])
def crawler_page():
    if request.method == 'POST':
        number_of_images = request.form['number']
        keyword = request.form['keyword']
        imgcrl.download_images(int(number_of_images),keyword)
        return redirect('/image_crawler')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)