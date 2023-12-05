import urllib.parse
from flask import Flask, request, jsonify
import requests
import subprocess

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def tts():
    try:
        data = request.json
        text = data.get('text', 'Hello, world!')
        # Encode the text for the query parameter
        encoded_text = urllib.parse.quote(text)
   
        command = f'curl -s "https://api.streamelements.com/kappa/v2/speech?voice=Brian&text={encoded_text}" | mpg123 -'
        subprocess.run(command, shell=True, check=True)
        return jsonify({'message': 'Audio played successfully'})

        return jsonify({'error': 'Failed to fetch TTS data'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)






