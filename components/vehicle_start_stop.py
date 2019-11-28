import requests

from constants import API_ENDPOINT_ENGINE_START_STOP


def get_engine_action(action):
    """ sets the action parameter as per gm api spec

    :param action: string value to either start or stop the vehicle
    :return: string that is gm api compliant for to make a post request
    """
    if action == 'START':
        return 'START_VEHICLE'
    if action == 'STOP':
        return 'STOP_VEHICLE'
    raise Exception('Expected either START or STOP, received {}'.format(action))


def set_engine_info_msg(result):
    """ Changes the gm api resp to smart car api spec

    :param result: response from gm api
    :return: string response to match smart car api spec
    """
    if result == 'EXECUTED':
        return 'success'
    if result == 'FAILED':
        return 'error'


def set_vehicle_start_stop(id, action, logger):
    """ post call to turn on/off vehicle

    :param id: vehicle id
    :param action: either start or stop the car
    :param logger: logging object to log info, debug, warning, error messages
    :return:  a dict object that contains status of the post call made as per smart car api spec
    """
    data = {'id': id,
            'command': get_engine_action(action),
            'responseType': 'JSON'}
    headers = {'Content-Type':'application/json'}
    try:
        r = requests.post(url=API_ENDPOINT_ENGINE_START_STOP, json=data, headers=headers)
        result = r.json()['actionResult']['status']
        return {'status': set_engine_info_msg(result)}
    except requests.exceptions.HTTPError as errh:
        logger.error('Http Error: {}'.format(errh))
    except requests.exceptions.ConnectionError as errc:
        logger.error('Error Connecting: {}'.format(errc))
    except requests.exceptions.Timeout as errt:
        logger.error('Timeout Error: {}'.format(errt))
    except requests.exceptions.RequestException as err:
        logger.error('Request Expection: {}'.format(err))
    except Exception as e:
        logger.error(e)
