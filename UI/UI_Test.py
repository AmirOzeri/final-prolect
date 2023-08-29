import pytest
from dict01 import *
from UIfunctions import *
import os
import traceback

class TestUI_amir:
    @pytest.fixture()
    def url(self):
        '''
        :return:
        '''
        try:
            return 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/'
        except Exception as error:
            print(f'Error url {error}')
            return None
    def take_screenshot(self,driver,test_name):
        '''
        :param driver:
        :param test_name:
        :return:
        '''
        try:
            screenshot_dir = 'UI_Test_Errors'
            if not os.path.exists(screenshot_dir):
                os.mkdir(screenshot_dir)
            screenshot_path = os.path.join(screenshot_dir,f'{test_name}.png')
            driver.save_screenshot(screenshot_path)
            print(f'Screenshot saved: {screenshot_path}')
        except Exception as error:
            print(f'Error occurred while capturing a screenshot: {error}')

    def test1_user_withdrawl(self,url):
        '''
        :param url:
        :return:
        '''
        driver = None
        try:
            driver = get_driver(url)
            current_time, transaction_table = user_withdrawl\
                (driver,selectors['login_page'],selectors['customer_page'],
                 selectors['account_page'],selectors['customer_page']['hermione'],1500,' Debit')
            if current_time not in transaction_table:
                self.take_screenshot(driver, 'Test1_error_assertion')
                traceback.print_exc()
                print('The transfer was not executed')
            assert current_time in transaction_table
        except Exception as error:
            self.take_screenshot(driver,'Test1_error')
            traceback.print_exc()
            raise
        finally:
            if driver:
                driver.quit()

    def test2_check_accounts(self,url):
        '''
        :param url:
        :return:
        '''
        driver = None
        try:
            driver = get_driver(url)
            transaction_table1, transaction_table2, transaction_table3 = \
                check_account(driver,selectors['login_page'],selectors['customer_page'],
                              selectors['account_page'],selectors['customer_page']['harry'])
            transaction = len(transaction_table1) + len(transaction_table2) + len(transaction_table3)
            if transaction != 4:
                self.take_screenshot(driver, 'Test2_error_assertion')
                traceback.print_exc()
                print('There is more or less than one transfer in all of the accounts')
            else:
                assert transaction == 4
        except Exception as error:
            self.take_screenshot(driver, 'Test2_error')
            traceback.print_exc()
            raise
        finally:
            if driver:
                driver.quit()

    def test3_check_transaction(self,url):
        '''
        :param url:
        :return:
        '''
        driver = None
        try:
            driver = get_driver(url)
            values = [100, 200, 300]
            transaction_count = check_transaction\
                (driver,selectors['login_page'],selectors['customer_page'],selectors['account_page'],selectors['customer_page']['hermione'],values)
            if transaction_count != 3:
                self.take_screenshot(driver, 'Test3_error_assertion')
                traceback.print_exc()
                raise AssertionError('The transaction failed')
            assert transaction_count == 3
        except Exception as error:
            self.take_screenshot(driver, 'Test3_error')
            traceback.print_exc()
            raise
        finally:
            if driver:
                driver.quit()

    def test4_check_customers(self,url):
        '''
        :param url:
        :return:
        '''
        driver = None
        try:
            driver = get_driver(url)
            customers_table = check_customers(driver,selectors['login_page'],selectors['manager_page'])
            if len(customers_table) != 6:
                self.take_screenshot(driver, 'Test4_error_assertion')
                traceback.print_exc()
                print('There are more or less than five customers in the system')
            assert len(customers_table) == 6
        except Exception as error:
            self.take_screenshot(driver, 'Test4_error')
            traceback.print_exc()
            raise
        finally:
            if driver:
                driver.quit()

    def test5_invalid_add_user(self,url):
        '''
        :param url:
        :return:
        '''
        driver = None
        try:
            driver = get_driver(url)
            customers_table_after, customers_table_before = invalid_add_user(driver,selectors['login_page'],selectors['manager_page'],'luna','1234')
            if customers_table_before != customers_table_after:
                self.take_screenshot(driver, 'Test5_error_assertion')
                traceback.print_exc()
                print('Invalid user was added anyway')
            assert customers_table_before == customers_table_after
        except Exception as error:
            self.take_screenshot(driver, 'Test5_error')
            traceback.print_exc()
            raise
        finally:
            if driver:
                driver.quit()

