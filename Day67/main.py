from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


# 🔹 MODEL
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)


# 🔹 HOME
@app.route("/")
def home():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


# 🔹 VIEW POST
@app.route("/post/<int:id>")
def show_post(id):
    post = Post.query.get_or_404(id)
    return render_template("post.html", post=post)


# 🔹 ADD POST
@app.route("/add", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")

        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html")


# 🔹 EDIT POST
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_post(id):
    post = Post.query.get_or_404(id)

    if request.method == "POST":
        post.title = request.form.get("title")
        post.content = request.form.get("content")
        db.session.commit()

        return redirect(url_for("show_post", id=post.id))

    return render_template("edit.html", post=post)


# 🔹 DELETE POST
@app.route("/delete/<int:id>")
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("home"))


# 🔹 RUN
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)