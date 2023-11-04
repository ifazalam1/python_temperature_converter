from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def temperature_converter():
    result = ""
    result_unit = ""
    if request.method == "POST":
        temperature = request.form["temperature"]
        unit = request.form["unit"]
        if unit == "celsius":
            result = str(celsius_to_fahrenheit(
                float(temperature))) + "° Fahrenheit"
        else:
            result = str(fahrenheit_to_celsius(
                float(temperature))) + "° Celsius"
    return render_template("index.html", result=result, result_unit=result_unit)


if __name__ == "__main__":
    app.run(debug=True)
