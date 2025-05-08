from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # For now, just print to console (or save to file/database later)
    print(f"Message from {name} ({email}): {message}")
    
    return "Thank you for contacting us!"

if __name__ == '__main__':
    app.run(debug=True)