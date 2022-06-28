build:
	rm dist/*
	python3 -m build

upload:
	python3 -m twine upload --repository pypi dist/*

test:
	coverage run -m unittest tests/test_game_events_aggregator.py tests/test_season_game_aggregator.py tests/test_final_aggregator.py && coverage html