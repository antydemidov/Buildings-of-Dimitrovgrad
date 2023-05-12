from mapbox import Maps

MAPBOX_ACCESS_TOKEN="pk.eyJ1IjoiYW50eWRlbWlkb3YiLCJhIjoiY2twN2luNnc1MDBvMTJvcGxpa3FjZzQ1MiJ9.GBkTgu8vLZ6hz_p6DDoZlQ"

def map():
    maps = Maps(access_token=MAPBOX_ACCESS_TOKEN)
    response = maps.tile('mapbox.streets', 0, 0, 0)
    if response.status_code == 200:
        with open("app/static/0.png", "wb") as output:
            output.write(response.content)

    return response.status_code

map()
