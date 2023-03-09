freeze:
	pip freeze --exclude-editable | grep -v "file:///" > requirements.txt

verify:
	isort --check-only .
	black --diff --check .
	flake8 .
	pytest .

clean:
	rm -r *.egg-info 2> /dev/null || true
	py3clean .