from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def calculator():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result =  num1 + num2
        elif operation == 'sub':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'division':
            result = num1/num2

        else:
            result = "Invalid Operation"

        return render_template('calculate.html', result=result)
    
    return render_template('calculate.html', result=None)


if __name__ == '__main__':
    app.run(debug=True)
