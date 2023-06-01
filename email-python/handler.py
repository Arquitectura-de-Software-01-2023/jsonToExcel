import json
import boto3

def sendEmail(event, context):
    # Obtener la URL y la dirección de correo electrónico del evento
    url = event['url']
    email = event['email']
    
    # Crear el contenido HTML del correo electrónico
    html_body = f"""
    <html>
    <head></head>
    <body>
      <h1>Evaluación de OWASP</h1>
      <p>Has recibido tu informe, puedes descargarlo de:</p>
      <p><a href="{url}">Tu Informe</a></p>
    </body>
    </html>
    """
    
    # Configurar el cliente de SES (Simple Email Service)
    ses_client = boto3.client('ses', region_name="us-west-2")
    
    # Enviar el correo electrónico
    response = ses_client.send_email(
        Source='emersonchipana12345@gmail.com',
        Destination={
            'ToAddresses': [email]
        },
        Message={
            'Subject': {
                'Data': 'URL recibida'
            },
            'Body': {
                'Html': {
                    'Data': html_body
                }
            }
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Correo electrónico enviado exitosamente')
    }