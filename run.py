from flask import Flask
import os
from app import server


if __name__ == '__main__':
	# app.run()
	port = int(os.environ.get("PORT", 8000))
	server.run(host='0.0.0.0', port=port)

