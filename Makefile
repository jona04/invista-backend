install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt


format:
	# format the code

lint:
	# flake8 or pylint

test: 
	# test

deploy:
	# deploy

all: install lint test deploy