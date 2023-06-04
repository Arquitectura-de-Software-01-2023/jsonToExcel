# Proyecto de Conversión de JSON a Excel y Envío de Correo

Este proyecto utiliza Python y se despliega en AWS Lambda para convertir un archivo JSON a Excel y enviar un correo electrónico con un enlace de descarga obtenido de Amazon S3.

## Requisitos

Antes de ejecutar este proyecto, asegúrate de tener los siguientes requisitos en su lugar:

- Python 3.9 o una versión posterior instalada en tu entorno de desarrollo local.
- Una cuenta de Amazon Web Services (AWS) con acceso a los servicios necesarios, como Lambda, S3 y SES.
- La AWS Command Line Interface (CLI) configurada con las credenciales de tu cuenta de AWS.

## Configuración

Sigue estos pasos para configurar el proyecto:

1. Clona este repositorio en tu máquina local:

git clone ("ssh refer")

2. Dirigete a la carpeta python-aws
3. Haz deploy del proyecto con "serverless":

serverless deploy

* Asegurate de tener configurado tus credenciales de AWS

4. Una vez creado el lambda, descarga este archivo .zip:

https://drive.google.com/file/d/1VTrDxZxMdbo7lAhTrJPwMnmYqZAtjsru/view?usp=sharing

5. Dirigete al lambda creado y ve a la sección de (layers). Crea un nuevo layer y sube el archivo .zip descargado anteriormente:

![.zip](https://github.com/Arquitectura-de-Software-01-2023/jsonToExcel/assets/116527334/67d51268-19ee-400d-bbf2-1c2847878106)

6. Dirigite a capas y asigna el layer creado anteriormente.


