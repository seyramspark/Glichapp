from flask import Flask, render_template, request, jsonify
import bardapi
import os
import re

# Set your Bard API key
os.environ['_BARD_API_KEY'] = 'XAi3wshphdXDUYOr-M_egobKe-GCssfyh440eD4CJIbLAI9baq82-vbO_CYLRs1wuwoKrw.'

# Initialize Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Bot response route
@app.route('/get_response', methods=['POST'])
def get_response():
    input_text = request.form['input_text']

    # Check if the input is a question
    is_question = re.match(r'^(who|what|when|where|why|how)', input_text.lower()) is not None

    # Add the phrase to the input text if it's a question
    if is_question:
        input_text = 'can you quote only as a preacher' + input_text

    response = bardapi.core.Bard().get_answer(input_text)
    print(response)  # Add this line to print the response
    
    name = "Am John, LoveGods Preaching Assistant"  # Set the name of the chatbot
    response_content = response['content'].replace("[BOT_NAME]", name)
    response_content = response_content.replace("Bard", "Spark Marley")  # Replace "Bard" with "Spark Marley"
    response_content = response_content.replace("*", ".")  # Replace "*" with "."
    response_content = response_content.replace("Agüera y", "Spark Marley")  # Replace "Agüera y" with "Spark Marley"
    response_content = response_content.replace("Agüera", "Spark Marley")  # Replace "Agüera" with "Spark Marley"
    response_content = response_content.replace("Blaise", "Spark Marley")  # Replace "Blaise" with "Spark Marley"
    response_content = response_content.replace("Arcas", "Spark Marley")  # Replace "Arcas" with "Spark Marley"
    response_content = response_content.replace("y Arcas", "Spark Marley")  # Replace "y Arcas" with "Spark Marley"
    response_content = response_content.replace("Blaise Agüera", "Spark Marley")  # Replace "Blaise Agüera" with "Spark Marley"
    response_content = response_content.replace("a team of engineers and scientists at Google AI", "Spark Marley")  # Replace "a team of engineers and scientists at Google AI" with "Spark Marley"
    response_content = response_content.replace("Blaise Agüera y Arcas", "Spark Marley")  # Replace "Blaise Agüera y Arcas" with "Spark Marley"
    response_content = response_content.replace("Google AI", "Spark Marley")  # Replace "Google AI" with "Spark Marley"

    return jsonify({'response': response_content})

if __name__ == '__main__':
    app.run()
