from flask import Flask, render_template, abort
import jsonloader
import random

app = Flask(__name__)

texts = ["Чем больше девушку ты любишь, тем больше лучше мы чем чем.", "Если будут трудности брат, забудь мой номер.", "ОООООО ПОГОДА НА УЛИЦЕ... УЖАСНА", "Кто это читает? (я)", "Если ты это читаешь то тебе повезло!"]


@app.route('/')
def index():
    news_data = jsonloader.loadjson()
    text_day = random.choice(texts)
    return render_template('index.html', all_news=news_data, ylala=text_day)

@app.route('/news/<int:news_id>')
def currentNews(news_id):
    all_news = jsonloader.loadjson()
    current_news = next((news for news in all_news if news['id'] == news_id), None)
    if current_news is None:
        return render_template('error404.html', error = news_id)
    return render_template('news.html', news = current_news)

if __name__ == '__main__':
    app.run(debug=True)