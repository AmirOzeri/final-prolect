import re
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

'''
transenction - עסקה
deposit - להפקיד
withdrawl - משיכה
'''


#- כנס למערכת בתור משתמש תעשה העברה של 1500 יש לוודא שההעברה בוצעה ומופיעה בדו״ח העברות -withdrowl



# url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/'


def get_driver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def user_withdrawl(driver,login_page,customer_page,account_page,customer_name,withdrawl,transaction_type):
    wait = WebDriverWait(driver, 10)
    customer_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_page['customer_login_btn'])))
    customer_login.click()
    customer_name_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer_name)))
    customer_name_login.click()
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer_page['login_btn'])))
    login_btn.click()
    withdrawl_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['withdraw_btn'])))
    withdrawl_btn.click()
    amount_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['amount_tb'])))
    amount_tb.click()
    amount_tb.send_keys(withdrawl)
    amount_tb.send_keys(Keys.ENTER)
    current_time = datetime.now().strftime('%b %d, %Y %I:%M:%S %p')
    current_time = re.sub(r' 0(\d:)', r' \1', current_time)
    time.sleep(2)
    transaction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transactions_btn'])))
    transaction_btn.click()
    time.sleep(2)
    date_time_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['date_time'])))
    date_time_btn.click()
    time.sleep(2)
    transaction_table = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transaction_table']))).text
    time.sleep(1)
    current_time = current_time + ' ' + str(withdrawl) + transaction_type
    return current_time, transaction_table



# driver = get_driver(url)
# # wait = WebDriverWait(driver, 10)
# customer_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['login_page']['customer_login_btn'])))
# customer_login.click()
# customer_name_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['customer_page']['hermione'])))
# customer_name_login.click()
# login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,selectors['customer_page']['login_btn'])))
# login_btn.click()
# withdrawl_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,selectors['account_page']['withdraw_btn'])))
# withdrawl_btn.click()
# amount_tb = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,selectors['account_page']['amount_tb'])))
# amount_tb.click()
# amount_tb.send_keys('1500')
# amount_tb.send_keys(Keys.ENTER)
# current_time = datetime.now().strftime('%b %d, %Y %I:%M:%S %p')
# current_time = re.sub(r' 0(\d:)', r' \1', current_time)
# time.sleep(2)
# transaction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['account_page']['transactions_btn'])))
# transaction_btn.click()
# time.sleep(2)
# date_time_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['account_page']['date_time'])))
# date_time_btn.click()
# time.sleep(2)
# transaction_table = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors['account_page']['transaction_table']))).text
# time.sleep(1)
# driver.close()
# print(current_time)
# print(transaction_table)
# txt = current_time + ' 1500 Debit'
# print(txt)
# print(txt in transaction_table)
# print(current_time in transaction_table)

def check_account(driver,login_page,customer_page,account_page,customer_name):
    wait = WebDriverWait(driver, 10)
    customer_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_page['customer_login_btn'])))
    customer_login.click()
    customer_name_login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer_name)))
    customer_name_login.click()
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, customer_page['login_btn'])))
    login_btn.click()

    account_number1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['account_num_btn1'])))
    account_number1.click()
    transaction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transactions_btn'])))
    transaction_btn.click()
    time.sleep(2)
    transaction_table1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transaction_table']))).text
    time.sleep(1)
    back_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['back_btn'])))
    back_btn.click()
    time.sleep(1)

    account_number2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['account_num_btn2'])))
    account_number2.click()
    transaction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transactions_btn'])))
    transaction_btn.click()
    time.sleep(2)
    transaction_table2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transaction_table']))).text
    time.sleep(1)
    back_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['back_btn'])))
    back_btn.click()
    time.sleep(1)

    account_number3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['account_num_btn3'])))
    account_number3.click()
    transaction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transactions_btn'])))
    transaction_btn.click()
    time.sleep(2)
    transaction_table3 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, account_page['transaction_table']))).text
    time.sleep(1)
    lines1 = transaction_table1.split('\n')
    lines2 = transaction_table2.split('\n')
    lines3 = transaction_table3.split('\n')
    return lines1, lines2, lines3
