from flask import Flask,render_template,redirect,request

#__name__==__main__
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/about')
def about():



if __name__=='__main__':
    #app.debug = True
    app.run(debug=True)