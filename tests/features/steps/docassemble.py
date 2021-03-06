from lettuce import step, world
from selenium.webdriver.common.keys import Keys
import time

@step('I start the interview "([^"]+)"')
def start_interview(step, interview_name):
    world.browser.get("http://localhost/?i=" + interview_name)
    #world.browser.wait_for_it()

@step('I click the button "([^"]+)"')
def click_button(step, button_name):
    world.browser.find_element_by_xpath('//button[text()="' + button_name + '"]').click()
    world.browser.wait_for_it()

@step('I click the link "([^"]+)"')
def click_button(step, link_name):
    world.browser.find_element_by_xpath('//a[text()="' + link_name + '"]').click()
    world.browser.wait_for_it()

@step('I should see the phrase "([^"]+)"')
def see_phrase(step, phrase):
    assert world.browser.text_present(phrase)

@step('I should not see the phrase "([^"]+)"')
def not_see_phrase(step, phrase):
    assert not world.browser.text_present(phrase)

@step('I set "([^"]+)" to "([^"]+)"')
def set_field(step, label, value):
    elem = world.browser.find_element_by_id(world.browser.find_element_by_xpath('//label[text()="' + label + '"]').get_attribute("for"))
    elem.clear()
    elem.send_keys(value)

@step('I select "([^"]+)" as the "([^"]+)"')
def select_option(step, value, label):
    elem = world.browser.find_element_by_id(world.browser.find_element_by_xpath('//label[text()="' + label + '"]').get_attribute("for"))
    for option in elem.find_elements_by_tag_name('option'):
        if option.text == value:
            option.click()
            break

@step('I wait (\d+) seconds?')
def wait_seconds(step, seconds):
    time.sleep(float(seconds))
    world.browser.wait_for_it()

@step('I should see that "([^"]+)" is "([^"]+)"')
def value_of_field(step, label, value):
    elem = world.browser.find_element_by_id(world.browser.find_element_by_xpath('//label[text()="' + label + '"]').get_attribute("for"))
    assert elem.get_attribute("value") == value
    
@step('I set the text box to "([^"]+)"')
def set_text_box(step, value):
    elem = world.browser.find_element_by_xpath("//input[contains(@alt, 'Input box')]")
    elem.clear()
    elem.send_keys(value)
    
@step('I click the "([^"]+)" option under "([^"]+)"')
def set_mc_option(step, option, label):
    label_elem = world.browser.find_element_by_xpath('//label[text()="' + label + '"]')
    div = label_elem.find_element_by_xpath("..")
    span = div.find_element_by_xpath('//span[text()="' + option + '"]')
    option_label = span.find_element_by_xpath("..")
    option_label.click()
        
@step('I click the "([^"]+)" choice')
def set_mc_option(step, choice):
    span_elem = world.browser.find_element_by_xpath('//span[text()="' + choice + '"]')
    label_elem = span_elem.find_element_by_xpath("..")
    label_elem.click()

@step('I should see "([^"]+)" as the title of the page')
def title_of_page(step, title):
    assert world.browser.title == title

@step('I should see "([^"]+)" as the URL of the page')
def url_of_page(step, url):
    assert world.browser.current_url == url

@step('I exit by clicking "([^"]+)"')
def exit_button(step, button_name):
    world.browser.find_element_by_xpath('//button[text()="' + button_name + '"]').click()
    time.sleep(1.0)

