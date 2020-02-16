sudo apt-get update

mkdir location_app/app/databases

sudo apt-get install python3-venv
python3 -m venv location_app/venv

cd location_app
. venv/bin/activate
pip install -r requirements.txt