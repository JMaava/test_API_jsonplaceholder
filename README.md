git clone

cd test_API_jsonplaceholder

pip install -r requirements.txt

Запуск и формирование отчета:
pytest --alluredir=./allure_results
allure serve ./allure_results#
 
 
