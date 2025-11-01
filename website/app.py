from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ram = request.form.get('ram')
        weight = request.form.get('weight')
        print(f"RAM: {ram}")
        print(f"Weight: {weight}")
        # You can add prediction logic here and pass result to template
        return render_template("index.html", ram=ram, weight=weight)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)