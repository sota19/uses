from flask import Flask, render_template, request, make_response
from datetime import datetime


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index1():
    if request.method == 'POST':
        a = request.form.get('a')
        b = request.form.get('b')
        c = request.form.get('c')
        d = request.form.get('d')
        time = datetime.now().strftime('%H:%M')
        total = int(100*(float(a) + float(b) + float(c) + float(d)) / 40)
        return render_template('index2.html', a=a, b=b, c=c, d=d, time=time, total=total)
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)
