"""
This class runs all tests
"""
import os,sys,time,pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.product_payment_conf as conf
from page_objects.product_object import Product_Object


def test_weather_shopper_form(base_url,browser,browser_version,os_version,os_name,remote_flag,remote_project_name,remote_build_name):

    "Run the test"
    try:
        
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1
        
        #Create a test object 
        test_obj = PageFactory.get_page_object("Main Page",base_url=base_url)

        #2. Setup and register a driver
        start_time = int(time.time())	#Set start_time with current time
        test_obj.register_driver(remote_flag,os_name,os_version,browser,browser_version,remote_project_name,remote_build_name)

        #3. Read the temparature
        result_flag=test_obj.get_temprature()
        test_obj.write("Temperature is %s"%result_flag)
        # print("Temperature is %s"%result_flag)

        #4. Select appropriate item and check the screen
        if int(result_flag) <= 19:
           # print("Temperature is %s"%result_flag)
           #print("We will buy moisturiser")
           test_obj.click_moisturizers()
           is_screen_visible=test_obj.check_redirect_moisturizers()
           #print(is_screen_visible)
           if is_screen_visible is not None:
               test_obj.write("You are on Buy Moisturizer page")
           
           # Select product categories
           product_moisturizers_category = conf.product_moisturizers_category
           test_obj.write("product categories are %s"%product_moisturizers_category)

           # Adding the product categories in the cart
           test_obj.add_products(product_moisturizers_category)

           # view the added products on the cart
           test_obj.click_cart()

           # verify you are at cart screen
           is_screen_visible=test_obj.check_redirect_cart()
           if is_screen_visible is not None:
              test_obj.write("You are on cart page")


        elif int(result_flag) >=34:
           #print("Temperature is %s"%result_flag)
           #print("We will buy sunscreens")
           test_obj.click_sunscreens()
           is_screen_visible=test_obj.check_redirect_sunscreens()

           #print(is_screen_visible)
           if is_screen_visible is not None:
               test_obj.write("You are on Buy Sunscreens page")

           # Select product categories
           product_sunscreens_category = conf.product_sunscreens_category
           test_obj.write("product categories are %s"%product_sunscreens_category)

           # Adding the product categories in the cart
           test_obj.add_products(product_sunscreens_category)

           # view added products on the cart
           test_obj.click_cart()

           # verify you are cart screen
           is_screen_visible=test_obj.check_redirect_cart()
           if is_screen_visible is not None:
              test_obj.write("You are on cart page")


        #Teardown
        test_obj.wait(3)
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter
        test_obj.teardown()
        
        
        
    except Exception as e:
        print("Exception when trying to run test:%s"%__file__)
        print("Python says:%s"%str(e))

    
       
    
#---START OF SCRIPT   
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()
                
    #Run the test only if the options provided are valid
    if options_obj.check_options(options): 
        test_weather_shopper_form(base_url=options.url,
                        browser=options.browser,
                        browser_version=options.browser_version,
                        os_version=options.os_version,
                        os_name=options.os_name,
                        remote_flag=options.remote_flag,
                        remote_project_name=options.remote_project_name,
                        remote_build_name=options.remote_build_name)

    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(options_obj.print_usage())