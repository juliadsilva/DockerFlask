# Docker

Este repositóro guarda uma aplicação simples que utiliza um container em Docker para prover uma aplicação Flask, que irá disponibilizar 4 páginas web.

---

## Como utilizar

Para utilizar, basta abrir um terminal na pasta raiz da aplicação (Docker) e digitar os seguintes comandos:

```
$ > docker build -t flask_docker .
$ > docker run -d -p 4200:80 --name= flask_docker -v [CAMINHO DA PASTA]:/app  flask_docker 
```

Abra o navegador no endereço http://localhost:4200

Para parar e deletar o container, digite:


```
$ > docker stop flask_docker .
$ > docker rm flask_docker 
```

---

## Autora

Julia Daniele Moreira Da Silva