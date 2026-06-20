from flask import Flask,render_template,request
import requests
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("app.html")


def ask_ai(user_message):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:1b",
            "prompt": user_message,
            "stream": False
        }
    )

    data = response.json()
    return data["response"]


@app.route("/submit", methods=["POST"])
		
def submit():
	user_message = request.form.get("message", "").lower();
	response = ask_ai(user_message)

	return render_template("app.html", user_message=user_message, bot_response=response)	


if __name__ == "__main__":
    app.run(debug=True)	
			
