git clone 
cd test_API_jsonplaceholder

python -m venv venv

source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt

Запуск и формирование отчета:
pytest --alluredir=./allure_results
allure serve ./allure_results#   t e s t _ A P I _ j s o n p l a c e h o l d e r  
 