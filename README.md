# Sumário  
1. [Estrutura da Aplicação](#1-estrutura-da-aplicação)  
1.1. [Companies](#11-companies)  
1.2. [Vehicles](#12-vehicles)  
1.3. [Parking (Parking Controller)](#13-parking)
1.4. [Setup](#14-setup)
2. [Como iniciar a aplicação](#2-iniciar-a-aplicação)  
2.1. [Clonar o repositório](#21-clonar-o-repositório)  
2.2. [Criar ambiente virtual](#22-criar-ambiente-virtual)  
2.3. [Instalar python](#23-instalar-python)  
2.4. [Instalar dependências](#24-instalar-dependências)  
2.5. [Secret Key](#25-secret-key)
2.6. [Base de dados](#26-base-de-dados)
2.7. [Iniciar o projeto](#27-iniciar-o-projeto)  
3. [Utilizando a aplicação](#3-utilizando-a-aplicação)  
3.1.1. [Companies POST](#311-companies-post)  
3.1.2. [Companies PUT](#312-companies-put)  
3.1.3. [Companies GET](#313-companies-get)  
3.1.4. [Companies DELETE](#314-companies-delete)  
3.1.5. [Vehicles_Brands POST](#315-vehicles_brands-post)  
3.1.6. [Vehicles_Brands PUT](#316-vehicles_brands-put)  
3.1.7. [Vehicles_Brands GET](#317-vehicles_brands-get)  
3.1.8. [Vehicles_Brands DELETE](#318-vehicles_brands-delete)  
3.1.9. [Vehicles_Models POST](#319-vehicles_models-post)  
3.1.10. [Vehicles_Models PUT](#3110-vehicles_models-put)  
3.1.11. [Vehicles_Models GET](#3111-vehicles_models-get)  
3.1.12. [Vehicles_Models DELETE](#3112-vehicles_models-delete)  
3.1.13. [Vehicles POST](#3113-vehicles-post)  
3.1.14. [Vehicles PUT](#3114-vehicles-put)  
3.1.15. [Vehicles GET](#3115-vehicles-get)  
3.1.16. [Vehicles DELETE](#3116-vehicles-delete)    
3.1.17. [Parking VEHICLE_IN](#3117-parking-vehicle_in)  
3.1.18. [Parking VEHICLE_OUT](#3118-parking-vehicle_out)

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
A aplicação companies segue o modelo MVT padrão do Django com a pattern "normalized models", "service objects" e "model mixins", sendo:
```shell
    |--companies
        |--migrations
        |--admin.py
        |--apps.py
        |--models.py
        |--services.py
        |--testes.py
        |--urls.py
        |--views.py
```
```migrations``` => Utilizado pelo Django ORM para migrações do banco de dados.  
```admin.py``` => Ainda não utilizado pela aplicação.  
```apps.py``` => Ainda não utilizado pela aplicação.  
```models.py``` => Contém as classe companies e seus métodos. A maioria da lógica da aplicação encontra-se aqui (M is bigger than V and C).  
```services.py``` => Divide responsabilidades com models.py, principalmente em tarefas rotineiras (como consumo de API, processamento de objetos, etc) e recebe funções genéricas que podem ser utilizadas por outras aplicações no futuro.
```testes``` => Ainda não utilizado pela aplicação.  
```urls``` => Arquivo de rotas da aplicação.  
```views``` => Request / Response da aplicação. 

### 1.2. Vehicles
A aplicação vehicles segue o modelo MVT padrão do Django com a pattern "normalized models" e "service objects", sendo:
```shell
    |--companies
        |--models
            |--__init__.py
            |--Vehicles_Brands.py
            |--Vehicles_Models.py
            |--Vehicles.py
        |--services.py
        |--testes.py
        |--urls.py
        |--views.py
```  
```models``` => Pasta contendo as classe necessárias para vehicles e seus métodos.  
```__init__.py``` => Arquivo responsável por carregar todos os modelos da pasta. Caso um novo modelo seja criado, ele deve ser importado nesse arquivo.  
```Vehicles_Brands``` => Model responsável pelo CRUD das fabricantes de veículos. Possui relação com Vehicles_Models.  
```Vehicles_Models```  => Model responsável pelo CRUD dos modelos de veículos. Possui relação com Vehicles_Brands e Vehicles.   
```Vehicles```  => Model responsável pelo CRUD dos veículos. Possui relação com Vehicles_Brands e Vehicles_Models.  
```services.py``` => Divide responsabilidades com models, principalmente em tarefas rotineiras (como consumo de API, processamento de objetos, etc) e recebe funções genéricas que podem ser utilizadas por outras aplicações no futuro e por mais de um modelo da pasta models.   

### 1.3. Parking
A aplicação parking segue o modelo MVT padrão do Django com a pattern "normalized models", sendo:
```shell
    |--companies
        |--models.py
        |--testes.py
        |--urls.py
        |--views.py
``` 
```models.py``` => Realiza o controle de entrada e saída de veículos e contabiliza o tempo estacionado. Futuramente pode ser necessário um arquivo services.py 

### 1.4. Setup
Setup contém as configurações gerais de toda a aplicação e funções comuns a todas as aplicações.
```shell
    |--setup
        |--asgi.py
        |--services.py
        |--settings.py
        |--urls.py
        |--wsgi.py
``` 
```asgi.py``` => Pasta com configuração padrão do Django.  
```services.py``` => Contém funções genéricas utilizadas por mais de uma aplicação incluindo funções padronização de objetos e de manipulação para impressão.  
```urls``` => Recebe as rotas de cada aplicação (cada aplicação possui seu próprio arquivo de rotas),
caso uma aplicação seja acrescentada é necessário importar suas rotas aqui.  
```wsgi```  => Pasta com configuração padrão do Django.  

## 2. Iniciar a aplicação

### 2.1. Clonar o repositório

Navegue até a pasta de destino e execute:
```shell
    git clone https://github.com/lucasmdpereira/django_parking_challenge.git
```

Caso queira atualizar a versão de desenvolvimento:
```shell
    git checkout dev && git push origin dev
```

### 2.2. Criar ambiente virtual

Recomenda-se utilizar um ambiente virtual para evitar conflito entre as versões utilizadas e instaladas.
Para isso, na pasta do projeto:
```shell
    python3 venv venv
```

Inicie o ambiente virtual:
```shell
    source venv/bin/activate
```

Para sair do ambiente virtual:
```shell
    deactivate
```

### 2.3. Instalar python
Instale a versão correta do python de acordo com seu ambiente.
A versão utilizada no projeto pode ser encontrada no arquivo .tool-versions

### 2.4. Instalar dependências
Para instalar as dependências, confira se o arquivo requirements.txt está na pasta raiz e execute:
```shell
    pip install -r requirements.txt
```

### 2.5. Secret Key
A chave secreta do projeto deve ficar no arquivo .env, para gerar uma nova chave acesse:
Você pode utilizar a um chave geral como ´´´kb&kcwdqg)!c_uld-^zk)s#gpc0#u#8kwt@%a6u6x*2gy1$z)c´´´ ou gerar uma chave individual em https://djecrety.ir/.

No arquivo .env deve constar a chave, conforme o exemplo:
```python
SECRET_KEY = 'django-insecure-kb&kcwdqg)!c_uld-^zk)s#gpc0#u#8kwt@%a6u6x*2gy1$z)c'
```

### 2.6. Base de dados
A aplicação possui uma base de dados em sqlite pré configurada. Outros banco de dados sql são facilmente configuráveis em:
```shell
    |--setup
        |--settings.py
```

Para iniciar uma base de dados em sqlite apenas execute:
```shell
    python manage.py makemigrations
    python manage.py migrate
```

### 2.7. Iniciar o projeto
Para iniciar o projeto:
```python manage.py runserver```

## 3. Utilizando a aplicação
Para correto funcionamento da aplicação temos que criar pelo menos uma entrada para companies e vehicles. A partir daí podemos utilizar as rotas contidas sem parking.urls para cadastrar a entrada e saída de veículos

### 3.1 Criando entradas no banco de dados

#### 3.1.1. Companies POST
Utilizando o postman ou insomnia, envie o objeto json:
```shell
    http://127.0.0.1:8000/companies/post
    {
        "address": {
            "cep": "1111111",
            "street": "street",
            "number": "1",
            "others": "others"
        },
        "name": "name",
        "cnpj": "1",
        "phone": "5500900000000",
        "bike_parking_spots": 10,
        "car_parking_spots": 5
    }
```
#### 3.1.2. Companies PUT
Utilize a rota put para atualizar qualquer dado de endereço ou da empresa.

```shell
    http://127.0.0.1:8000/companies/put/1
    {
        "name": "name PUT",
        "address": {
            "street": "street PUT"
        }
    }
```

#### 3.1.3. Companies GET
```shell
    http://127.0.0.1:8000/companies/get/1
```

#### 3.1.4. Companies DELETE
```shell
    http://127.0.0.1:8000/companies/delete/1
```

#### 3.1.5. Vehicles_Brands POST
```shell
    http://127.0.0.1:8000/vehicles/brands/post 
    {
	    "brand": "bmw"
    }
```

#### 3.1.6. Vehicles_Brands PUT
```shell
    http://127.0.0.1:8000/vehicles/brands/put/bmw
    {
	    "brand": "fiat"
    }
```

#### 3.1.7. Vehicles_Brands GET
```shell
    http://127.0.0.1:8000/vehicles/brands/get/fiat
```

#### 3.1.8. Vehicles_Brands DELETE
```shell
    http://127.0.0.1:8000/vehicles/brands/delete/fiat
```

#### 3.1.9. Vehicles_Models POST
```shell
    http://127.0.0.1:8000/vehicles/models/post  
    {
	    "model": "model",
	    "brand": "bmw"
    }
```
 #### 3.1.10. Vehicles_Models PUT
```shell
    http://127.0.0.1:8000/vehicles/models/put/model  
    {
	    "model": "modelPUT",
	    "brand": "bmw"
    }
```

#### 3.1.11. Vehicles_Models GET
```shell
    http://127.0.0.1:8000/vehicles/models/get/modelPUT
```

#### 3.1.12. Vehicles_Models DELETE
```shell
    http://127.0.0.1:8000/vehicles/models/delete/modelPUT
```

#### 3.1.13. Vehicles POST
```shell
    http://127.0.0.1:8000/vehicles/post  
    {
        "license_plate": "AAA0000",
        "model": "model",
        "type": "car"
    }
```

#### 3.1.14. Vehicles PUT
```shell
    http://127.0.0.1:8000/vehicles/put/AAA0000
    {
        "license_plate": "AAA9999",
        "model": "model"
    }
```

##### 3.1.15. Vehicles GET
```shell
    http://127.0.0.1:8000/vehicles/get/AAA9999
```

#### 3.1.16. Vehicles DELETE
```shell
    http://127.0.0.1:8000/vehicles/delete/AAA9999
```

#### 3.1.17. Parking VEHICLE_IN
```shell
    http://127.0.0.1:8000/parking/in
    {
        "license_plate": "AAA0000",
        "company": "1"
    }
```

#### 3.1.18. Parking VEHICLE_OUT
```shell
    {
        "license_plate": "AAA0000",
        "company": "1"      
    }
```