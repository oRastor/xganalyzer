build:
	rm dist/*
	python3 -m build

upload:
	python3 -m twine upload --repository pypi dist/*

test:
	coverage run -m unittest tests/test_game_events_aggregator.py && coverage html