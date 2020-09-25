echo "Running tests..." &&
pytest
echo "Running create_readme.py..." &&
black . --exclude venv/ &&
python3 create_readme.py
