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


    def is_working_block_present(self):
        with allure.step("Block 'Работаем' is present"):
            self.wait.until(EC.presence_of_element_located(self.WORKING_BLOCK))



    def check_images_same_size(self):
        with allure.step("Checking that the images in the block 'Работаем' are the same size"):
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
                    allure.attach("Message", "Image sizes don't match! First: {} x {}, current: {} x {}".format(first_width, first_height, width, height), allure.attachment_type.TEXT)
                    raise AssertionError("Image sizes don't match")

            allure.attach("Message", "All images are the same size: {} x {}".format(first_width, first_height), allure.attachment_type.TEXT)
