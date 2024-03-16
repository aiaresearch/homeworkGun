import get_advice

from flask import Flask, request, Response, stream_with_context
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/get-data', methods=['GET'])
def get_data():
    def generate():
        for chunk_delta in get_advice.generate_data():
            yield json.dumps({'content': chunk_delta}) + '\n'
    
    return Response(stream_with_context(generate()), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
