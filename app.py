from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/lookupParts", methods=["GET"])
def lookup_parts():
    make = request.args.get("make")
    model = request.args.get("model")
    year = request.args.get("year")
    part = request.args.get("partName")

    # 🔧 Replace with real scraping logic
    sample_results = {
        "parts": [
            {"name": part, "partNumber": "XYZ123", "priceCAD": 89.99, "vendor": "Performance Auto Parts"},
            {"name": part, "partNumber": "XYZ123-B", "priceCAD": 92.49, "vendor": "NAPA Auto Parts"}
        ]
    }

    return jsonify(sample_results)

if __name__ == "__main__":
    app.run(debug=True)
