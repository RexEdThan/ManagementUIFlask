from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
  
app = Flask(__name__) 

#app.config['SQLALCHEMY_DATABASE_URI']

@app.route("/")
def view_dashboard():
    return render_template("index.html", title="Dashboard", active="dashboard")

@app.route("/ticket")
def view_tickets():
    return render_template("ticket.html", title="Tickets", active="tickets")

@app.route("/history")
def view_history():
    return render_template("history.html", title="History", active="history")

@app.route("/email")
def view_email():
    return render_template("email.html", title="Email", active="email")

@app.route("/profile")
def view_profile():
    return render_template("profile.html", title="Profile", active="profile")

@app.route("/setting")
def view_setting():
    return render_template("setting.html", title="Setting", active="setting")

if __name__ == '__main__':
    app.run(debug=True)
