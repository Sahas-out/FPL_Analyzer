#!/bin/bash
python3 fpl.py
python3 fixtures_stats.py
cd fixtures
python3 data_sorter.py
cd ..
python3 predictions.py
python3 clean_predictions.py
python3 top_players.py
python3 create_best11.py
