import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button(browser):
	browser.get(link)
	text_long = browser.find_element_by_class_name('btn-add-to-basket').text
	text_long = len(text_long)

	time.sleep(1)
	assert text_long > 1