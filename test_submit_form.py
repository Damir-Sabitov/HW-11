from resourse import RegistrationPage
import allure



def test_submit():
    registration_page = RegistrationPage()
    registration_page.open()


    with allure.step('Заполняем имя'):
        registration_page.fill_first_name('John')

    with allure.step('Заполняем фамилию'):
        registration_page.fill_last_name('Smith')

    with allure.step('Заполняем e-mail'):
        registration_page.fill_email('example@mail.ru')

    with allure.step('Заполняем пол'):
        registration_page.fill_gender('Male')

    with allure.step('Заполняем номер телефона'):
        registration_page.fill_phone_number('5555555555')

    with allure.step('Заполняем дату рождения'):
        registration_page.fill_date_of_birth(15,5,1995)

    with allure.step('Заполняем предмет'):
        registration_page.fill_subject('Hist')

    with allure.step('Заполняем хобби'):
        registration_page.fill_hobby('Sports')

    with allure.step('Отправляем файл'):
        registration_page.send_file('my_file.png')

    with allure.step('Заполняем адрес регистрации'):
        registration_page.fill_adress('test street address')

    with allure.step('Заполняем штат и город'):
        registration_page.fill_state_city('NCR','Delhi')

    with allure.step('Отправляем форму'):
        registration_page.submit()

    with allure.step('Проверка результата'):
        registration_page.should_have_registered('John Smith','example@mail.ru','Male','5555555555','15 May,1995','History','Sports','my_file.png','test street address','NCR Delhi')









