class Locators:
    COVER_STORY_TEXT = "//div[text()='Cover Story ']"
    BIKE_BUTTON = "//button[text()='Bike']"
    RIGHT_ARROW_SECTION_2 = "(//span[@data-testid='right-button'])[2]"
    RIGHT_ARROW_SECTION_4 = "(//span[@data-testid='right-button'])[4]"
    FIRST_CAR_BRAND = "(//div[@class='iconCard card  '])[1]"

    COMPARISON_CARD = "//div[@data-widget='ComparisonCard']"
    VIEW_ALL_COMPARISON = "(//span[text()='View All'])[8]"
    SELECT_CAR_1_MAKE = "(//select[@class='customSelect cvSelect relative'])[1]"
    LAND_ROVER_OPTION_1 = "(//option[text()='Land Rover'])[1]"
    SELECT_CAR_1_MODEL = "(//select[@placeholder='Select Make'])[2]"
    CAR_MODEL_OPTION_1 = "(//option[@value='1596'])[1]"
    SELECT_CAR_1_VARIANT = "(//select[@placeholder='Select Variant'])[1]"
    CAR_VARIANT_OPTION_1 = "(//option[@value='19764'])[1]"

    SELECT_CAR_2_MAKE = "(//select[@class='customSelect cvSelect relative'])[3]"
    LAND_ROVER_OPTION_2 = "(//option[text()='Land Rover'])[2]"
    SELECT_CAR_2_MODEL = "(//select[@placeholder='Select Make'])[4]"
    CAR_MODEL_OPTION_2 = "(//option[@value='1462'])[2]"
    SELECT_CAR_2_VARIANT = "(//select[@placeholder='Select Variant'])[2]"
    CAR_VARIANT_OPTION_2 = "(//option[@value='16969'])"

    SELECT_CAR_3_MAKE = "(//select[@class='customSelect cvSelect relative'])[5]"
    LAND_ROVER_OPTION_3 = "(//option[text()='Land Rover'])[3]"
    SELECT_CAR_3_MODEL = "(//select[@placeholder='Select Make'])[6]"
    CAR_MODEL_OPTION_3 = "(//option[@value='1511'])[3]"
    SELECT_CAR_3_VARIANT = "(//select[@placeholder='Select Variant'])[3]"
    CAR_VARIANT_OPTION_3 = "(//option[@value='20048'])"

    COMPARE_BUTTON = "(//button[text()='Compare'])[1]"
    COMPARE_RESULT = "(//div[@class='wrapper'])[8]"

    HOME_BUTTON = "//a[@title='Home']"
    QUESTION_LABEL = "//p[@class='quest']"
    HEAD_LABEL = "//p[@class='head']"
    QUESTION_BOX = "//textarea[@placeholder='Your Questions']"
    NAME_FIELD = "//input[@name='name']"
    EMAIL_FIELD = "//input[@name='email']"
    SUBMIT_BUTTON = "//button[@type='button']"

    @staticmethod
    def FOOTER_ITEM(n):
        return f"//div[@class='fItem'][{n}]"

    SEARCH_INPUT = "//input[@class='headerInput']"
    SEARCH_RESULT = "(//div[text()='Kawasaki Ninja 650 Bikes'])[1]"
    OVERVIEW_SECTION = "//div[@id='overview']"
    ABOUT_SECTION = "//div[@id='about']"
    EXPERT_REVIEW = "//div[@id='expert-review']"
    QUICK_COMPARE = "//div[@data-widget='quickCompare']"
    PERFORMANCE_TAB = "(//h3[text()='Performance'])"
    COMFORT_TAB = "(//h3[text()='Comfort'])"
    FEATURES_TAB = "(//h3[text()='Features'])"
    CITY_INPUT = "//input[@placeholder='Type Here to Search City']"
    FIND_DEALER = "//button[text()='Find Dealer']"

    SELL_CAR = "(//a[contains(@href, '/used/sell-your-car')])[1]"

    SELL_CAR_NAME = "//input[@id='leadform-name']"
    SELL_CAR_MOBILE = "//input[@id='leadform-mobile']"
    SELL_CAR_SUBMIT = "//button[text()='Submit']"

    #New Bikes Xpath

    NEW_BIKES = "//a[@title='New Bikes' and contains(@href, '/new-bikes')]"
    NEW_BIKE_LIST = "//div[@class='sellUsed grid2 grid gridJs']"
    BIKE_FILTER_BUTTON = "(//button[@type='button'])[5]"
    SEARCH_BUTTON = "(//button[text()='Search'])"
    VIEW_ALL_NEW_BIKES = "(//span[@class='viewAll relative'])[1]"
    Bike_Stories = "(//span[@class='right-arrow'])[1]"
    Latest_Bike_found = "(//div[@data-testid='carousel-container'])[4]"
    Commuter = "//h3[text()='Commuter']"
    Commuter_arrow = "(//span[@class='right-arrow'])[3]"
    Cruiser ="(//h3[text()='Cruiser'])"
    Cruiser_arrow ="(//span[@class='right-arrow'])[4]"
    Scooter = "(//h3[text()='Scooter'])"
    Scooter_arrow = "(//span[@class='right-arrow'])[5]"
    Popular_Electric_Bikes = "(//span[@class='right-arrow'])[7]"
    Newly_Launched_Bikes_arrow ="(// span[@class ='right-arrow'])[8]"
    Popular_Bikes = "(//h3[text()='Popular Bikes'])"
    Popular_Bikes_arrow = "(// span[@class ='right-arrow'])[9]"
    Upcoming_Bikes = "(//h3[text()='Upcoming Bikes'])"
    Upcoming_Bikes_arrow = "(// span[@class ='right-arrow'])[10]"
    One_lakh_to_half_lakh = "//h3[text()='Between 1 Lakh to 1.5 Lakh']"
    One_lakh_to_half_lakh_arrow = "(// span[@class ='right-arrow'])[11]"
    Between_one_half_lakh_to_three_lakh = "(//h3[text()='Between 1.5 Lakh - 2.5 Lakh'])"
    Between_one_half_lakh_to_three_lakh_arrow = "(// span[@class ='right-arrow'])[12]"
    Top_Brands = "//div[@id='icon-card']"

    # News & Reviews

    NEWS_REVIEWS_TAB = "(//span[@class='uppercase'])[2]"
    CATEGORY_SECTION = "//div[@id='categories']"
    #About Us
    About_us = "(//span[@class='uppercase'])[8]"
    AboutUs1="(//a[contains(@href, 'buying-a-new-car-full-payment-vs-emis-which-is-smarter-for-your-money')])[2]"
    highlights = "//div[@class='mb30']"

    #Top brand bikes
    Royal = "//img[@title='Royal Enfield Bikes']"
    Royal_review ="(//div[text()='Reviews'])[5]"
    cross1 = "//*[name()='path' and contains(@d,'M19 6.41L1')]"
    Varrient = "(//div[text()='Variants'])[5]"
    cross2 = "//*[name()='path' and contains(@d,'M19 6.41L1')]"
    Royal_compare = "(//div[text()='Compare'])[5]"
    Royal_compare1 = "(//input[@type='checkbox'])[2]"
    Royal_compare2 = "(//input[@type='checkbox'])[3]"
    Royal_compare3 = "(//input[@type='checkbox'])[4]"
    Royal_compare_button = "//button[text()='Compare Now']"
    royal_color = "//a[@title='Colors']"
    expert_rating = "//a[@title='Expert Rating']"
    Engine_Performance = "//a[@title='Engine & Performance']"
    Dimension_Weight = "//a[@title='Dimension and Weight']"
    Fuel_Efficiency = "//a[@title='Fuel Efficiency']"
    Suspension_Brakes = "//a[@title='Suspension Brakes & Wheels']"
    Standard_Features = "//a[@title='Standard Features']"

    #Scrap your car

    car_service_main = "(//span[text()='Car services'])[1]"
    scrap_your_car = "(//span[text()='Scrap Your Car'])[1]"
    scrap_your_car_steps = "//div[@data-widget ='ImageScroller']"
    why_choose_car = "(//div[@class='wrapper'])[8]"

    #Socal media touch
    youtube = "(//img[@alt='car&bike Youtube'])"
    Twitter = "(//img[@alt='car&bike Twitter'])"
    Instagram = "(//img[@alt='car&bike Instagram'])"
    facebook = "(//img[@alt='car&bike Facebook'])"
    Linkedin = "(//img[@alt='car&bike Facebook'])"
    whatsup = "(//img[@alt='car&bike WhatsApp'])"
    office_add = "(//div[@class='fAddr'])[1]"


    #First Look
    video= "(//span[text()='Videos'])[1]"
    first_look = "(//span[text()='First Look'])[1]"
    arrow_1 = "//div[@class='arrowRight']"
    categories = "//div[@class='listContainer grid card  ']"

    #Keep in touch

    scrollButton = "window.scrollBy(0,document.body.scrollHeight);"
    address = "//div[@class='fAddr']"
    contact = "//div[@class='fTel flex gridAc mb10']"
    email = "//div[@class='fTel flex gridAc']"
    copyright = "(//div[@class='fAddr'])[2]"

    #Test Budget bike button
    New_bike_budget = "(//span[@class='uppercase'])[5]"
    New_bike_budget_button = "(//span[@class='nListTitle'])[14]"
    New_bike_budget_button_price = "(//button[@type='button'])[4]"
    New_bike_budget_button_type = "(//button[@type='button'])[8]"
    New_bike_budget_button_search = "(//button[text()='Search'])[1]"
    Key_highlights = "(//div[@class='card toggleSlide '])[1]"
    faq = "(//div[@id='faqs'])[1]"









'''
    New_Cars_Home = "(//span[@class='uppercase'])[4]"
    New_Cars = "//div[@data-widget='ImageScroller']"
    right_click = "(//span[@data-testid='right-button'])[1]"
    Price_of_car = "//span[text()='25 - 40 Lakh']"
    Coupe_car ="//span[text()='Coupe']"
    CAR_Search ="(//button[text()='Search'])[1]"
'''