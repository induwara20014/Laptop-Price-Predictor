from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        ram = request.form.get('ram')
        weight = request.form.get('weight')
        company = request.form.get('company')
        typename = request.form.get('typename')
        opsys = request.form.get('opsys')
        cpu = request.form.get('cpuname')
        gpu = request.form.get('gpuname')
        touchscreen = request.form.get('touchscreen')
        ips = request.form.get('ips')

        print(ram, weight, company, typename, opsys, cpu, gpu, touchscreen, ips)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
 