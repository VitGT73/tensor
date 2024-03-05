import allure
from helpers.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class TensorAboutPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)


        self.PAGE_URL = Links.TENSOR_ABOUT_PAGE
        self.WORKING_BLOCK = (By.XPATH, "//div[div[h2[text()='Работаем']]]")
        # self.WORKING_IMAGES = (By.XPATH, "//div[div[h2[text()='Работаем']]]//img")


    @allure.step("Блок 'Работаем' существует")
    def is_working_block_present(self):
        self.wait.until(EC.presence_of_element_located(self.WORKING_BLOCK))


    @allure.step("Checking that the images in the block 'Работаем' are the same size")
    def check_images_same_size(self):
        # Найдем элемент с помощью XPath
        element = self.driver.find_element(*self.WORKING_BLOCK)

        # Теперь найдем все изображения внутри этого элемента
        images = element.find_elements(By.TAG_NAME, "img")

        # Получим размер первого изображения
        first_image = images[0]
        first_width = first_image.size.get("width")
        first_height = first_image.size.get("height")

        for image in images[1:]:
            width = image.size.get("width")
            height = image.size.get("height")
            if width != first_width or height != first_height:
                allure.attach("Сообщение", "Размеры изображений не совпадают: первый: {} x {}, текущий: {} x {}".format(first_width, first_height, width, height), allure.attachment_type.TEXT)
                raise AssertionError("Размеры изображений не совпадают")

        allure.attach("Сообщение", "Все изображения имеют одинаковый размер: {} x {}".format(first_width, first_height), allure.attachment_type.TEXT)
