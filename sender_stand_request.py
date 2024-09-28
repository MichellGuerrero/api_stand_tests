import configuration
import requests
import data
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)

def get_logs_params():
     return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,params={"count":20})

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados


#get_logs
response1 = get_logs()
print(response1.status_code)
print(response1.headers)
#get_logs_params
response2 = get_logs_params()
print(response2.status_code)
print(response2.headers)
#get_users_table
response  = get_users_table()
print(response.status_code)
#post_new_user
response = post_new_user(data.user_body)
print(response.status_code)
#post__new_user_formato_json
response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())
#post_products_kits
response = post_products_kits(data.product_ids);
print(response.status_code)
print(response.json())


