from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time


class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SUGGEST = (By.ID, "suggest-list-pevc4l50j9")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_SEARCH_RESULT = (By.ID, "search-result")
    LOCATOR_FIRST_lINK = (By.CSS_SELECTOR, "#search-result > .serp-item a.link > b")

    LOCATOR_NAME = "tensor.ru"
    LOCATOR_YANDEX_IMAGE = (By.CSS_SELECTOR, '[data-id="images"]')

    LOCATOR_FIRST_CATEGORY = (By.CSS_SELECTOR, ".PopularRequestList-Item.PopularRequestList-Item_pos_0 > a > div.PopularRequestList-Shadow")
    LOCATOR_FIRST_CATEGORY_TEXT = (By.CSS_SELECTOR, '.PopularRequestList-Item.PopularRequestList-Item_pos_0 > a > div.PopularRequestList-SearchText')

    LOCATOR_IMAGE_SEARCH_FIELD = (By.CSS_SELECTOR, "input.input__control.mini-suggest__input")
    LOCATOR_FIRST_IMAGE_IN_SEARCH = (By.CSS_SELECTOR, "a.serp-item__link")
    LOCATOR_VIEWER = (By.CSS_SELECTOR, ".MediaViewer")
    LOCATOR_IMAGE_ID = (By.CSS_SELECTOR, ".MMImageContainer > img")
    LOCATOR_NEXT_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_next")
    LOCATOR_BACK_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_prev")


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field




    def check_suggest(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SUGGEST, time=2)

    def click_on_the_search_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()

    def check_result(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_RESULT, time=2)

    def check_link(self):
        link = self.find_element(YandexSeacrhLocators.LOCATOR_FIRST_lINK, time=2)

        item = link.text.strip()

        if YandexSeacrhLocators.LOCATOR_NAME != item:
            raise Exception("site tensor.ru not found")

    def check_link_image(self):
        yandex_image = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_IMAGE, time=2)
        yandex_image.click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(2)
        assert "https://yandex.ru/images/" in self.driver.current_url, \
            "it's not https://yandex.ru/images/"


    def check_category(self):
        first_category = self.find_element(YandexSeacrhLocators.LOCATOR_FIRST_CATEGORY, time=2)
        first_category_text = self.find_element(YandexSeacrhLocators.LOCATOR_FIRST_CATEGORY_TEXT, time=2)
        first_category_name = first_category_text.text
        first_category.click()
        time.sleep(2)

        image_search_field = self.find_element(YandexSeacrhLocators.LOCATOR_IMAGE_SEARCH_FIELD, time=2)
        text_image_search_field = image_search_field.get_attribute('value')

        assert first_category_name == text_image_search_field, "search text does not match category name"

    def check_first_image(self):
        first_image = self.find_element(YandexSeacrhLocators.LOCATOR_FIRST_IMAGE_IN_SEARCH, time=2)
        first_image.click()
        return self.find_element(YandexSeacrhLocators.LOCATOR_VIEWER, time=2)
    def check_images_src(self):
        check_before_image = self.find_element(YandexSeacrhLocators.LOCATOR_IMAGE_ID, time=2)
        before_image = check_before_image.get_attribute('src')

        button_next = self.find_element(YandexSeacrhLocators.LOCATOR_NEXT_BUTTON, time=2)
        button_next.click()

        check_after_image = self.find_element(YandexSeacrhLocators.LOCATOR_IMAGE_ID, time=2)
        after_image = check_after_image.get_attribute('src')
        assert before_image != after_image, "after_image has the same src"
        button_back = self.find_element(YandexSeacrhLocators.LOCATOR_BACK_BUTTON, time=2)
        button_back.click()

        check_current_image = self.find_element(YandexSeacrhLocators.LOCATOR_IMAGE_ID, time=2)
        current_image = check_current_image.get_attribute('src')
        assert current_image == before_image, "current_image src  does not have before_image src"


