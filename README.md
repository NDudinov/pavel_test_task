This is a test task.

To run this locally you need
1. Install poetry https://python-poetry.org:

    * for  Linux, Mac, WSL: 
`curl -sSL https://install.python-poetry.org | python3 -
` 

    * for Windows (PowerShell):

    `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    `


2. Add poetry to PATH
   * `$HOME/.local/bin` on Unix.
   * `%APPDATA%\Python\Scripts` on Windows.
   * `$POETRY_HOME/bin` if `$POETRY_HOME` is set.


3. Install dependencies 

    Enter `poetry install` to install dependencies

    Enter `poetry shell` to enter poetry shell

    Enter `playwright install` to install playwright browser instances


4. Run tests using `pytest`

   You can use flags 

   * `--headless=True` to run UI tests in headless mode. By default, UI tests are run in headed mode
   * `--br=chrome` to specify browser. By default, UI tests are run in chromium. Available browsers are `firefox` for Mozilla Firefox (and similar) and `webkit` for Safari (and other webkit browsers)


5. Allure reports

   Every run will generate allure report in ./allure-results   

   To view you need to install allure

   https://allurereport.org/docs/gettingstarted/installation/

   Use homebrew (Mac): `brew install allure`
   
   Scoop (Windows) `scoop install allure`
   
   or Linux package manager `sudo dpkg -i allure_2.24.0-1_all.deb` or `sudo rpm -i allure_2.24.0-1.noarch.rpm`

   depending on your system

   You can install from downloaded archive, but you'll need either to add allure to PATH manually or use it from its unpackaged folder

   The easiest way to create an easy to open html report via:
         
   `allure generate --single-file allure-results`

   Then allure report will be put as ./allure-report/index.html
