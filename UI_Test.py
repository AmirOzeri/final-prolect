import pytest
from dict01 import *
from UIfunctions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUI_amir:
    @pytest.fixture()
    def url(self):
        return 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/'


    def test1_user_withdrawl(self,url):
        driver = get_driver(url)
        current_time, transaction_table = user_withdrawl\
            (driver,selectors['login_page'],selectors['customer_page'],
             selectors['account_page'],selectors['customer_page']['hermione'],1500,' Debit')
        assert current_time in transaction_table
        driver.quit()

    def test2_check_accounts(self,url):
        driver = get_driver(url)
        transaction_table1, transaction_table2, transaction_table3 = \
            check_account(driver,selectors['login_page'],selectors['customer_page'],
                          selectors['account_page'],selectors['customer_page']['harry'])
        assert len(transaction_table1) == 1 or len(transaction_table2) == 1 or len(transaction_table3) == 1
        driver.quit()
