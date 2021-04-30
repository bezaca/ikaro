from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

# Initial Configurations

URL = 'https://sia.unal.edu.co/ServiciosApp/facespublico/public/servicioPublico.jsf?taskflowId=task-flow-AC_CatalogoAsignaturas'
driver = webdriver.Firefox()

# helpers and functions


def waiting_for_cursor(function):
    def wrapper(*args, **kwargs):
        select_element = function(*args, **kwargs)
        # Waiting for the cursor to be available
        WebDriverWait(driver, 20).until(lambda cursor: driver.find_element_by_tag_name(
            "body").value_of_css_property("cursor") != "wait")
        return select_element
    return wrapper


@waiting_for_cursor
def selecting_element_by_id(id_value: str, index_value: int):
    """
    Select the current value on the dropdown element. 
    """
    select_element = driver.find_element(By.ID, id_value)
    return Select(select_element).select_by_index(index_value)


@waiting_for_cursor
def click_button(xpath_value: str):
    """
    Click a button based on the xpath.
    """
    button = driver.find_element_by_xpath(xpath_value)
    return button.click()


# Selecting search parameters
driver.get(URL)

level_of_study = selecting_element_by_id("pt1:r1:0:soc1::content", 1)

"""
      select 1 => Pregrado ,
      2 => Doctorado ,
      3 => Masters y postgrados 
    """
campus = selecting_element_by_id("pt1:r1:0:soc9::content", 6)

"""
Select 1 => Amazonia,
       2 => Bogotá,
       3 => Caribe,
       4 => La Paz,
       5 => Manizales,
       6 => Medellín,
       7 => Orinoquia,
       8 => Palmira,
       9 => Tumaco
"""
faculty = selecting_element_by_id("pt1:r1:0:soc2::content", 1)
syllabus = selecting_element_by_id("pt1:r1:0:soc3::content", 1)

click_button("//div[@id='pt1:r1:0:cb1']")









