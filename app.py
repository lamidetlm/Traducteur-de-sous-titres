from flask import Flask, request, jsonify, render_template
import os
import deepl

app = Flask(__name__)
DEEPL_API_KEY = "72b32559-af90-415c-b067-263afe926c82:fx"
translator = deepl.Translator(DEEPL_API_KEY)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_subtitles():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    target_lang = request.form.get('target_lang')
    
    if not file or file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not target_lang:
        return jsonify({'error': 'No target language specified'}), 400

    try:
        # Read and translate the subtitle content
        content = file.read().decode('utf-8')
        result = translator.translate_text(content, target_lang=target_lang)
        
        return jsonify({
            'translated_text': result.text,
            'source_lang': result.detected_source_lang
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
