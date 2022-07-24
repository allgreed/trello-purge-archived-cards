setup:
	python3 -m venv env
	. env/bin/activate; pip install trello

run:
	. env/bin/activate; python main.py
