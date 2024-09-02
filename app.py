from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/guide')
def guide():
    return render_template('guide.html')

@app.route('/packages')
def packages():
    return render_template('packages.html')

@app.route('/insurance')
def insurance():
    return render_template('insurance.html')

@app.route('/plan')
def plan():
    return render_template('plan.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        feedback_text = request.form.get('feedback')
        # Process the feedback (e.g., save it to a file or send an email)
        print(f"Feedback received: {feedback_text}")  # For debugging
        return redirect(url_for('feedback_success'))
    return render_template('feedback.html')

@app.route('/feedback_success')
def feedback_success():
    return "Thank you for your feedback!"

if __name__ == '__main__':
    app.run(debug=True)
