from flask import Flask, render_template, request

app = Flask(_name_)

def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return None

def get_bmi_category(bmi):
    if bmi is None:
        return "Invalid input"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        return render_template('index.html', bmi=bmi, category=category)
    except ValueError:
        return render_template('index.html', error="Please enter valid numbers")

if _name_ == '_main_':
    app.run(debug=True)