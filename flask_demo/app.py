from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")

# SQLite config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:pass@localhost/dbname"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)

# Create tables once
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html", tasks=Task.query.all())

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("task", "").strip()
    if title:
        db.session.add(Task(title=title))
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    Task.query.filter_by(id=task_id).delete()
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
