from flask import Flask, render_template, request

app = Flask(__name__)

def get_advice(symptoms):
    symptoms = symptoms.lower()

    if "fever" in symptoms:
        return "You may have an infection. Stay hydrated and consult a doctor."
    elif "headache" in symptoms:
        return "It could be stress or dehydration. Rest and drink water."
    elif "cough" in symptoms:
        return "Possible cold or allergy. Monitor symptoms."
    else:
        return "Please consult a healthcare professional for accurate advice."

@app.route("/", methods=["GET", "POST"])
def home():
    advice = ""
    if request.method == "POST":
        symptoms = request.form.get("symptoms")
        advice = get_advice(symptoms)

    return render_template("index.html", advice=advice)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
