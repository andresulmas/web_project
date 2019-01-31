from src.app import app

__author__ = 'jslvtr'

app.run(debug=app.config['DEBUG'], port=5000)
