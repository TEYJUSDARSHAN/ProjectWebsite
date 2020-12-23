from flask import Flask,render_template,request,redirect
#from flask_sqlalchemy import SQLAlchemy
import imagecrawler as imgcrl
#import NLPlyrics as lyrics

app = Flask(__name__)



post_list = [
    {
        'title' : 'my first post',
        'author' : 'teyjus darshan the great',
        'content' : 'hey that was a great post by the great one'
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
        return redirect('/image_crawler/downloads')
    else:
        return render_template('index.html')

@app.route('/image_crawler/downloads')
def download_page():
    return render_template('crawler_download.html')

@app.route('/NLP_model',methods = ['POST','GET'])
def songlyrics():
    if request.method == 'POST':
        number_of_needed_words = request.form['number']
        initial_sent = request.form['sentence']
        #predicted_text = lyrics.writelyrics(number_of_needed_words,intital_sent)
        return render_template('/lyricsresult.html',display_text = 'predicted_text')
    else:
        return render_template('NLP.html')



if __name__ == '__main__':
    app.run(debug=True)