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

Step 6: Run the tests with Allure results:
pytest --browser chromium --alluredir=allure-results

Step 7: Generate Allure Report
allure generate allure-results --clean -o allure-report

Step 8: View Allure Report
allure open allure-report

Step 9: View downloaded Allure Report from GitHub actions
go to Downloads and decompress allure-report zip file
navigate to decompressed directory in terminal
run command: allure open .

Step 1o: Linting and Formatting
pip install flake8 black
flake8 path/to/your/code
black path/to/your/code

Step 11: Type Annotations
pip install mypy
mypy path/to/your/code

Step 12: Documentation
pip install sphinx
sphinx-quickstart