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
  
- Instalar dependências Python com através do arquivo requirements.txt do projeto.

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
