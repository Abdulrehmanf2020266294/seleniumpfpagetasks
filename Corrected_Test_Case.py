
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from homePageElements import HomePageElements


driver = webdriver.Chrome()
driver.get("https://pf.com.pk/")
driver.maximize_window()
time.sleep(4)

# Generic function for clicking a button and validating the URL
def click_button_and_validate(xpath, expected_url_part):
    button = driver.find_element(By.XPATH, xpath)
    assert button.is_displayed(), "Button is not visible on the page."
    button.click()
    time.sleep(2)
    assert expected_url_part in driver.current_url, f"Navigation to {expected_url_part} page failed."

# Expertise button
click_button_and_validate(HomePageElements.expertise, "expertise")
print("Expertise button clicked successfully and the correct page loaded.")
driver.back()

# About Us button
click_button_and_validate(HomePageElements.about_us, "about-us")
print("About Us button clicked successfully and the correct page loaded.")
driver.back()

# Life at PF button
click_button_and_validate(HomePageElements.life_at_pf, "life-at-pf")
print("Life at PF button clicked successfully and the correct page loaded.")
driver.back()

# Graduate Gateway button
click_button_and_validate(HomePageElements.trainee_program, "trainee-program")
print("Graduate Gateway Program button clicked successfully and the correct page loaded.")
driver.back()

# Career button
click_button_and_validate(HomePageElements.career, "career")
print("Career button clicked successfully and the correct page loaded.")
driver.back()

# Apply Now button
click_button_and_validate(HomePageElements.apply_now, "apply-now")
print("Apply Now button clicked successfully and the correct page loaded.")
driver.back()

# Career dropdown option
def career_dropdown_click(dropdown_id, expected_url):
    actions = ActionChains(driver)
    Career_button = driver.find_element(By.XPATH, HomePageElements.career)
    actions.move_to_element(Career_button).perform()
    Career_dropdown = driver.find_element(By.ID, dropdown_id)
    Career_dropdown.click()
    time.sleep(2)
    assert driver.current_url == expected_url, "Career dropdown navigation failed."

# Dropdown 1 - Open positions
career_dropdown_click(HomePageElements.career_drop1, "https://pf.com.pk/apply-now/")
print("Career dropdown 1 clicked successfully and correct page loaded.")
driver.back()

# Dropdown 2 - Send Resume
career_dropdown_click(HomePageElements.career_drop2, "https://pf.com.pk/apply-now/#popup1")
print("Career dropdown 2 clicked successfully and correct page loaded.")
driver.back()

# Resources dropdown options
def resource_dropdown_click(xpath, expected_url):
    actions = ActionChains(driver)
    Resource_button = driver.find_element(By.XPATH, HomePageElements.resource)
    actions.move_to_element(Resource_button).perform()
    Resource_dropdown = driver.find_element(By.XPATH, xpath)
    Resource_dropdown.click()
    time.sleep(2)
    assert driver.current_url == expected_url, "Resource dropdown navigation failed."

# Resource option 1 - Blogs
resource_dropdown_click(HomePageElements.resource_drop1, "https://pf.com.pk/blogs/")
print("Resources option 1 Blogs clicked successfully and correct page loaded.")
driver.back()

# Resource option 2 - News
resource_dropdown_click(HomePageElements.resource_drop2, "https://pf.com.pk/news/")
print("Resources option 2 News clicked successfully and correct page loaded.")
driver.back()

# PF logo click
click_button_and_validate(HomePageElements.pf_logo, "pf.com.pk")
print("PF logo clicked successfully and redirected to the homepage.")
