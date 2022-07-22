from YandexPages import SearchHelper


def test_yandex_search(browser):
    yandex_image_page = SearchHelper(browser)
    yandex_image_page.go_to_site()
    yandex_image_page.check_link_image()
    yandex_image_page.check_category()
    yandex_image_page.check_first_image()
    yandex_image_page.check_images_src()

