from flask import Flask, request, send_file
from sendPrompt import prompt
from processData import processData
from scrapeImage import scrapeImages
from createPowerpoint import createPPT

app = Flask(__name__)

@app.route('/create-presentation', methods=['POST'])
def create_presentation_endpoint():
    data = request.json
    material = data.get('material')
    number = data.get('number')

    response_text = prompt(material, number)
    items, images = processData(response_text)

    scrapeImages(images)
    createPPT(items)

    return send_file('presentation.pptx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)