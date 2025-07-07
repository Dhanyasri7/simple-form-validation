from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            return "❌ Error: All fields must be filled!", 400
        elif '@' not in email:
            return "❌ Error: Email must contain '@'!", 400
        else:
            print("\n--- Received Data ---")
            print("Name:", name)
            print("Email:", email)
            return "✅ Success: Data received by Python!"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
