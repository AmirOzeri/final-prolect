'''
This file contains all the selectors of the XYZ Bank that I used in my codes.
'''

selectors = \
    {
        'login_page':
            {  # https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login
                  'customer_login_btn': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button',
                  'manager_login_btn': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button',
                  'home_btn': 'body > div > div > div.box.mainhdr > button.btn.home'},
        'customer_page':
            {  # https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer
                  'hermione': '#userSelect > option:nth-child(2)',
                  'harry': '#userSelect > option:nth-child(3)',
                  'ron': '#userSelect > option:nth-child(4)',
                  'albus': '#userSelect > option:nth-child(5)',
                  'neville': '#userSelect > option:nth-child(6)',
                  'login_btn': 'body > div > div > div.ng-scope > div > form > button'},
        'account_page':
            {  # https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account
                  'deposit_btn': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)',
                  'withdraw_btn': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)',
                  'amount_tb': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input',
                  'balance_number': 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)',
                  'currency_type': 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(3)',
                  'log_out_btn': 'body > div > div > div.box.mainhdr > button.btn.logout',
                  'transactions_btn':'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)',
                  'date_time':'body > div > div > div.ng-scope > div > div:nth-child(2) > table > thead > tr > td:nth-child(1) > a',
                  'transaction_table':'body > div > div > div.ng-scope > div > div:nth-child(2) > table',
                  'account_num_btn1':'#accountSelect > option:nth-child(1)',
                  'account_num_btn2':'#accountSelect > option:nth-child(2)',
                  'account_num_btn3':'#accountSelect > option:nth-child(3)',
                  'back_btn':'body > div > div > div.ng-scope > div > div.fixedTopBox > button:nth-child(1)'},
        'manager_page':
            {  # https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager
                  'add_customer_btn': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(1)',
                  'first_name_tb': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input',
                  'last_name_tb': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input',
                  'post_code_tb': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input',
                  'open_account_btn': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(2)',
                  'dollar': '#currency > option:nth-child(2)',
                  'pound': '#currency > option:nth-child(3)',
                  'rupee': '#currency > option:nth-child(4)',
                  'process_btn': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button',
                  'customers_btn': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)',
                  'delete_btn1': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > button',
                  'delete_btn2': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(2) > td:nth-child(5) > button',
                  'delete_btn3': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(3) > td:nth-child(5) > button',
                  'delete_btn4': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(4) > td:nth-child(5) > button',
                  'delete_btn5': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(5) > td:nth-child(5) > button',
                  'customers_table': 'body > div > div > div.ng-scope > div > div.ng-scope > div',
                  'account1_data': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(1)',
                  'account2_data': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(2)',
                  'account3_data': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(3)',
                  'account4_data': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(4)',
                  'account5_data': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(5)'}
    }