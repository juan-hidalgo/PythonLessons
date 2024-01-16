# Veremos un procesamiento de múltiples datos tomados desde un archivo csv

from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

# Creación de la sesión en el navegador seleccionado
driver = webdriver.Chrome()

# Maximización de la ventana del navegador
driver.maximize_window()

# detección de errores
try:

    # Ingreso a la página
    driver.get("https://institutoweb.com.ar/test/login.html")

    with open('CursoAutomationPython/data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)

        contador = 0

        for line in reader:
            var_id, var_first_name, var_last_name, var_email, var_gender, var_fav_color = line
            print(var_first_name, var_last_name)

            # Obtención de los elementos mediante selectores
            txt_usuario = driver.find_element(By.ID, "tuusuario")
            txt_clave = driver.find_element(By.ID, "tuclave")
            txt_mail = driver.find_element(By.ID, "tumail")
            btn_ingresar = driver.find_element(By.CSS_SELECTOR, "body > form > button:nth-child(8)")
            # Ejecución de las acciones sobre los elementos
            txt_usuario.send_keys(var_first_name)
            txt_clave.send_keys(var_last_name)
            txt_mail.send_keys(var_email)
            btn_ingresar.click()

            # Obtención de los elementos mediante selectores de la sig.pág.
            link_volver = driver.find_element(By.ID, "volver")
            title_ok = driver.find_element(By.CSS_SELECTOR, "body > h3")
            # Ejecución de las acciones sobre los elementos de la sig.pág.
            texto_assertion = "Acceso INCORRECTO con", var_first_name, var_last_name
            assert "Acceso correcto!" == title_ok.text, texto_assertion
            link_volver.click()
            contador = contador + 1

except AssertionError:
    print("Ocurrió un error de assertion")
except FileNotFoundError:
    print("No se encontró el archivo")
except Exception:
    print("Ocurrió un error")

# Cierre del navegador
driver.quit

print("Se verificaron ", contador, " registros")
