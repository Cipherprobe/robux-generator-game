@echo off
echo Installing...
pip install -r requirements.txt --quiet
echo Preparing generator...
python main.py