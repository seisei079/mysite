from flask import Flask, render_template_string, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <h1>こんにちは</h1>
        <h2>これはクイズページだよ！！（答えは別ページにあるよ！）</h2>
        <p>今からポケモンクイズを出すから頑張って解いてみてね！！</p>
        <p>問題１ピカチュウは進化したら何になるでしょう！</p>
        <p>問題２ヒトカゲ　リザード　次は何のポケモンでしょう　</p>    
        <p>問題３ミミッキュの中身を見るとどうなるでしょう？</p>  
        <p>問題4ポケモンsvの一番最初の御三家はにゃおは、クワッス、誰でしょう？</p>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
