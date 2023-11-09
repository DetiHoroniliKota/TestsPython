import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope = "function")
def driwer():
    # Перед началом теста
    driver = webdriver.Chrome(ChromeDriverManager().install()) #запускает вебдрайвер при каждом вызове фикстуры.Из кэша
    driver.maximize_window()  # ратягивает окно по всей ширине жкрана.

