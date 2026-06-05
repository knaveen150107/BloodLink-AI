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
@app.route("/login")
def login():
    return render_template("login.html")

# Register Page
@app.route("/register")
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