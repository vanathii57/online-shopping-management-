from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'swathi@vanathi2005',
    'database': 'online_shop_db'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    name = request.args.get('name')
    email = request.args.get('email')
    return render_template('home.html', name=name, email=email)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Corrected this part
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, message))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect("/home")
    return render_template("contact.html")

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('home', name=name, email=email))

@app.route('/contact-submit', methods=['POST'])
def contact_submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    contactscol_value = "Default info"  # Replace with dynamic input if needed

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contacts (name, email, message, contactscol) VALUES (%s, %s, %s, %s)",
        (name, email, message, contactscol_value)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/contact')


@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
