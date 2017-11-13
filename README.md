## SistemaWeb

### Configurações
  
  - Instalação do Python 3.6.1
    - Windows x86 executable installer (32 Bits): https://www.python.org/ftp/python/3.6.1/python-3.6.1.exe
    - Windows x86 executable installer (64 Bits): https://www.python.org/ftp/python/3.6.1/python-3.6.1-amd64.exe  
    - Linux (DEB): ```sudo apt-get install python3.6```
  
  - Instalação do VirtualEnv
  
    Na versão 3.4 em diante do Python o VirtualEnv faz parte da distribuição, logo não é necessário baixa-lo.
    Leitura Recomendada: https://docs.python.org/3/library/venv.html
    
    Principais comandos: 
      Windows:
      - Criar Ambiente Virtual: ```c:\>python -m venv myenv c:\path\to\myenv```
      - Ativar Ambiente: ```c:\path\to\myenv\Scripts\activate```  
      Linux :
      - Criar Ambiente Virtual: ```$ python -m venv myenv /path/to/myenv```
      - Ativar Ambiente: ```source path/to/myenv/bin/activate```
      - Desativar      : ```deactivate```

- Instalação do GIT
    - Windows: https://git-scm.com/download/win
    - Linux: Pacote nativo nas distribuições Linux.
    
    Leitura recomendada sobre GIT e Politicas de Versionamento:
    
      - https://git-scm.com/book/pt-br/v1/Ramifica%C3%A7%C3%A3o-Branching-no-Git-B%C3%A1sico-de-Branch-e-Merge
      
      - https://git-scm.com/book/pt-br/v1/Ramifica%C3%A7%C3%A3o-Branching-no-Git-Branches-Remotos

- Instalação do NodeJs e Bower.
    - Baixar a versão adequada para o seu sistema operacional diretamente no site https://nodejs.org/en/download/.
    - Instale na pasta de prefencia com configurações padrões.

- Instalação do PyCharm Comunity.
    - Acesse e escolha a versão Comunity para o seu Sistema Operaciona: https://www.jetbrains.com/pycharm/download/

- Configurar o  PyCharm para trabalhar com o Git local e remoto.
    - (Em construção).
    
- Configurar o PyCharm para rodar o projeto usando o ambiente virtual do projeto.
  
    - Acesse o menu: "File > Default Settings" e clicque na sessão Project Interpreter.
    - Clique no botão de configurações.
    - Clique em "Create VirtualEnv".
    - Na campo Name digite "sistemaweb".
    - No campo Location informe a pasta que utiliza para armazenar seus ambientes virtuais.
    - Clique em OK.  
    
    Se o PyCharm utilizado for o Comunity não traz suporte nativo para Django, então configure o PyCharm para rodar o arquivo manage.py diretamente utilizando o python.exe do seu ambiente virtual.
    
    Se o PyCharm utilizado for o Professional a ferramenta possui alguns recursos que dependem de reconhecer o Django no interpretador, contudo se ele estiver em um ambiente virtual seria necessário que ele fosse ligado para isso acontecer, evitando alguns erros por não encontrar o Django, ex: ´´´erro please enable django support for the project´´´. 
    Para isso é preciso habilitar o suporte ao Django na configuração do PyCharm
    
      - Va no menu File > Settings > Languages & Frameworks > Django.
      - Selecione a opção "Enable Django Support".
      - No campo Django Project Root informe a pasta que contem o arquivo settings.py do projeto.
      - Clique em apply e ok.

    Adicionar comandos de execução ao PyCharm.
  
- Instalar dependências Python com através do arquivo requirements.txt do projeto.

- Instalar as dependencias de front-end é necessário ter o ```django-bower``` instalado.
    - A instalação do django-bower é feita através do pip e dos requirements do projeto.
    - No arquivo settings.py altere o ```BOWER_PATH``` para a pasta onde ele esta instalado.
        - Se for no windows: ```C:\Users\{user_folder}\AppData\Roaming\npm\bower.cmd```
        - Se for no Linux: ```VERIFICAR```

- Configure o PyCharm para analisar o código Python com o Pylint (instalado previamente pelos requirements).
    - Acesse o painel File > Settings > Tools > External Tools.
    - Clique para adicionar novo comando.
    - No campo "Name" Informe o nome "pylint-pycharm".
    - No campo "Group" digite "Code Style"
    - Deixar Marcado a opção: "Synchronize files after execution", "Open console".
    - Na sessão "Show in" marcar todas as opções.
    - No campo "Program" digitar "pylint-pychar".
    - No campo "Parameters" digitar "$FileName$".
    - No campo "Working Directory" informar "$FileDir$".
    - Clicar em Apply e OK.

    O Pylint estara analisando em tempo real o codigo fonte sugerindo possiveis melhorias e adequações a padrões de codificação internacional como o PEP8.

- Configurar comandos para executar scripts no Pycharm.
    - bower install :
       - No campo "Name" digite ```bower install```
       - No campo "Script" digite o caminho para o arquivo ```manage.py```
       - No campo "Script parameters" digite ```bower install```
    - behave test :
       - No campo "Name" digite ```behave test```
       - No campo "Script" digite o caminho para o arquivo ```manage.py```
       - No campo "Script parameters" digite ```behave test```
    - makemigrations :
       - No campo "Name" digite ```makemigrations```
       - No campo "Script" digite o caminho para o arquivo ```manage.py```
       - No campo "Script parameters" digite ```makemigrations```
    - migrate :
       - No campo "Name" digite ```migrate```
       - No campo "Script" digite o caminho para o arquivo ```manage.py```
       - No campo "Script parameters" digite ```migrate```
    - runtests :
       - No campo "Name" digite ```runtests```
       - No campo "Script" digite o caminho para o arquivo ```manage.py```
       - No campo "Script parameters" digite ```tests -v 2```
    - runtests entity :
       - No campo "Name" digite ```runtests entity```
       - No campo "Script" digite o caminho para o arquivo ```manage.py```
       - No campo "Script parameters" digite ```test test\unit\backend\entity\ -v 2 --pattern="tests_*.py```
    - runtests entity validators:
       - No campo "Name" digite ```runtests entity validators```
       - No campo "Script" digite o caminho para o arquivo ```manage.py```
       - No campo "Script parameters" digite ```test test\unit\backend\entity\test_validators.py -v 2 --pattern="tests_*.py"```
    - runserver:
       - No campo "Name" digite ```runserver```
       - No campo "Script" digite o caminho para o arquivo ```manage.py```
       - No campo "Script parameters" digite ```runserver 0.0.0.0:8000```
    - backup:
       - No campo "Name" digite ```backup```
       - No campo "Script" digite o caminho para o arquivo ```dbdropbox.py```
       - No campo "Script parameters" digite ```--backup```
    - backup for dropbox:
       - No campo "Name" digite ```upload backup```
       - No campo "Script" digite o caminho para o arquivo ```dbdropbox.py```
       - No campo "Script parameters" digite ```--dbcompress```
    - dropbox restore:
       - No campo "Name" digite ```restore backup```
       - No campo "Script" digite o caminho para o arquivo ```dbdropbox.py```
       - No campo "Script parameters" digite ```--restore```       

- Gerando chave GPG
    - Faça o download e instalação do GPG : https://www.gnupg.org/download/
    - Via linha de comando ou Git Bash digite ```gpg --full-generate-key```.
    - No prompt, especifique o tipo de chave que deseja, ou pressione Enter para aceitar o padrão ```RSA and RSA```.
    - Escolha o tamanho da chave:
        - o tamanho mínimo é 768 bits, o tamanho padrão é 1024 bits e o máximo sugerido é 2048 bits.
    - Especifique o tempo que a chave deve ser válida.
        - 0 = a chave não expira;
        - d = a chave expira em n dias;
        - w = a chave expira em n semanas;
        - m = a chave expira em n meses;
        - y = a chave expira em n anos.
        - 1d equivale a 1 dia.
    - No prompt confirme se tudo está correto digite ```s``` para sim ou ```n``` para não.
    - Digite seu nome completo,não use apelidos ou códigos.
    - Digite seu endereço de e-mail real para gerar sua chave GPG.
    - Use o campo de comentários para incluir apelidos e outras informações.
        - Algumas pessoas usam chaves diferentes para diferentes propósitos e identificam cada chave com um comentário, tal como "Office" ou "Open Source Projects."
    - No prompt de confirmação, digite a letra ```O``` para continuar se todas as entradas estão corretas ou use as outras opções para consertar quaisquer problemas.
    - Finalmente, digite uma frase secreta para sua chave secreta.

### Estrutura
```
<project_root>
├── sistemaweb              <django_project_root>
│  ├── sistemaweb           <configuration_root>
│  │  ├── __init__.py
│  │  ├── settings.py
│  │  ├── urls.py
│  │  └── wsgi.py
│  ├── modules             <aplications_folder>
│  │  ├── core             <main_aplication>
│  │  └── __init__.py
│  ├── conf
│  ├── data
│  │  └── backup
│  ├── logs
│  ├── media
│  ├── requirements
│  │  ├── development.txt
│  │  └── production.txt
│  └── static
│  │  └── bower
│  ├──  media
│  ├──  templates
│  ├──  .bowerrc
│  ├──  .gitignore
│  ├──  bower.json
│  ├──  manage.py
│  └──  README.MD

```

Para adicionar criar um novo modulo (app) basta informar o diretório no comando:

``` python manage.py startapp <nome_modulo> modules/<nome_modulo> ```

É necessário que a pasta onde se deseja criar o módulo exista previamente.

