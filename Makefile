install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py invista/*.py core/*.py api/*.py
lint:
	# pylint - disable recommendations and configuratios
	pylint --disable=R,C *.py invista/*.py core/*.py api/*.py
test: 
	#pytest -m pytest -vv --cov=tests tests/*.py
build:
	docker-compose up
deploy:
	# deploy
all: install lint test deploy