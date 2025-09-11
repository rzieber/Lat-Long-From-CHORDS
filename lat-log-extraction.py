import requests
from json import dumps
from json import loads

portal = 'https://3d.chordsrt.com'
inst_id=[
    '18'
]
user_email='rzieber@ucar.edu'
api_key='pc7HQpcDipWsetaxmJ5t'
start='2025-09-01T00:00'
end='2025-09-01T23:59'

for instrument in inst_id:
    url = f"{portal}/api/v1/data/{instrument}?start={start}&end={end}&email={user_email}&api_key={api_key}"

    response = requests.get(url=url)
    all_fields = loads(dumps(response.json()))

    geometry = all_fields['features'][0]['geometry']
    lon, lat, *rest = geometry['coordinates']
    print("Latitude:", lat)
    print("Longitude:", lon)
    if rest: print("Elevation:", rest[0])
