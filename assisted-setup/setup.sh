# Stop on error.
set -o errexit

# Updating pip version on original environment.
pip install -U pip

# Installing virtualenv.
pip install virtualenv==20.11.2

# Creating virtual environment.
virtualenv -p python3.9 "../system-env"

# Move wheel into virtual environment..... CHANGE FROM COPY TO MOVE LATER.
cp "./dlib-19.22.99-cp39-cp39-win_amd64.whl" "../system-env/Lib/site-packages"

# Activating virtual environment.
source ../system-env/Scripts/activate

# Installing dlib wheel.
pip install ../system-env/Lib/site-packages/dlib-19.22.99-cp39-cp39-win_amd64.whl

# Updating pip version in the virtual environment.
# pip install -U pip
# This requires admin priviledge hence commented out for now.

# Installing system requirements.
pip install -r ../requirements.txt

# Displaying installed requirements.
echo "THE FOLLOWING REQUIREMENTS HAVE NOW BEEN INSTLLED"
pip freeze
echo ""
echo "Starting System Now."

# Run Main File
python ../main.py