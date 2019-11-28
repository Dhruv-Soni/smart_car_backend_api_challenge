import json
import structlog

import components.vehicle_attributes as vehicle_attributes
import components.vehicle_security as vehicle_security
import components.vehicle_battery as vehicle_battery
import components.vehicle_fuel as vehicle_fuel
import components.vehicle_start_stop as vehicle_start_stop

from flask import Flask, request, jsonify

logger = structlog.get_logger()

app = Flask(__name__)


@app.route('/vehicles/<string:id>', endpoint='vehicle_info', methods=["GET"])
def vehicle_info(id: str):
    """get call for vehicle attributes

    :param id: vehicle id
    :return: a tuple, where the first element is response, and the second one is the status code
    """
    info = vehicle_attributes.get_vehicle_attributes(id, logger)
    return jsonify(info), 200


@app.route('/vehicles/<string:id>/doors', endpoint='vehicle_security_info', methods=["GET"])
def vehicle_security_info(id: str):
    """get call for vehicle security, showing which doors are open and closed

    :param id: vehicle id
    :return: a tuple, where the first element is response, and the second one is the status code
    """
    info = vehicle_security.get_vehicle_security(id, logger)
    return jsonify(info), 200


@app.route('/vehicles/<string:id>/fuel', endpoint='vehicle_fuel_info', methods=["GET"])
def vehicle_fuel_info(id: str):
    """get call for vehicle fuel info

    :param id: vehicle id
    :return: a tuple, where the first element is response, and the second one is the status code,
     will return a 404 if the car is electric powered
    """
    info = vehicle_fuel.get_vehicle_fuel(id, logger)
    if info is None:
        return jsonify(info), 404
    return jsonify(info), 200


@app.route('/vehicles/<string:id>/battery', endpoint='vehicle_battery_info', methods=["GET"])
def vehicle_battery_info(id: str):
    """get call for vehicle battery info

    :param id: vehicle id
    :return: a tuple, where the first element is response, and the second one is the status code,
     will return a 404 if the car is gas powered
    """
    info = vehicle_battery.get_vehicle_battery(id, logger)
    if info is None:
        return jsonify(info), 404
    return jsonify(info), 200


@app.route('/vehicles/<string:id>/engine', endpoint='vehicle_engine_start_stop', methods=["POST"])
def vehicle_engine_start_stop_info(id: str):
    """post call to start or stop the engine. will return a success or a fail depending on the response received

    :param id: vehicle id
    :return: a tuple, where the first element is response, and the second one is the status code
    """
    payload = json.loads(request.data)
    info = vehicle_start_stop.set_vehicle_start_stop(id, payload['action'], logger)
    return jsonify(info), 200


if __name__ == '__main__':
    app.run()
