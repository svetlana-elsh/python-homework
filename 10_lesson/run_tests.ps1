# Test runner

# Calculator test
Write-Host "=== Calculator Test (Chrome) ===" -ForegroundColor Cyan
pytest 10_lesson\tests\test_calculator.py --browser=chrome --alluredir=allure-results

# Store test  
Write-Host "=== Store Test (Firefox) ===" -ForegroundColor Cyan
pytest 10_lesson\tests\test_saucedemo.py --browser=firefox --alluredir=allure-results

# Generate report
allure generate allure-results -o allure-report --clean
allure open allure-report

Write-Host "=== Report generated ===" -ForegroundColor Green