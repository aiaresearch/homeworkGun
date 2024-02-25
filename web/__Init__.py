import get_advice

from flask import Flask, request, Response, stream_with_context
import json

app = Flask(__name__)

@app.route('/get-data', methods=['GET'])
def get_data():
    get_advice.generate_data()

    for chunk in get_advice.response:
        yield json.dumps({'content': chunk.choices[0].delta}) + '\n'
    
    return Response(stream_with_context(get_advice.generate_data()), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)