class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):  # пошук елементу
        return self.driver.find_element(*locator)

    def click_element(self, *locator):  # клік на елемент
        self.find_element(*locator).click()

    def input(self, text, *locator):  # вставка тексту в поле
        e = self.find_element(*locator)
        e.clear()
        e.send_keys(text)
