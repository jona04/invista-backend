install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py invista/*.py core/*.py api/*.py
lint:
	# flake8 or pylint
test: 
	# test
deploy:
	# deploy
all: install lint test deploy