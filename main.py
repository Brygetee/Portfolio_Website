from operator import index
import smtplib
from flask import Flask, render_template, request

my_email = "python.course.email28@gmail.com"
my_password= "ouoy lmoc bibl cddh"

app= Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about_me')
def about_me():
    return render_template("about_me.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data= request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject: Contact me form submission from: {data["name"]}\n\n{data["message"]}\n\n{data["name"]}\n{data["email"]}\n{data["phone"]}"
            )
        return render_template("contact.html", msg_sent = True)

    return render_template("contact.html", msg_sent = False)



if __name__ == '__main__':
    app.run(debug=True)