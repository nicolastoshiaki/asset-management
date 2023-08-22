from sqlalchemy import create_engine
from sqlalchemy.engine import URL
#import pandas as pd
import sys
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

from classes import User, Authenticator, UserNotAuthenticatedError, WebScraping
from infra.repository import AmUserRepository, AmProductsRepository, AmInvestPortRepository, AmProdTypeRepository

authentication = Authenticator()
repo_user = AmUserRepository()
repo_product = AmProductsRepository()
repo_invest_port = AmInvestPortRepository()
repo_prod_type = AmProdTypeRepository()
web_scraping = WebScraping()

menu_selection_sucess = False
while not menu_selection_sucess:
    menu_selection = input(
        "[1] LogIn, [2] Sign Up, [3] Exit program:")
    if menu_selection == "1":
        menu_selection_sucess = True
    elif menu_selection == "2":
        new_login = input("Login:")        
        user_check = authentication.check_existing_user(new_login)        
        if user_check:
            new_password = getpass.getpass("Password:")
            new_username = input("Insert your full name:")
            new_user_return = authentication.create_new_user(
                new_login, new_password, new_username)
            if new_user_return:
                print(f"User {new_login} created sucessfully!")
                menu_selection_sucess = True
            else:
                print("Error.")
        else:            
            print(f"User {new_login} already exists!")
    elif menu_selection == "3":
        print("Closing program...")
        sys.exit()
    else:
        print("Invalid option.")

print()

login_sucess = False
while not login_sucess:
    insert_user = input("Login (leave empty to exit program):")
    if not insert_user:
        print("Closing program...")
        sys.exit()
    else:
        insert_password = getpass.getpass("Password:")
        try:
            main_user = authentication.user_authentication(
                insert_user, insert_password)
            print(f"Welcome {main_user.username.strip()}!")
            main_user.get_porfolio()
            if not main_user.portfolio:
                print("User does not have a portfolio registered.")
            else:
                print("Portfolio loaded sucessfully.")
            login_sucess = True
        except UnboundLocalError:
            print("User does not exist.")
        except UserNotAuthenticatedError:
            print(f"Invalid password for {insert_user}")


log_off_flag = False
list_of_id = []
while not log_off_flag:
    action_selected = input(
        "[1] Check Portfolio, [2] Update Portfolio, [3] Update Asset Market Values, [4] Leave Programm: ")
    if action_selected == "1":
        portfolio_total_assets = 0
        portfolio_value = 0.0
        for key in main_user.portfolio:
            portfolio_total_assets += 1
            portfolio_value += float(main_user.portfolio[key][1]) * float(main_user.portfolio[key][2])
        if portfolio_value == 0.0:
            print("Update the assets market values first!")
        else:
            print(f"You have {portfolio_total_assets} total assets in your portfolio!")
            print(f"You portfolio is worth R${portfolio_value:,.2f}!")
            print("-------------")
            print(main_user.portfolio)
    elif action_selected == "2":
        user_input_asset = input("Input the asset you want to update in your portfolio: ").upper()
        if user_input_asset in main_user.portfolio:
            print(f"Asset already exists in the protfolio. You have {main_user.portfolio.get(user_input_asset)[1]} shares.")
            user_choice = input("Do you want to update the quantity [U] or remove the asset [R]? ").upper()
            if user_choice == "U":                 
                user_input_asset_quantity = input("Insert new quantity: ")
                insert_portfolio_result = main_user.update_asset_quantity_in_portfolio(user_input_asset, user_input_asset_quantity)
                if insert_portfolio_result:
                    print("Asset quantity updated!")   
            elif user_choice == "R":
                user_remove_asset_option_doublecheck = input(f"Are you shure do you want to remove {user_input_asset} from your portfolio? [Y/N] ")
                if user_remove_asset_option_doublecheck == "Y":
                    remove_asset_return = main_user.remove_asset(user_input_asset)
                    print(f'{remove_asset_return} of {user_input_asset} were deleted from your portfolio!')
        else:
            query_check_asset_exists_database = repo_product.select_by_name(user_input_asset)
            if query_check_asset_exists_database:
                user_input_asset_quantity = input("Insert quantity: ")
                insert_portfolio_result = main_user.insert_asset(user_input_asset, user_input_asset_quantity)
                if insert_portfolio_result:
                    print("Asset added to portfolio!")
            else:
                print("Asset does not exists in the database.")
                query_get_all_short_types = repo_prod_type.select_short_types()
                for item in query_get_all_short_types:
                    user_new_asset_prod_type_id = item.id_type
                    user_new_asset_prod_type_short = item.des_type_short
                    list_of_id.append(user_new_asset_prod_type_id)
                    print(item)
                user_new_asset_prod_type = input("Insert asset type (number) from the options shown above (Type 99 to exit): ")
                try:
                    int(user_new_asset_prod_type)
                    if user_new_asset_prod_type == '99':
                        continue
                    elif int(user_new_asset_prod_type) in list_of_id:
                        repo_product.insert(user_input_asset, user_new_asset_prod_type)
                        print("Asset added to the database!")
                        user_input_asset_quantity = input("Insert quantity: ")
                        insert_portfolio_result = main_user.insert_asset(user_input_asset, user_input_asset_quantity)
                        if insert_portfolio_result:
                            print("Asset added to portfolio!")
                    else:
                        print("Invalid number!")
                except ValueError:
                    print("Please insert the type number, not the name!") 
        main_user.portfolio.clear()             
        main_user.get_porfolio()
    elif action_selected == "3":  
        main_user.portfolio = web_scraping.get_asset_price(main_user.portfolio) 
    elif action_selected == "4":
        print("Closing program...")
        log_off_flag = True
    else:
        print("Invalid option.")


sys.exit()
