import unittest
from uuid import uuid4 as uuid

from osgate.devices import deviceFactory


class DeviceFactoryTests(unittest.TestCase):
    def testValidCreation(self):
        device = deviceFactory.create_device(
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
            device = deviceFactory.create_device(
                {
                    "name": "sensorname",
                    "type": "not something real",
                    "uuid": uuid(),
                    "meta": {"some": "value"},
                    "channels": [],
                }
            )
