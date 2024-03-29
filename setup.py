import subprocess

# Stop on error.
subprocess.run(['set', '-o', 'errexit'], check=True)

# Updating pip version on original environment.
subprocess.run(['pip', 'install', '-U', 'pip'], check=True)

# Installing virtualenv.
subprocess.run(['pip', 'install', 'virtualenv==20.11.2'], check=True)

# Creating virtual environment.
subprocess.run(['virtualenv', '-p', 'python3.9', '../system-env'], check=True)

# Move wheel into virtual environment.
subprocess.run(['mv', './dlib-19.22.99-cp39-cp39-win_amd64.whl', '../system-env/Lib/site-packages'], check=True)

# Activating virtual environment.
subprocess.run(['source', '../system-env/Scripts/activate'], check=True)

# Installing dlib wheel.
subprocess.run(['pip', 'install', '../system-env/Lib/site-packages/dlib-19.22.99-cp39-cp39-win_amd64.whl'], check=True)

# Updating pip version in the virtual environment.
# This requires admin privilege, hence commented out for now.

# Installing system requirements.
subprocess.run(['pip', 'install', '-r', '../requirements.txt'], check=True)

# Displaying installed requirements.
print("THE FOLLOWING REQUIREMENTS HAVE NOW BEEN INSTALLED")
subprocess.run(['pip', 'freeze'])

print("\nStarting System Now.")

# Run Main File
subprocess.run(['python', '../main.py'])
