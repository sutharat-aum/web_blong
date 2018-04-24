from flask import Flask, render_template

import src.getTwitter as gtw
import src.classicfly as classicfly

app = Flask(__name__)
start = classicfly.start_train()

@app.route('/')
def home_template():  # def  เป็นคำสำคัญสำหรับการสร้างฟังก์ชัน
    return render_template('homepage.html')


# @app.route('/search')
# def search_template():  # def  เป็นคำสำคัญสำหรับการสร้างฟังก์ชัน
#     return render_template('search.html')


@app.route('/search/<input_keyword>')
def search_keyword(input_keyword):  # def  เป็นคำสำคัญสำหรับการสร้างฟังก์ชัน
    emoHappy = []
    emoSad = []
    emoLove = []
    emoHate = []
    emoFun = []
    emoWorry = []
    client = gtw.twitterClient()
    tweet = client.getSearchTweets(query=input_keyword, count=20)
    for tt in tweet:
        tweetStr = classicfly.processTweet(tt)
        tweetStr = classicfly.processClaer(tweetStr)
        classicflyStr = classicfly.classify_String(tweetStr,start)
        if classicflyStr == 'happiness':
            emoHappy.append(tt)
        elif classicflyStr == 'sadness':
            emoSad.append(tt)
        elif classicflyStr == 'love':
            emoLove.append(tt)
        elif classicflyStr == 'hate':
            emoHate.append(tt)
        elif classicflyStr == 'fun':
            emoFun.append(tt)
        elif classicflyStr == 'worry':
            emoWorry.append(tt)
        else:
            print('err')

    if emoHappy.__len__()==0  :
        emoHappy.append("No message")
    if emoSad.__len__()==0  :
        emoSad.append("No message")
    if emoLove.__len__()==0 :
        emoLove.append("No message")
    if emoHate.__len__()==0 :
        emoHate.append("No message")
    if emoFun.__len__()==0 :
        emoFun.append("No message")
    if emoWorry.__len__()==0 :
        emoWorry.append("No message")


    return render_template('search_result.html',emoHappy=emoHappy,emoSad=emoSad,emoLove=emoLove,emoHate=emoHate,emoFun=emoFun,emoWorry=emoWorry )


# @app.route('/overview')
# def overview_template():  # def  เป็นคำสำคัญสำหรับการสร้างฟังก์ชัน
#     return render_template('overview.html')


@app.route('/overview/<input_keyword>')
def overview_keyword(input_keyword):  # def  เป็นคำสำคัญสำหรับการสร้างฟังก์ชัน
    pieHappy = 0
    pieSad = 0
    pieLove = 0
    pieHate = 0
    pieFun = 0
    pieWorry = 0
    client = gtw.twitterClient()
    tweet = client.getSearchTweets(query=input_keyword, count=100)
    for tt in tweet:
        tweetStr = classicfly.processTweet(tt)
        tweetStr = classicfly.processClaer(tweetStr)
        classicflyStr = classicfly.classify_String(tweetStr, start)
        if classicflyStr == 'happiness':
            pieHappy += 1
        elif classicflyStr == 'sadness':
            pieSad += 1
        elif classicflyStr == 'love':
            pieLove += 1
        elif classicflyStr == 'hate':
            pieHate += 1
        elif classicflyStr == 'fun':
            pieFun += 1
        elif classicflyStr == 'worry':
            pieWorry += 1
        else:
            print('err')

    return render_template('overview_result.html', keyword=input_keyword,pieHappy=pieHappy,pieSad=pieSad,pieLove=pieLove,pieHate=pieHate,pieFun=pieFun,pieWorry=pieWorry)


# @app.route('/piechart')
# def piechart_template():  # def  เป็นคำสำคัญสำหรับการสร้างฟังก์ชัน
#     return render_template('piechart.html')


if __name__ == '__main__':
    app.run(port=4995, debug=True)
    # app.run(host= '10.10.100.65',port=4995, debug=True)
