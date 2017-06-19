'''
Created on 20 de jan de 2016

@author: Diego
'''
import time

from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.select import Select

#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#from selenium.webdriver.common.keys import Keys



class DjangoWebTest:

    web_controller = None
    project_url = None

    def login(self,email,password):
        if self.web_controller.enter_text('email',email) and self.web_controller.enter_text('password', password) and self.web_controller.click('button_send'):
            print("CONSEGUI ESCREVER")
        else:
            print("NAO CONSEGUI ESCREVER")


    def __init__(self,project_url=None):
        if project_url is not None:
            self.project_url = project_url
            self.web_controller = WebController()
            self.load_page(self.project_url)

    def load_page(self,url):
        if self.web_controller is None:
            self.web_controller = WebController()

        if "http://" not in url:
            url = "http://" + url
        self.web_controller.load_page(url)

    def get_title(self):
        return self.web_controller.get_title()

    def close(self):
        self.web_controller.close()


class WebController:

    controle_componentes  = None
    link = None
    driver = None
    component = None
    
    def __init__(self,extensoes=[]):
        self.load_controllers(extensoes)

    def get_title(self):
        return self.driver.title

    def load_page(self, url):
        self.driver.get(url)
        try:
            pass
        except:
            print("Falha no carregamento da pagina: ",url)
            self.close()
        
    def maximize_window(self):
        self.driver.maximize_window()
    
    def load_controllers(self, extensoes=[]):
        binary = FirefoxBinary(settings.MOZILLA_FIREFOX_TEST_PATH)
        capabilities = webdriver.DesiredCapabilities().FIREFOX
        capabilities["marionette"] = True
        try:
            self.driver = webdriver.Firefox(firefox_binary=binary,executable_path=settings.SELENIUM_GECKODRIVER_MOZILLA,capabilities=capabilities)
            self.driver.maximize_window()

            """ Especificando extensoes
            profile = webdriver.FirefoxProfile()
            for item in extensoes:
                profile.add_extension(extension=item)
            self.driver = webdriver.Firefox(firefox_profile=profile) """
            
            """ Carregar Mozilla Simples """

            
        except:
            print("Navegador nao pode ser aberto. Pode ser necessario atualiza-lo antes.")
            exit(0)

    def get_component(self, metodo, valor):
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait

        #print "Buscando Elemento: ",valor
        wait = WebDriverWait(self.driver, 5)
        try:
            element = wait.until(EC.element_to_be_clickable((metodo,valor)))
            return element
        except:
            
            time.sleep(2)
            try:
                self.component = self.driver.find_element(metodo, valor)
                return self.component
            except:
                #print "Busca por elemento excedeu o tempo maximo.",valor
                return None
    
    def select(self, identificador, opcao):
        self.component = self.get_component(By.ID, identificador)
        if self.component != None:
            Select(self.component).select_by_value(opcao)
            return True
        return False
        
    def click(self, identificador):
        self.component = self.get_component(By.ID, identificador)
        if self.component != None:
            try:
                self.component.click()
                return True
            except:
                #print "Erro! Componente nao pode ser clicado.."
                return False
            
            #try:
                #print "encontrei o componente.. vou tentar clicar",self.componente.text
                
            #    return True
            #except:
            #    print "Componente localizado, mas nao consegui clicar: ",identificador
            #    print "olha o elemento: ",self.componente
            #    self.componente.click()
        return False
    
    def enter_text(self, identificador, texto):
        self.component = self.get_component(By.ID, identificador)
        if self.component != None:
            self.component.send_keys(texto)
            return True
        return False
        
    def clear_field(self, identificador):
        self.component = self.get_component(By.ID, identificador)
        if self.component != None:
            self.component.clear()
            return True
        return False
    
    def print_screen(self,path):
        self.driver.save_screenshot(path)

    def iniciar(self, url):
        self.link = url
        self.load_page(url)

    def close(self):
        self.driver.close()
        try:
            alert = self.controlador.driver.switch_to_alert()
            alert.accept()

        except:
            pass

        time.sleep(1)
        try:
            alert = self.controlador.driver.switch_to_alert()
            alert.accept()
        except:
            pass
