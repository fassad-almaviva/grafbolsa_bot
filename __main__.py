# -*- coding: utf-8 -*-

DIRECTOTY_PACKAGE = 'grafbolsa_bot'
HORARIOS_EXECUCAO = [ \
    '08:00', '08:30', \
    '09:00', '09:30', \
    '10:00'
]

### Dependences
from sys import platform
import os, sys, traceback
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By

# bibliotecas externas para funções neste programa
from _library.webdriver import WebDriverChrome, Browser

if platform == "win32":
    # windows
    from _library.database import Database

elif platform == "darwin":
    # os x
    from _library.database_freetds import Database

# elif platform == "linux" or platform == "linux2":
#   linux
#   from _library.database_freetds import Database

# bibliotecas de ações principais do sistema
from .navegate import get_tables


# fluxo principal em funcion para facilitar implementação em thread e try/exception
def start():

    try:
        
        now = time.time()
        mlsec = repr(now).split('.')[1][:3]
        print ('OK:' + str(time.strftime("%Y-%m-%d %H:%M:%S.{}".format(mlsec), time.localtime(now))) + ":" + str(__name__) + " - start do sistema")

        now = time.time()
        mlsec = repr(now).split('.')[1][:3]
        print ('OK:' + str(time.strftime("%Y-%m-%d %H:%M:%S.{}".format(mlsec), time.localtime(now))) + ":" + str(__name__) + " - conectando ao servidor de banco de dados")
        
        # Acesso exclusivo ao banco [MonitorBolsa]
        server = 'sp0001bi0001.cuakt7l44eqc.sa-east-1.rds.amazonaws.com'
        database = 'MonitorBolsa'
        username = 'bot_grafbolsa'
        password = '1q2w3e'
        dba = Database (server, database, username, password)
        dba.connect()

        now = time.time()
        mlsec = repr(now).split('.')[1][:3]
        print ('OK:' + str(time.strftime("%Y-%m-%d %H:%M:%S.{}".format(mlsec), time.localtime(now))) + ":" + str(__name__) + " - inicializando webdriver")
        
        # Inicialização do WebDriver com perfil para permitir restaurar ultima sessão
        
        if platform == "win32":
            # windows
            executable_path = './_requerements/chromedriver_win32/chromedriver'

        elif platform == "darwin":
            # os x
            executable_path = './_requerements/chromedriver_mac64/chromedriver'

        # elif platform == "linux" or platform == "linux2":
        #   linux
        #   executable_path = './_requerements/chromedriver_linux/chromedriver'

        driver = WebDriverChrome ( \
            profile_location='./' + str(DIRECTOTY_PACKAGE) + '/grafbolsa_project_chrome_profile', \
            executable_path=executable_path \
        )
        driver.set_options (new_argument='--disable-dev-shm-usage')   # Opção para desabilitar recursos de desenvolvedor - economiza custo da memória
        driver.set_options (new_argument='--disable-gpu')    # Opção para economizar processamento de vídeo
        driver.set_options (new_argument='--no-sandbox') # Opção para teste de versões Beta da aplicação

        browser = Browser( \
            browser=driver.set_browser( \
                url=fr'http://www.grafbolsa.com/index.html' \
            ) \
        )
        
        time.sleep(5)   # tempo para rendenização gráfica do website
        assert \
            browser.current_url() == \
            fr'http://www.grafbolsa.com/index.html'

        now = time.time()
        mlsec = repr(now).split('.')[1][:3]
        print ('OK:' + str(time.strftime("%Y-%m-%d %H:%M:%S.{}".format(mlsec), time.localtime(now))) + ":" + str(__name__) + " - aguardando próximo horário para exportação")

        # GrafBolsa Export Page
        while True:
            
            try:

                now = time.time()
                mlsec = repr(now).split('.')[1][:3]
                print ('OK:' + str(time.strftime("%Y-%m-%d %H:%M:%S.{}".format(mlsec), time.localtime(now))) + ":" + str(__name__) + " - verificação periódica do status da página web")

                browser = Browser( \
                    browser=driver.set_browser( \
                        url=fr'http://www.grafbolsa.com/index.html' \
                    ) \
                )
                
                time.sleep(5)   # tempo para rendenização gráfica do website
                assert \
                    browser.current_url() == \
                    fr'http://www.grafbolsa.com/index.html'

                if (len([hr for hr in HORARIOS_EXECUCAO if str(time.strftime("%H:%M")) in hr]) > 0):
                
                    ###
                    ### Exportar a primeira tabela de Alta Liquidez
                    ###

                    now = time.time()
                    mlsec = repr(now).split('.')[1][:3]
                    print ('OK:' + str(time.strftime("%Y-%m-%d %H:%M:%S.{}".format(mlsec), time.localtime(now))) + ":" + str(__name__) + " - obtendo informações das ações de alta liquidez")
                    
                    browser = Browser( \
                        browser=driver.set_browser( \
                            url=fr'http://www.grafbolsa.com/index.html' \
                        ) \
                    )
                    
                    time.sleep(5)   # tempo para rendenização gráfica do website
                    assert \
                        browser.current_url() == \
                        fr'http://www.grafbolsa.com/index.html'

                    results = []
                    sql_querys = []
                    results = get_tables(browser=browser).export()
                    
                    id = 3
                    while id < len (results):
                        
                        insert_sql_line = \
                        'insert ' \
                            'grafbolsa.AltaLiquidez ' \
                            '(data, nome, fech, oscil, neg, vol, liq, var5, var30, var180, cod) ' \
                        'values ' \
                            '( ' \
                            '   convert (date, getdate()-1)' \
                            ',  \'' + (results[id]['Nome']) + '\'' \
                            ',  \'' + (results[id]['Fechamento']) + '\'' \
                            ',  \'' + (results[id]['Oscilação']) + '\'' \
                            ',  \'' + (results[id]['Negociação']) + '\'' \
                            ',  \'' + (results[id]['Volume']) + '\'' \
                            ',  \'' + (results[id]['Liquidez']) + '\'' \
                            ',  \'' + (results[id]['Variação 5 dias']).replace('-', '-0') + '\'' \
                            ',  \'' + (results[id]['Variação 30 dias']).replace('-', '-0') + '\'' \
                            ',  \'' + (results[id]['Variação 6 meses']).replace('-', '-0') + '\'' \
                            ',  \'' + (results[id]['Código']) + '\'' \
                            ') '
                        
                        sql_querys.append(
                            insert_sql_line
                        )
                        
                        id = id + 1

                    for query in sql_querys:
                        dba.insert (query)

                    now = time.time()
                    mlsec = repr(now).split('.')[1][:3]
                    print ('OK:' + str(time.strftime("%Y-%m-%d %H:%M:%S.{}".format(mlsec), time.localtime(now))) + ":" + str(__name__) + " - foram adicionados " + str(len(results)) + " ações de alta liquidez ao banco de dados")
                    
                    del results
                    del sql_querys

                    ###
                    ### Exportar a primeira tabela de Média Liquidez
                    ###

                    now = time.time()
                    mlsec = repr(now).split('.')[1][:3]
                    print ('OK:' + str(time.strftime("%Y-%m-%d %H:%M:%S.{}".format(mlsec), time.localtime(now))) + ":" + str(__name__) + " - obtendo informações das ações de média liquidez")

                    browser = Browser( \
                        browser=driver.set_browser( \
                            url=fr'http://www.grafbolsa.com/liqbai.html' \
                        ) \
                    )
                    
                    time.sleep(5)   # tempo para rendenização gráfica do website
                    assert \
                        browser.current_url() == \
                        fr'http://www.grafbolsa.com/liqbai.html'

                    results = []
                    sql_querys = []
                    results = get_tables(browser=browser).export()
                    
                    id = 3
                    while id < len (results):
                        
                        insert_sql_line = \
                        'insert ' \
                            'grafbolsa.MediaLiquidez ' \
                            '(data, nome, fech, oscil, neg, vol, liq, var5, var30, var180, cod) ' \
                        'values ' \
                            '( ' \
                            '   convert (date, getdate()-1)' \
                            ',  \'' + (results[id]['Nome']) + '\'' \
                            ',  \'' + (results[id]['Fechamento']) + '\'' \
                            ',  \'' + (results[id]['Oscilação']) + '\'' \
                            ',  \'' + (results[id]['Negociação']) + '\'' \
                            ',  \'' + (results[id]['Volume']) + '\'' \
                            ',  \'' + (results[id]['Liquidez']) + '\'' \
                            ',  \'' + (results[id]['Variação 5 dias']).replace('-', '-0') + '\'' \
                            ',  \'' + (results[id]['Variação 30 dias']).replace('-', '-0') + '\'' \
                            ',  \'' + (results[id]['Variação 6 meses']).replace('-', '-0') + '\'' \
                            ',  \'' + (results[id]['Código']) + '\'' \
                            ') '
                        
                        sql_querys.append(
                            insert_sql_line
                        )
                        
                        id = id + 1

                    for query in sql_querys:
                        dba.insert (query)

                    now = time.time()
                    mlsec = repr(now).split('.')[1][:3]
                    print ('OK:' + str(time.strftime("%Y-%m-%d %H:%M:%S.{}".format(mlsec), time.localtime(now))) + ":" + str(__name__) + " - foram adicionados " + str(len(results)) + " ações de média liquidez ao banco de dados")
                    
                    del results
                    del sql_querys

                    ###
                    ### Fim do programa principal
                    ###

                    now = time.time()
                    mlsec = repr(now).split('.')[1][:3]
                    print ('OK:' + str(time.strftime("%Y-%m-%d %H:%M:%S.{}".format(mlsec), time.localtime(now))) + ":" + str(__name__) + " - aguardando próximo horário para exportação ...")

            except Exception as ecp:
                print (sys.exc_info())
                print (traceback.print_exc(file=sys.stdout))
                try:
                    now = time.time()
                    mlsec = repr(now).split('.')[1][:3]
                    print ('ERRO:' + str(time.strftime("%Y-%m-%d %H:%M:%S.{}".format(mlsec), time.localtime(now))) + ":" + str(__name__) + " - houve uma falha no processo atual")
                    print (str(sys.exc_info()[0]))
                    browser.quit()
                
                except:
                    pass

                raise ecp
                
            else:
                
                time.sleep(60)

                # restart:
                continue

    except:
        print (sys.exc_info())
        print (traceback.print_exc(file=sys.stdout))
        try:
            now = time.time()
            mlsec = repr(now).split('.')[1][:3]
            print ('ERRO:' + str(time.strftime("%Y-%m-%d %H:%M:%S.{}".format(mlsec), time.localtime(now))) + ":" + str(__name__) + " - ocorreu uma falha que fez o sistema retornar ao fluxo principal. a reinicialização do programa foi feita para evitar a interrupção da rotina")
            print (str(sys.exc_info()[0]))
            browser.quit()
        
        except:
            pass

    finally:
        pass

# fluxo principal do programa - manter sempre disponível para reiniciar em caso de falha
while True:
    start()