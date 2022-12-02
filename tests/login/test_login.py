import time
import pytest


@pytest.mark.parametrize('login,password,expectation', [
    ('ajax.app.automation@gmail.com', 'qa_automation_password', False),  # логін- , пароль+
    ('qa.ajax.app.automation@gmail.com', 'qa_automation_password', True),  # логін+ , пароль+
    ('qa.ajax.app.automation@gmail.com', '_automation_password', False),  # логін+ , пароль-
    ('ajax.app.automation@gmail.com', '_automation_password', False)  # логін- , пароль-
])
def test_user_login(user_login_fixture, login, password, expectation):
    value = user_login_fixture
    time.sleep(1)
    value.tap_login()
    time.sleep(1)

    value.input_login(login)
    value.input_pass(password)
    value.auth_tap()
    try:
        time.sleep(15)  # такий сліп бо ноут не вивозить
        value.popup_tap()
        time.sleep(5)
        value.logout()
        time.sleep(1)
        assert expectation
    except:
        assert False == expectation

# pytest -s -v tests/login/test_login.py
