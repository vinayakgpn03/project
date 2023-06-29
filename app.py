from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def web():
    return render_template("/webpage.html")
@app.route('/register')
def reg():
    return render_template("/register.html")
if("__main__"==__name__):
    app.run()


