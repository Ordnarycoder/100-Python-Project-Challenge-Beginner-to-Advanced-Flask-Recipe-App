from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("recipe.html")  # templates/ kısmını kaldırdık

if __name__ == '__main__':
    app.run()
