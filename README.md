# GRAFBOLSA | Extração automatizada
> Sistema de coleta automatizada das informações do site grafbolsa usado para simulação, histórico e previsão da bolsa de valores


## Executando o programa

Siga o passo a passo abaixo para executar o código dessa aplicação:

1.  Acessar o ambiente virtual existente deste projeto, execute, no PowerShell, a partir da pasta que contém a pasta do projeto ``grafbolsa_bot``:

    - No Windows, execute:

    ```
    grafbolsa_bot\Scripts\activate
    ```

    - No Unix ou no MacOS, execute:

    ```
    source grafbolsa_bot/bin/activate
    ```

2.  Por fim, execute:

    ```
    python -m grafbolsa_bot
    ```

3.  Para sair do ambiente virtual, execute:

    ```
    deactivate
    ```


## Editando o projeto

**O que você precisa saber antes de iniciar a edição deste projeto?**

Para editar este projeto, você precisará:

1.  Instalar Microsoft .NET Framework 4.5.1
2.  Instalar Python 3.8.2
3.  Configurar ambiente virtual
4.  Instalar pacotes e dependências do projeto no ambiente virtual
5.  "Congelar" as versões das bibliotecas utilizadas no projeto


**Por que o ambiente virtual é necessário?**

> Para reduzir o tamanho da compilação do ``.exe`` ao final da edição e também manter o mesmo padrão das bibliotecas e dependências afim de manter a compatibilidade entre os sistemas

> Foram utilizados versões específicas de cada biblioteca incluso neste projeto. Ao editar/atualizar o projeto, não necessariamente terá que redefinir o código por conta de uma versão mais atualizada das bibliotecas na máquina de destino pois precisará atualizar a biblioteca neste ambiente virtual e compilar uma nova versão para que as alterações entrem em vigor. Isto isola o projeto e o mantém sempre funcionando com a versão para qual a biblioteca foi desenhada.


### Acessando o ambiente virtual existente

Para acessar o ambiente virtual existente para este projeto, execute, no PowerShell, de dentro da pasta ``grafbolsa_bot`` que contém os arquivos deste projeto:

- No Windows, execute:

```
Scripts\activate
```

- No Unix ou no MacOS, execute:

```
source bin/activate
```

- Para sair do ambiente virtual, execute:

```
deactivate
```


### Criar um novo ambiente virtual para este projeto
> Caso não tenha criado o ambiente virtual, siga o passo a passo para criar um novo ambiente virtual para este projeto:

1. Microsoft .NET Framework

    - Instalar Microsoft .NET Framework 4.5.1

2. Python 3.8.2

    - Vem instalado em todos sistemas operacionais, exceto o windows

    - Para instalar no windows, [clique aqui e veja como](https://python.org.br/instalacao-windows/)

3. Ambiente virtual

    - Instalar virtualenv, [clique aqui e veja como](https://virtualenv.pypa.io/en/latest/installation.html#via-pip)

    - Para criar a máquina virtual, vá até a pasta que contém a pasta do projeto e execute, no PowerShell:

        > Importante lembrar que o nome da pasta que contém o projeto tem que ser o mesmo nome que está escrito na função a ser executada acima
        
        ```
        python -m venv grafbolsa_bot
        ```

    - Para acessar a máquina virtual, execute, no PowerShell, de dentro da pasta ``grafbolsa_bot`` que contém os arquivos deste projeto:

        No Windows, execute:

        ```
        Scripts\activate
        ```

        No Unix ou no MacOS, execute:

        ```
        source bin/activate
        ```

        Para sair do ambiente virtual, execute:

        ```
        deactivate
        ```

    Para que os passos acima sejam executados com sucesso, será necessário revisar a política de execução do scripts do PowerShell. Execute, no PowerShell:

    ```
    Get-ExecutionPolicy -List
    ```

    Caso ``Scope ExecutionPolicy`` esteja diferente de ``Remotesigned``, execute, no PowerShell:

    ```
    Set-ExecutionPolicy -ExecutionPolicy Remotesigned -Scope Process
    ```

4. Instalando os pacotes e dependências deste projeto no ambiente virtual.

    - Execute, no PowerShell, de dentro da pasta do projeto ``grafbolsa_bot`` que contém os arquivos do projeto:

        ```
        python -m pip install -r requirements.txt
        ```

5.  "Congelar" as versões das bibliotecas utilizadas no projeto.

    - Instale ou atualize as novas bibliotecas utilizadas neste projeto dentro do ambiente virtual. Feito isso execute, no PowerShell, de dentro da pasta do projeto ``grafbolsa_bot`` que contém os arquivos do projeto:

        ```
        pip list
        pip freeze > requirements.txt
        ```

        > Isto fará o registro dos nomes e versões das bibliotecas usadas na construção/edição deste projeto no arquivo ``requirements.txt`` na pasta do projeto, que poderá ser lido posteriormente, caso necessário, pelo instalador PIP do Python usando o exemplo do código executado no item 4.


## Revisões deste projeto

Versão/Tags | Data edição | Branch(s)   | Data Publicação | Status                   | Publicado por
------------| ----------- | ----------- | --------------- | ------------------------ | --------------------------------------------------------
v1.0.0      | 2021-08-01  | STABLE      | 2021-08-01      | GO-LIVE                  | [Assad, Felipe](mailto:felipe@felipeassad.com.br)