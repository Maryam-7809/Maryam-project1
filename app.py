from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send-sticker', methods=['POST'])
def send_sticker():
    data = request.json
    # Process your data here
    return jsonify({'status': 'success'}), 200

# Additional routes and logic
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
