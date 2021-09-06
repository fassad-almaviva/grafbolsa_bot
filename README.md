# GRAFBOLSA | Extração grafbolsa.com.br
> Sistema de coleta automatizada das informações do site grafbolsa usado para simulação, histórico e previsão da bolsa de valores


## Executando o programa

Execute o programa ``.exe`` localizado na pasta ``dist/`` deste projeto.


## Editando o projeto

**O que você precisa saber antes de iniciar a edição deste projeto?**

Para editar este projeto, você precisará:

1.  Instalar Microsoft .NET Framework 4.5.1
2.  Instalar Python 3.8.2
3.  Configurar ambiente virtual
4.  Instalar pacotes e dependências do projeto no ambiente virtual

**Por que o ambiente virtual é necessário?**

> Para reduzir o tamanho da compilação do ``.exe`` ao final da edição e também manter o mesmo padrão das bibliotecas e dependências afim de manter a compatibilidade entre os sistemas

> Foram utilizados versões específicas de cada biblioteca incluso neste projeto. Ao editar/atualizar o projeto, não necessariamente terá que redefinir o código por conta de uma versão mais atualizada das bibliotecas na máquina de destino pois precisará atualizar a biblioteca neste ambiente virtual e compilar uma nova versão para que as alterações entrem em vigor. Isto isola o projeto e o mantém sempre funcionando com a versão para qual a biblioteca foi desenhada.


### Acessando o ambiente virtual existente

Para acessar o ambiente virtual existente para este projeto, execute, no PowerShell, na pasta que contém a pasta deste projeto:

```
activate xxx
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

    - Para criar a máquina virtual, execute, no PowerShell:

        ```
        virtualenv xxx
        ```

    - Para acessar a máquina virtual, execute, no PowerShell:

        ```
        activate xxx
        ```

    Para que os passos acima sejam executados com sucesso, é necessária uma instalação correta do Python e que a pasta ``\nmg_bot\Scripts`` esteja registrada na variavél de ambiente ``path`` caso o sistema operacional seja Windows.

    Também será necessário revisar a política de execução do scripts do PowerShell.
    
    Execute, no PowerShell:

    ```
    Get-ExecutionPolicy -List
    ```

    Caso ``Scope ExecutionPolicy`` esteja diferente de ``Remotesigned``, execute, no PowerShell:

    ```
    Set-ExecutionPolicy -ExecutionPolicy Remotesigned -Scope Process
    ```

4. Instalando os pacotes e dependências deste projeto no ambiente virtual.

    - Execute, no PowerShell, o(s) seguinte(s) código(s):

        ```
        pip install xxx
        ```


## Revisões deste projeto

Versão/Tags | Data edição | Branch(s)   | Data Publicação | Status                   | Publicado por
------------| ----------- | ----------- | --------------- | ------------------------ | --------------------------------------------------------
v1.0.0      | YYYY-MM-DD  | BETA/STABLE | YYYY-MM-DD      | Pré-lançamento / GO-LIVE | [Sobrenome, Nome](mailto:email@almavivadobrasil.com.br)