# Sumário  
1. [Estrutura da Aplicação](#estrutura-da-aplicação)  
1.1. [Companies](#companies)


## 1. Estrutura da Aplicação

```shell
    |--Root
        |--companies
        |--vehicles
        |--parking
        |--setup 
``` 

```companies``` => aplicação responsável pelo cadastro e controle das empresas/estacionamentos.    
```vehicles``` => aplicação responsável pelo cadastro e controle dos veículos/clientes.  
```parking``` => aplicação responsável pelo controle de entrada e saída dos veículos/clientes
nas empresas/estacionamentos.    
```setup``` => configurações do projeto.    

### 1.1. Companies
A aplicação companies segue o modelo MVT padrão do Django, sendo:
```shell
    |--companies
        |--migrations
        |--admin.py
        |--apps.py
        |--models.py
        |--testes.py
        |--urls.py
        |--views.py
```
```migrations``` => Utilizado pelo Django ORM para migrações do banco de dados.  
```admin.py``` => Ainda não utilizado pela aplicação.  
```apps.py``` => Ainda não utilizado pela aplicação.  
```models.py``` => Contém as classe companies e seus métodos. A maioria da lógica da aplicação encontra-se aqui (M is bigger than V and C).  
```testes``` => Ainda não utilizado pela aplicação.  
```urls``` => Arquivo de rotas da aplicação.  
```views``` => Request / Response da aplicação.  





