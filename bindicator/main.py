import asyncio

import sentry_sdk
from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

from bindicator.config import config

if config.SENTRY_DSN is not None:
    sentry_sdk.init(
        dsn=config.SENTRY_DSN,
        integrations=[AwsLambdaIntegration()],
    )


async def main(
    email: str = config.MEROSS_EMAIL, password: str = config.MEROSS_PASSWORD
):
    """Set the lights to the next bin colour"""
    # code smell but meh
    raise Exception("Hello Sentry!")
    from bindicator import bins

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
        # down and dirty
        if dev.name.startswith("Garage Bulb"):
            ix = int(dev.name[-1]) - 1
            new_col = bins.NEXT_BINS[ix]
            await dev.async_update()
            # Check the current RGB color
            current_color = dev.get_rgb_color()
            print(f"Device {dev.name} set to RGB {current_color}")
            # set to next bins colour
            print(f"Chosen random color (R,G,B): {new_col}")
            await dev.async_set_light_color(rgb=new_col.value)
            print("Color changed!")

    # Close the manager and logout from http_api
    manager.close()
    await http_api_client.async_logout()


def handler(event=None, context=None):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()


if __name__ == "__main__":
    try:
        handler()
    except Exception as e:
        # something went wrong in the above, send to sentry
        sentry_sdk.capture_exception(e)
