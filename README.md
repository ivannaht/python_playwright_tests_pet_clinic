Step 1: Create a requirements.txt File
* Create a new file named requirements.txt.
touch requirements.txt

Step 2: Freeze Current Dependencies
pip freeze > requirements.txt

Step 3: Install Dependencies from requirements.txt
pip install -r requirements.txt

Step 4: Create the YAML file from GitHub Actions
Save the YAML content to a file named python-app.yml.

Step 5: Install Allure dependencies
pip install allure-pytest
