import os
import requests
import json
from dotenv import load_dotenv


# Cargar credenciales
load_dotenv()
USERNAME = os.getenv("SPACETRACK_USERNAME")
PASSWORD = os.environ.get("SPACETRACK_PASSWORD")

# URL para acceder a la API
LOGIN_URL = "https://www.space-track.org/ajaxauth/login"
QUERY_DEBRIS = "https://www.space-track.org/basicspacedata/query/class/satcat/OBJECT_TYPE/DEBRIS/format/json"
QUERY_SATELLITES = "https://www.space-track.org/basicspacedata/query/class/satcat/OBJECT_TYPE/PAYLOAD/format/json"
QUERY_ROCKETS = "https://www.space-track.org/basicspacedata/query/class/satcat/OBJECT_TYPE/ROCKET BODY/format/json"
QUERY_UNKNOWN = "https://www.space-track.org/basicspacedata/query/class/satcat/OBJECT_TYPE/UNKNOWN/format/json"

def obtener_datos(query_url, filename):
    with requests.Session() as session:
        login_data = {'identity': USERNAME, 'password': PASSWORD}
        response = session.post(LOGIN_URL, data=login_data)
        
        if response.status_code == 200:
            print(f"Login exitoso. Obteniendo datos...")
            
            # Obtener datos
            data_response = session.get(query_url)
            
            if data_response.status_code == 200:
                data = data_response.json()
                
                # Guardar en .json
                with open(filename, "w", encoding="utf-8") as json_file:
                    json.dump(data, json_file, indent=4)
                
                print(f"Datos guardados en {filename}")
            else:
                print(f"Error al obtener datos ({data_response.status_code})")
        else:
            print(f"Error en el login ({response.status_code})")

obtener_datos(QUERY_SATELLITES, "data/space_track/satellites.json")
obtener_datos(QUERY_DEBRIS, "data/space_track/debris.json")
obtener_datos(QUERY_ROCKETS, "data/space_track.json")
obtener_datos(QUERY_UNKNOWN, "data/space_track/unknown.json")