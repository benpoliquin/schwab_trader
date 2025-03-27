.PHONY: setup install clean

setup:
	python3 -m venv venv
	@echo "Virtual environment created. Activate it with:"
	@echo "source venv/bin/activate  # On Unix/macOS"
	@echo "or"
	@echo ".\\venv\\Scripts\\activate  # On Windows"

install:
	pip install -r requirements.txt

run:
	python src/main.py

clean:
	rm -rf venv
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete 