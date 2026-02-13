from flask import Flask, render_template, request
import os
import re
import zipfile
import smtplib
from email.message import EmailMessage
import subprocess

app = Flask(__name__)

def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def send_email(receiver, zip_file):
    sender = "paridhirastogi85@gmail.com"
    password = "qhjz zgrc bblk yoam"

    msg = EmailMessage()
    msg["Subject"] = "Your Mashup File"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Your mashup is attached.")

    with open(zip_file, "rb") as f:
        msg.add_attachment(f.read(), maintype="application",
                           subtype="zip", filename=zip_file)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

def create_dummy_mashup(output_name):
    # Replace with your real mashup logic
    with open(output_name, "w") as f:
        f.write("Mashup content")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            singer = request.form.get("singer", "").strip()
            videos = int(request.form.get("videos", 0))
            duration = int(request.form.get("duration", 0))
            email = request.form.get("email", "").strip()

            # Validation
            if not singer:
                return "Please enter a singer name", 400

            if videos <= 10:
                return "Number of videos must be more than 10", 400

            if duration <= 20:
                return "Duration must be more than 20 seconds", 400

            if not valid_email(email):
                return "Invalid email address", 400

            output_file = "mashup.mp3"
            create_dummy_mashup(output_file)

            zip_name = "mashup.zip"
            with zipfile.ZipFile(zip_name, "w") as zipf:
                zipf.write(output_file)

            send_email(email, zip_name)

            return "Mashup created and sent to email successfully!", 200

        except ValueError:
            return "Invalid input values. Please check your entries.", 400
        except Exception as e:
            return f"An error occurred: {str(e)}", 500

    return render_template("index.html")

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
