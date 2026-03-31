from flask import Flask, request, jsonify

app = Flask(__name__)

# --- ROOT ROUTE ---
@app.route("/", methods=["GET"])
def home():
    return "✅ Flask API is working on Vercel"

# --- TEST ROUTE ---
@app.route("/api/test", methods=["GET"])
def test():
    return jsonify({"status": "success", "message": "API is working"})

# --- MAIN ANALYZE ROUTE ---
@app.route("/api/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        topic = data.get("topic")

        if not topic:
            return jsonify({"error": "No topic provided"}), 400

        # 🔥 TEMP TEST RESPONSE (replace later with your AI logic)
        return jsonify({
            "status": "success",
            "result": f"Analysis for: {topic}"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# --- LOCAL RUN ---
if __name__ == "__main__":
    app.run(debug=True)