@echo off
echo
rd /s /q allure-results
rd /s /q allure-report

echo 
pytest --alluredir=allure-results

echo
allure generate allure-results -o allure-report --clean

echo 
allure open allure-report