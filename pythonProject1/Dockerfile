# Используйте официальный образ Python
FROM python:3.8

# Установите рабочую директорию в контейнере
WORKDIR /code

# Скопируйте файлы зависимостей
COPY requirements.txt .

# Установите зависимости
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# Скопируйте только необходимые файлы в контейнер
COPY ./requirements.txt /code/requirements.txt
COPY ./main.py /code/main.py
COPY ./BTC_AML_blockchain_Info.py /code/BTC_AML_blockchain_Info.py
COPY ./ETH_AML_etherscan.py /code/ETH_AML_etherscan.py
COPY ./USDT_TRC20_AML_trongrid.py /code/USDT_TRC20_AML_trongrid.py

ENV PYTHONPATH "${PYTHONPATH}:/code"

# Запускайте приложение на порту 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
