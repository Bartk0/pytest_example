# pytest_example

## Installation of Requirements

Execute in project directory

```bash
pip3 install -r requirements.txt
```

## Run tests

* With commandline and allure report from root project directory:

```bash
python3 pytest --alluredir=allure_report
```

* With IDE (PyCharm):
    * Right click on `tests` project folder
    * Choose `Run py.test in tests`

## Get allure reports

Execute in project directory

```bash
allure serve allure_report
```
