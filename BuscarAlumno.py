import boto3

def lambda_handler(event, context):
    # Entrada (json)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    response = table.get_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )
    item = response.get('Item')
    status = 200 if item else 404
    # Salida (json)
    return {
        'statusCode': status,
        'tenant_id': tenant_id,
        'alumno_id': alumno_id,
        'alumno': item,
        'response': response
    }
