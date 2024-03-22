# Importing libraries
from flask import Flask, render_template, request
from utils import load_model, chatbot
import re

# Initialize Flask app
app = Flask(__name__)

# Load the chatbot model from a file
model = load_model('chatbot_model.pkl')

# Index route to handle user interactions with the chatbot
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # Render the initial template if no question has been submitted yet
        return render_template('index.html', question='', answer='', chat_history='', source_documents='')
    if request.method == 'POST':
        # Get the user's question from the form
        user_question = request.form['user_question']
        
        # Get the chatbot response
        response = chatbot(user_question, model)
        
        # Extract relevant information
        question = response['question']
        answer = re.sub(r'[^\w\s]', '', response['answer']).strip()
        chat_history = response['chat_history']
        source_documents = response['source_documents']
        
        # Render the template with the response data
        return render_template('index.html', question=question, answer=answer,
                               chat_history=chat_history, source_documents=source_documents)

if __name__ == '__main__':
    # Run the Flask app with debugging enabled
    app.run(debug=True)