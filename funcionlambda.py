import json
import os
import mercadopago

def lambda_handler(event, context):
    # Obtener las credenciales de acceso a MercadoPago en este caso del test
    sdk = mercadopago.SDK(os.environ["TEST_TOKEN"])
    
     # Obtener el ID del producto o servicio a comprar
    product_id = event['product_id']

    # Crear una preferencia de pago
     preference_data = {
       "items": bodyGet["items"]
    }
    # Obtener la información del comprador
     payer_names = event['first_name', 'last_name']
     payer_email = event['email']

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]


    # Crear una preferencia de pago
    preference = {
        "product": [
            {
                "id": id,
                "image": image,
                "name": name,
                "description": description,
                "price": price
            }
        ],
        "payer": {
            "name": first_name,
            "email": email
        },
        "back_urls": {
            "success": "http://localhost:3000/process_payment",
            "failure": error,
            "pending": 
        },
        "auto_return": "approved"
    }
    preference_response = mercadopago.Preference.create(preference)
    
    # Obtener la URL de checkout de MercadoPago
    checkout_url = preference['response']['init_point']
    
    # Devolver la URL de checkout como respuesta
    return {
        'statusCode': 200,
       'body': json.dumps(
            preference
        ),
    }
