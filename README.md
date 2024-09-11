Автоматический тест покупки на saucedemo.com

Этот репозиторий содержит автоматический e2e тест для проверки сценария покупки товара на сайте saucedemo.com с использованием Python и Selenium WebDriver.

Требования:
-Python 3.x
-Библиотека Selenium (pip install selenium)
-Браузер Chrome

Установка
-Скачать файл main.py
-Запустить файл main.py

Запуск теста
Тест будет выполнять следующие действия:
1) Авторизация на сайте saucedemo.com с тестовым аккаунтом:
   -Логин: "standard_user"
   -Пароль: "secret_sauce"
2) Выбор товара "Sauce Labs Backpack" и добавление его в корзину.
3) Проверка корзины на наличие выбранного товара.
4) Оформление покупки, заполнение полей:
   -First Name: "User"
   -Last Name: "User_ln"
   -Zip/Postal Code: "12345"
5) Завершение покупки.
6) Проверка успешного завершения покупки.
