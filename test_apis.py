import unittest
from app import *


class ApiListTestCases(unittest.TestCase):


    # Test cases for Vehicle info
    def test_vehicle_info_1234(self):
        """
        tests vehicle info get request for id == 1234, including params and status code
        """
        with app.app_context():
            logger.info('Starting testcase to check vehicle info for id: 1235')
            res, status_code = vehicle_info('1234')
            res_data = json.loads(res.data)
            assert status_code == 200, 'expected 200, got {}'.format(status_code)
            assert len(res_data) == 4,\
                'expected, "vin", "color", "doorCount", "driveTrain", ' \
                'got {}'.format(res_data)
            logger.info('Testcase passed')

    def test_vehicle_info_1235(self):
        """
        tests vehicle info get request for id == 1235, including params and status code
        """
        with app.app_context():
            logger.info('Starting testcase to check vehicle info for id: 1235')
            res, status_code = vehicle_info('1235')
            res_data = json.loads(res.data)
            assert status_code == 200, 'expected 200, got {}'.format(status_code)
            assert len(res_data) == 4,\
                'expected, "vin", "color", "doorCount", "driveTrain", ' \
                'got {}'.format(res_data)
            logger.info('Testcase passed')


    # Test cases for Vehicle Security
    def test_vehicle_security_1234(self):
        """
        tests vehicle security get request for id == 1234, including params and status code
        """
        with app.app_context():
            logger.info('Starting testcase to check vehicle security info for id: 1234')
            res, status_code = vehicle_security_info('1234')
            res_data = json.loads(res.data)
            assert status_code == 200, 'expected 200, got {}'.format(status_code)
            assert len(res_data) == 4,\
                'expected, "frontLeft", "frontRight", "backLeft", "backRight", ' \
                'got {}'.format(res_data)
            logger.info('Testcase passed')

    def test_vehicle_security_1235(self):
        """
        tests vehicle security get request for id == 1235, including params and status code
        """
        with app.app_context():
            logger.info('Starting testcase to check vehicle security info for id: 1235')
            res, status_code = vehicle_security_info('1235')
            res_data = json.loads(res.data)
            assert status_code == 200, 'expected 200, got {}'.format(status_code)
            assert len(res_data) == 2,\
                'expected, "frontLeft", "frontRight", ' \
                'got {}'.format(res_data)
            logger.info('Testcase passed')


    # Test cases for Vehicle Battery
    def test_vehicle_battery_1234(self):
        """
        tests vehicle battery percentage get request for id == 1234, including params and status code
        """
        with app.app_context():
            logger.info('Starting testcase to check vehicle battery info for id: 1234')
            res, status_code = vehicle_battery_info('1234')
            res_data = json.loads(res.data)
            assert status_code == 404, 'expected 404, got {}'.format(status_code)
            logger.info('Testcase passed')

    def test_vehicle_battery_1235(self):
        """
        tests vehicle battery percentage get request for id == 1235, including params and status code
        """
        with app.app_context():
            logger.info('Starting testcase to check vehicle battery info for id: 1235')
            res, status_code = vehicle_battery_info('1235')
            res_data = json.loads(res.data)
            assert status_code == 200, 'expected 200, got {}'.format(status_code)
            assert len(res_data) == 1,\
                'expected,  "Percentage", ' \
                'got {}'.format(res_data)
            logger.info('Testcase passed')


    # Test cases for Vehicle Fuel
    def test_vehicle_fuel_1234(self):
        """
        tests vehicle fuel percentage get request for id == 1234, including params and status code
        """
        with app.app_context():
            logger.info('Starting testcase to check vehicle battery info for id: 1234')
            res, status_code = vehicle_fuel_info('1234')
            res_data = json.loads(res.data)
            assert status_code == 200, 'expected 200, got {}'.format(status_code)
            assert len(res_data) == 1,\
                'expected,  "Percentage", ' \
                'got {}'.format(res_data)
            logger.info('Testcase passed')

    def test_vehicle_fuel_1235(self):
        """
        tests vehicle fuel percentage get request for id == 1235, including params and status code
        """
        with app.app_context():
            logger.info('Starting testcase to check vehicle battery info for id: 1235')
            res, status_code = vehicle_fuel_info('1235')
            res_data = json.loads(res.data)
            assert status_code == 404, 'expected 404, got {}'.format(status_code)
            logger.info('Testcase passed')


    # Test cases for vehicle engine start/stop
    def test_vehicle_engine_start_1234(self):
        """
        tests vehicle engine start set request for id == 1234, including params and status code
        """
        with app.test_request_context('/vehicles/1234/engine', data=json.dumps({'action': 'START'})):
            logger.info('Starting testcase set vehicle engine start mode for id: 1234')
            res, status_code = vehicle_engine_start_stop_info('1234')
            res_data = json.loads(res.data)
            assert status_code == 200, 'expected 200, got {}'.format(status_code)
            assert len(res_data) == 1,\
                'expected,  "status", ' \
                'got {}'.format(res_data)
            logger.info('Testcase passed')

    def test_vehicle_engine_stop_1234(self):
        """
        tests vehicle engine stop set post request for id == 1234, including params and status code
        """
        with app.test_request_context('/vehicles/1234/engine', data=json.dumps({'action': 'STOP'})):
            logger.info('Starting testcase set vehicle engine stop mode for id: 1234')
            res, status_code = vehicle_engine_start_stop_info('1234')
            res_data = json.loads(res.data)
            assert status_code == 200, 'expected 200, got {}'.format(status_code)
            assert len(res_data) == 1,\
                'expected,  "status", ' \
                'got {}'.format(res_data)
            logger.info('Testcase passed')

    def test_vehicle_engine_start_1235(self):
        """
        tests vehicle engine start set request for id == 1235, including params and status code
        """
        with app.test_request_context('/vehicles/1235/engine', data=json.dumps({'action': 'START'})):
            logger.info('Starting testcase set vehicle engine start mode for id: 1235')
            res, status_code = vehicle_engine_start_stop_info('1235')
            res_data = json.loads(res.data)
            assert status_code == 200, 'expected 200, got {}'.format(status_code)
            assert len(res_data) == 1,\
                'expected,  "status", ' \
                'got {}'.format(res_data)
            logger.info('Testcase passed')

    def test_vehicle_engine_stop_1235(self):
        """
        tests vehicle engine stop set post request for id == 1235, including params and status code
        """
        with app.test_request_context('/vehicles/1235/engine', data=json.dumps({'action': 'STOP'})):
            logger.info('Starting testcase set vehicle engine stop mode for id: 1235')
            res, status_code = vehicle_engine_start_stop_info('1235')
            res_data = json.loads(res.data)
            assert status_code == 200, 'expected 200, got {}'.format(status_code)
            assert len(res_data) == 1,\
                'expected,  "status", ' \
                'got {}'.format(res_data)
            logger.info('Testcase passed')


if __name__ == "__main__":
    unittest.main()
