import pytest
import allure


@allure.title("Verify Google title")
def test_google_title(setup):
    driver = setup
    driver.get("https://www.google.com")
    assert "Google" in driver.title


@allure.title("Dummy Passing Test")
def test_dummy_pass():
    x = 10
    y = 20
    assert x + y == 30


@allure.title("Dummy Failing Test")
def test_dummy_fail():
    a = "Hello"
    b = "World"
    assert a == b   # This will FAIL on purpose


@allure.title("Dummy Skipped Test")
@pytest.mark.skip(reason="Skipping for demo")
def test_dummy_skip():
    assert True
