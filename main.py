from googletrans import Translator
import random
from flask import Flask,  request, render_template
import requests
import json
app = Flask(__name__)

translator = Translator(service_urls=[
    'translate.google.cn'
])
ptlan = ['en', 'ru', 'es', 'fr', 'ja', 'ko', 'zh-CN']
alllan = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-CN', 'zh-tw', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku',
          'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu', 'fil', 'he']


@app.route('/', methods=['GET'])
def hello_world():
    return render_template("index.html")


@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        raw = request.form['text']
        count = int(request.form['count'])
        low = "true" in request.form['low']
        # print(request.form)
        fynr = []
        if count > 50:
            count = 1
        lan = ""
        rres = {"state": 0}
        if translator.detect(raw).lang != "zh-CN":
            res = translator.translate(raw, dest='zh-CN').text
            lan = "zh-CN"
            fynr.append(res)
        else:
            res = translator.translate(raw, dest='en').text
            lan = "en"
            fynr.append(res)
        if count-2 > 0:
            for _ in range(count-2):
                if low:
                    cache = ptlan.copy()
                else:
                    cache = alllan.copy()
                cache.remove(lan)
                # print(i, lan)
                s = random.randint(0, len(cache)-2)
                res = translator.translate(res, dest=cache[s]).text
                lan = cache[s]
                fynr.append(res)
        if lan != "zh-CN":
            res = translator.translate(res, dest='zh-CN').text
            fynr.append(res)
        # print(res, fynr)
        rres["res"] = res
        rres["process"] = fynr
        return rres


if __name__ == '__main__':
    app.run(port=4586, debug=True)      # 设置debug=True是为了让代码修改实时生效，而不用每次重启加载
