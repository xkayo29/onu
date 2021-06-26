from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import pyttsx3
from time import sleep

class Automatico:
    def __init__(self):
        self.driver = webdriver.Firefox()
    
    def acessar(self, site):
        try:
            self.driver.get(site)
            sleep(1)
            pyautogui.press('f5')
            sleep(1)
            return True
        except Exception as error:
            print(f'Erro ao iniciar site',error)
            return False
    
    def login(self,user,passw):
        try:
            usuario = self.driver.find_element_by_name('username1')
            usuario.send_keys(user)
            senha = self.driver.find_element_by_name('psd1')
            senha.send_keys(passw)
            
            check = self.driver.find_element_by_id('check_code')
            code = check.get_attribute('value')
            verificar = self.driver.find_element_by_id('verification_code')
            verificar.send_keys(code)
            sleep(1)
            return True
        except Exception as error:
            print(f'Error ao logar, {error}')
            return False
    
    def logar(self):
        try:
            btn_entrar = self.driver.find_element_by_css_selector('body > form:nth-child(7) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(1) > input:nth-child(1)')
            btn_entrar.click()
            sleep(1)
            if 'HGU' in self.driver.title:
                return True
            elif 'PASSWORD' in self.driver.title:
                return 'Trocar'
            else:
                btn_ok = self.driver.find_element_by_css_selector('body > blockquote:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > input:nth-child(1)')
                pyttsx3.speak('Erro de senha...')
                btn_ok.click()
                return False
        except Exception as error:
            print(f'Erro ao clickar em logar {error}')
    
    def trocar_pass(self):
        if 'PASSWORD' in self.driver.title:
            try:
                senha_antiga = self.driver.find_element_by_id('oldPasswd')
                senha_antiga.send_keys('stdONU101')
                
                senha_nova = self.driver.find_element_by_id('newPasswd')
                senha_nova.send_keys('obti0806')
                
                confirma = self.driver.find_element_by_id('affirmPasswd')
                confirma.send_keys('obti0806')
                
                btn_apl = self.driver.find_element_by_xpath('/html/body/blockquote/form/div/table/tbody/tr[9]/td/input[1]')
                btn_apl.click()
                pyttsx3.speak('Troca de senha concluida...')
                return True
            except Exception as error:
                print(f'Error ao tentar trocar senha, {error}')
                return False
        else:
            pass

    
    def caminho(self):
        try:
            pyautogui.click(921,167)
            sleep(1)
            pyautogui.click(694,188)
            sleep(1)
            pyautogui.click(241,417)
            sleep(1)
            pyautogui.click(415,352)
            sleep(2)
            pyautogui.write('HG323DAC_all_V2.0.20-210205_Normalver.tar')
            pyautogui.click(507,444)
            sleep(1)
            pyautogui.click(410,415)
            sleep(1)
            pyautogui.click(665,368)
            pyttsx3.speak('Atualização iniciada com sucesso...')
            return 'OK'
        except Exception as error:
            print(f'Error ao clicar para atualizar, {error}')
            return 'Error'
        
if __name__ == '__main__':
    
    firefox = Automatico()
    acesso = firefox.acessar('http://192.168.1.1')
    if acesso:
        login = firefox.login('admin','stdONU101')
        if login:
            logar = firefox.logar()
            if logar:
                caminho = firefox.caminho()
            if logar == 'Trocar':
                trocar = firefox.trocar_pass()
            else:
                login = firefox.login('admin','obti0806')
                logar = firefox.logar()
                caminho = firefox.caminho()
        
        else:
            print('Pagina nao disponivel')
            
    else:
        print(f'Pagina nao disponivel')
    
