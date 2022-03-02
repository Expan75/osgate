import unittest
from uuid import uuid4 as uuid

from osgate.devices.deviceFactory import create_device


class DeviceFactoryTests(unittest.TestCase):
    def testValidCreation(self):
        device = create_device(
            {
                "name": "sensorname",
                "type": "default",
                "uuid": uuid(),
                "meta": {"some": "value"},
                "channels": [],
            }
        )
        self.assertIsNotNone(device)

    def testInvalidCreation(self):
        with self.assertRaises(NotImplementedError):
            device = create_device(
                {
                    "name": "sensorname",
                    "type": "not something real",
                    "uuid": uuid(),
                    "meta": {"some": "value"},
                    "channels": [],
                }
            )
