from flask import Flask

app = Flask(__name__)
languages = [{'name':'hey'}]
@app.route('/lang', methods=['GET'])

def returnn():
	return jsonify({'languages': languages})


if __name__=='__main__':
	app.run(debug=True, port = 5000)