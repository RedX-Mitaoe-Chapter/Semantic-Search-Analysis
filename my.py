from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form.get("input")
        return redirect(url_for("user",usr=user))
        print(user)
    else:
        return render_template("index.html")
        print(user)

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"
    print(user)

if __name__ == '__main__':
    app.run()
