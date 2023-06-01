import json
import pandas as pd
import io
import boto3
from datetime import datetime

def lambda_handler(event, context):
    print("======================")
    print(event)
#    print(event['body'])
    dat = event['body']
    finalDat = json.loads(dat)
    print(finalDat['data'])
    dfRes = returnExcel(finalDat['data'])
    
    with io.BytesIO() as output:
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            dfRes.to_excel(writer)
        data = output.getvalue()
    s3 = boto3.resource('s3')
    name =  datetime.now()
    nameStr = str(name).replace(" ","_").replace("-","_").replace(":", "_").replace(".", "__")
    fullName = f"reporte_{nameStr}.xlsx"
    s3.Bucket('my-custom-bucket-one-emer').put_object(Key=fullName, Body=data)

   

    url = boto3.client('s3').generate_presigned_url(
           ClientMethod='get_object', 
           Params={'Bucket': 'my-custom-bucket-one-emer', 'Key': fullName},
            ExpiresIn=3600)  # seconds
    
    lambda_client = boto3.client('lambda', region_name='us-weast-2')
    payload = {
        'email': finalDat['email'],
        'url': url,
    }
    invoke_response = lambda_client.invoke(
        FunctionName='email-python-dev-hello',
        InvocationType='Event',
        Payload=json.dumps(payload)
    )


    return {
        'statusCode': 200,
        'body': json.dumps({"url":url, "name": fullName})
    }

def returnExcel(responseList: list):
    '''
    response = [
        {
            "number": 1,
            "top": "Pérdida de Control de Acceso (Broken Access Control)",
            "questions": [
                "¿Se implementan restricciones de acceso adecuadas para garantizar que los usuarios solo puedan acceder a los recursos autorizados?",
                "¿Se verifica que los usuarios autenticados no puedan realizar acciones no permitidas sin la debida autorización?",
                "¿Se aplican controles de acceso para evitar la manipulación de parámetros o URLs para acceder a funcionalidades no autorizadas?"
            ],
            "answers": [0, 0, 0]
        }
    ]
    '''
    mapRes = {
        "0": "Bajo",
        "1":"Medio",
        "2": "Alto"
    }
    data = pd.DataFrame(
        {
            "Número": [],
            "Top": [],
            "Pregunta":[],
            "Respuesta": []
        }
    )
    for res in responseList:
      for ind in range(len(res["questions"])):
        da = pd.DataFrame({
            "Número": [str(res["number"])],
            "Top": [res["top"]],
            "Pregunta": [res["questions"][ind]],
            "Respuesta": [mapRes[str(res["answers"][ind])]]
        })
        data = pd.concat([data, da],  ignore_index=True)
    
    return data
