import requests
from json import dumps
from json import loads
import json
import pandas as pd

portal = 'https://3d-zambia.chordsrt.com'
#inst_id=[
   # '18'
#]
user_email='mode2512@colorado.edu'
api_key='v_rRvx7cAMLK6fSXzAkv'
start='2025-09-01T00:00'
end='2025-09-01T23:59'

collection = set()

for instrument in range(1,156):
    url = f"{portal}/api/v1/data/{instrument}?start={start}&end={end}&email={user_email}&api_key={api_key}"

    try:
        response = requests.get(url=url)
        all_fields = loads(dumps(response.json()))

        geometry = all_fields['features'][0]['geometry']
        lon, lat, *rest = geometry['coordinates']

        collection.add((instrument, lat, lon, rest[0]))
        print(f"added for intrument {instrument}", lat, lon, rest[0])

    except requests.exceptions.RequestException as e:
        print(e)
    except json.JSONDecodeError as e:
        print(e)
    except:
        continue

df = pd.DataFrame(list(collection),columns=["Instrument ID","Latitude","Longitude","Elevation (m)"])

df.sort_values('Instrument ID', inplace=True)

df.to_csv('./data/ZambiaCoordinates.csv',index=False)

    
