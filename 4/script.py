from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
# everything in parenthesis becomes the address of the webpage specifically
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

#The HTML files are templates and should be put in a separate folder called templates at the same location

if __name__=="__main__":
    app.run(debug=True)