import asyncio
import logging
import getpass

from pytrutankless.api import TruTanklessApiInterface
from pytrutankless.device import Device

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


async def main():
    email = "youremail@here"
    password = "account_password"
    # email = input("Enter your email: ").strip()
    # password = getpass.getpass(prompt="Enter your password: ")
    api = await TruTanklessApiInterface.login(email, password)
    # await api.get_devices()
    # await api.refresh_device("1061")
    # print(f"All Locations: {api._locations}")
    # print(f"Get Devices: {api._devices}")

    await api.get_devices()

    test_device = Device(api.devices)

    for dev_id in api.devices.keys():
        await api.refresh_device(dev_id)
        dev_obj = api.devices[dev_id]
        print(dev_obj.get("serial_number"))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
