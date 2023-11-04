from flask import Flask, render_template, request

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius



@app.route("/", methods=["GET", "POST"])
def temperature_converter():
    result = ""
    result_unit = ""
    if request.method == "POST":
        temperature = request.form["temperature"]
        unit = request.form["unit"]
        if unit == "celsius":
            result = celsius_to_fahrenheit(float(temperature))
            result_unit = "Fahrenheit"
        else:
            result = fahrenheit_to_celsius(float(temperature))
            result_unit = "Celsius"
    return render_template("index.html", result=result, result_unit=result_unit)


if __name__ == "__main__":
    app.run(debug=True)
