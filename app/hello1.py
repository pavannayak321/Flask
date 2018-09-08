from flask import Flask,render_template,request
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('student.html')


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/about/')
def about_page():
    return render_template('about.html')

@app.route('/layout/')
def layout_page():
    return render_template('layout.html')


@app.route('/hello/<int:score>')
def hello_nam(score):
    
    return render_template('hello.html',marks=score)
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        result=request.form
        return render_template("result.html",result=result)


if __name__ == '__main__':
    app.run(debug=True)
