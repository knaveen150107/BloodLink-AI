from flask import Flask, render_template, request, redirect, url_for

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

# Home Page
@app.route("/")
def home():
    return render_template("home.html")

# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Validate user here

        return redirect(url_for("dashboard"))

    return render_template("login.html")


# Dashboard Page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Register Page
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        phone = request.form["phone"]
        blood_group = request.form["blood_group"]
        city = request.form["city"]
        role = request.form["role"]
        password = request.form["password"]

        print(fullname)
        print(email)
        print(phone)
        print(blood_group)
        print(city)
        print(role)

        return "Registration Successful"

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)