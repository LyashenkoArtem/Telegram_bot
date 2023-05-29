# define the name of the virtual environment directory
VENV := venv

# default target, when make executed without arguments
all: venv build docker-build

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

run: venv
	./$(VENV)/bin/python3 Da_bot/Da_bot.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	rm -r build dist

build:
	#mkdir -p distutils
	python3 setup.py sdist bdist

docker-build:
	docker build -t dabot:latest .

docker-run:
	docker run --env-file=secrets.env -it dabot:latest

.PHONY: all venv run clean build docker-build docker-run
