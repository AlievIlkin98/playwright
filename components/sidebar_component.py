import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.sidebar_list_item_component import SidebarListItemComponent
from typing import Pattern


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.dashboard_list_item = SidebarListItemComponent(page=page, identifier="dashboard")
        self.logout_list_item = SidebarListItemComponent(page=page, identifier="logout")
        self.courses_list_item = SidebarListItemComponent(page=page, identifier="courses")


    def check_visible(self):
        self.dashboard_list_item.check_visible('dashboard')
        self.logout_list_item.check_visible('logout')
        self.courses_list_item.check_visible('courses')


    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(".*/#/dashboard"))


    def click_courses(self):
        self.courses_list_item.navigate(re.compile(".*/#/courses"))


    def click_logout(self):
        self.logout_list_item.navigate(re.compile(".*/#/auth/login"))
