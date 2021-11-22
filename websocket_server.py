"""This module is implementation of server side"""
import websockets
from datetime import datetime
import asyncio
from pyngrok import ngrok
from moon import moon_coordinates_from_ephem, manual_moon_coordinates_calculation, moon_is_going_up, ra_dec_transformer


async def sender(websocket, path):
    """
    It is the main couratine that sends coordinates of the moon every 10 seconds
    """
    moon_coordinates1 = moon_coordinates_from_ephem(datetime.now())
    is_moon_going_up = moon_is_going_up(datetime.now())
    ra_dec_coordinates = manual_moon_coordinates_calculation(*moon_coordinates1, is_moon_going_up)
    result = str(ra_dec_transformer(*ra_dec_coordinates))
    await websocket.send(result)
    while True:
        await asyncio.sleep(10)
        ra_dec_coordinates = manual_moon_coordinates_calculation(*ra_dec_coordinates, is_moon_going_up)
        result = str(ra_dec_transformer(*ra_dec_coordinates))
        await websocket.send(result)


async def server_run():
    """
    This couratine is running the server and ngrok tunnel
    """
    async with websockets.serve(sender, "localhost", 8777):
        ngrok.set_auth_token('1zonoVhE72uzDQgHepnpP88sInW_5BFdnjN8LAwAoZSuQRd4Z')
        ws_tunnel = ngrok.connect(8777, 'tcp')
        print(f'ws://{ws_tunnel.public_url[6:]}')
        await asyncio.Future()


asyncio.run(server_run())
