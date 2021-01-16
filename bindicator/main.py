import asyncio
import os
import pprint
import random

from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager

from .config import config


async def main(
    email: str = config.MEROSS_EMAIL, password: str = config.MEROSS_PASSWORD
):
    """Set the lights to the next bin colour"""
    # Setup the HTTP client API from user-password
    http_api_client = await MerossHttpClient.async_from_user_password(
        email=email, password=password
    )

    # Setup and start the device manager
    manager = MerossManager(
        http_client=http_api_client, over_limit_threshold_percentage=1000
    )
    await manager.async_init()

    # Retrieve all the MSS310 devices that are registered on this account
    # Discover devices.
    await manager.async_device_discovery()
    meross_devices = manager.find_devices()

    # Print them
    print("I've found the following devices:")
    for dev in meross_devices:
        print(f"- {dev.name} ({dev.type}): {dev.online_status}")
        if dev.name == "Garage Bulb":
            await dev.async_update()
            # Check the current RGB color
            current_color = dev.get_rgb_color()
            print(
                f"Currently, device {dev.name} is set to color (RGB) = {current_color}"
            )
            # Randomly chose a new color
            rgb = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
            print(f"Chosen random color (R,G,B): {rgb}")
            await dev.async_set_light_color(rgb=rgb)
            print("Color changed!")

    # Close the manager and logout from http_api
    manager.close()
    await http_api_client.async_logout()


if __name__ == "__main__":
    # On Windows + Python 3.8, you should uncomment the following
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()