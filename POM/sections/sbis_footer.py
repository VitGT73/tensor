from playwright.sync_api import Page

from sites.stepik.page_factory import StepikModule, StepikLesson
from selenium.webdriver.common.by import By

class Sidebar:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.all_modules_locator = "//*[@class='sidebar-module-header__title']"
        self.lessons_relation_locator = "//*[@class='lesson-sidebar__toc-inner']"

        self.modules = StepikModule(page, locator="//*[@class='sidebar-module-header__title']", name='Modules')
        self.lessons = StepikLesson(page, locator="//*[@class='lesson-sidebar__toc-inner']", name='Modules')

    def get_modules(self) -> list[StepikModule]:
        item_elements = self.page.query_selector_all(self.all_modules_locator)
        items = [StepikModule(page=self.page, locator=f"{self.all_modules_locator}[{num}]", name=f"{num}")
                 for num, element in enumerate(item_elements)]
        return items

    def get_module(self, condition) -> StepikModule | None:
        items = self.get_modules()
        for item in items:
            if condition(item):
                return item
        raise Exception("Module not found")

    def get_lessons(self, module: StepikModule) -> list[StepikLesson]:
        items_locator = str(module.get_locator()) + self.lessons_relation_locator
        item_elements = self.page.query_selector_all(items_locator)
        items = [StepikLesson(page=self.page, locator=f"{items_locator}[{num}]", name=f"{module.name}.{num}")
                 for num, element in enumerate(item_elements)]
        return items

    def get_lesson(self, module: StepikModule, condition) -> StepikLesson | None:
        items = self.get_lessons(module=module)
        for item in items:
            if condition(item):
                return item
        raise Exception("Lesson not found")
