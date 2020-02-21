# -*- coding: utf-8 -*-

from teste_flask import app

if __name__ == '__main__':
	app.run('0.0.0.0', port=5000, debug=True, use_reloader=True)
