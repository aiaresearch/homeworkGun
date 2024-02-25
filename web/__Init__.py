import get_advice

from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/get-data')
def stream_response():
    def generate():
        for chunk in get_advice.response:
            yield f"data: {json.dumps(chunk.choices[0].delta)}\n\n"

    return Response(generate(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)