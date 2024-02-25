import get_advice

from flask import Flask, request, Response, stream_with_context
import json

app = Flask(__name__)

@app.route('/get-data', methods=['GET'])
def get_data():
    def generate():
        for chunk_delta in get_advice.generate_data():
            yield json.dumps({'content': chunk_delta}) + '\n'
    
    return Response(stream_with_context(generate()), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
