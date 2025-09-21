from selene import browser, be, have
import os, calendar
from pathlib import Path



class RegistrationPage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def fill_first_name(self,value):
        browser.element('#firstName').type(value)

    def fill_last_name(self,value):
        browser.element('#lastName').type(value)

    def fill_email(self,value):
        browser.element('#userEmail').type(value)

    def fill_gender(self,value):
        if value == 'Male':
            browser.element('label[for="gender-radio-1"]').should(be.clickable).click()
        elif value == 'Female':
            browser.element('label[for="gender-radio-2"]').should(be.clickable).click()

    def fill_phone_number(self,value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        month_index = month - 1
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'.react-datepicker__month-select option[value="{month_index}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'.react-datepicker__year-select option[value="{year}"]').click()
        expected_text = f"{calendar.month_name[month]} {year}"
        browser.element('.react-datepicker__current-month').should(have.text(expected_text))
        browser.all('.react-datepicker__day:not(.react-datepicker__day--outside-month)') \
            .element_by(have.text(str(day))) \
            .should(be.visible) \
            .click()

    def fill_subject (self,value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobby(self,value):
        if value == 'Sports':
            target = browser.element('[for="hobbies-checkbox-1"]')
            browser.driver.execute_script("arguments[0].scrollIntoView(true);", target.locate())
            target.should(be.visible).should(be.clickable).click()
        elif value == 'Reading':
            target = browser.element('[for="hobbies-checkbox-2"]')
            browser.driver.execute_script("arguments[0].scrollIntoView(true);", target.locate())
            target.should(be.visible).should(be.clickable).click()
        elif value == 'Music':
            target = browser.element('[for="hobbies-checkbox-3"]')
            browser.driver.execute_script("arguments[0].scrollIntoView(true);", target.locate())
            target.should(be.visible).should(be.clickable).click()

    def send_file(self,value):
        file_path = Path(__file__).parent / value
        if not file_path.exists():
            raise FileNotFoundError(f"Файл {file_path} не найден.")
        browser.element('#uploadPicture').send_keys(str(file_path))

    def fill_adress(self,value):
        browser.element('#currentAddress').type(value)

    def fill_state_city(self,state,city):
        browser.element('#state').click()
        browser.element('#react-select-3-input').type(state).press_enter()
        browser.element('#city').click()
        browser.element('#react-select-4-input').type(city).press_enter()

    def submit(self):
        browser.element('#submit').click()

    def should_have_registered (self, name_surname,useremail,gender,user_number,date_of_birth,subject,hobby,file_name, adress,state_city):
        browser.element('.modal-content').should(be.visible)
        browser.element('.table-responsive').should(have.text(name_surname))
        browser.element('.table-responsive').should(have.text(useremail))
        browser.element('.table-responsive').should(have.text(gender))
        browser.element('.table-responsive').should(have.text(user_number))
        browser.element('.table-responsive').should(have.text(date_of_birth))
        browser.element('.table-responsive').should(have.text(subject))
        browser.element('.table-responsive').should(have.text(hobby))
        browser.element('.table-responsive').should(have.text(file_name))
        browser.element('.table-responsive').should(have.text(adress))
        browser.element('.table-responsive').should(have.text(state_city))








