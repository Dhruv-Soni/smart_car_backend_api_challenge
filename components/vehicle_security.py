import requests

from constants import API_ENDPOINT_SECURITY


def get_door_locked_value(value):
    """checks if door is locked

    :param value: a string value that is either true or false
    :return: a True boolean if the door is locked, else False if it is open
    """
    if value == "True":
        return True
    if value == "False":
        return False


def extract_gm_data(doors):
    """populates a list with the number of doors locked and unlocked for a particular vehicle

    :param doors: a list with each element being a different car door
    :return:  a list object that contains vehicle door security as per smart car api spec
    """
    simplified_doors = []
    for door in doors:
        simplified_doors.append({'location': door['location']['value'],
                                 'locked': get_door_locked_value(door['locked']['value'])})
    return simplified_doors


def get_vehicle_security(id, logger):
    """ post call to gm api to get vehicle security door attributes

    :param id: vehicle id
    :param logger: logging object to log info, debug, warning, error messages
    :return:  a list object that contains vehicle door security as per smart car api spec
    """
    data = {'id': id,
            'responseType': 'JSON'}
    headers = {'Content-Type':'application/json'}

    try:
        r = requests.post(url=API_ENDPOINT_SECURITY, json=data, headers=headers)
        doors = r.json()['data']['doors']['values']
        simplified_doors = extract_gm_data(doors)
        logger.info('Open and closed doors: {}'.format(simplified_doors))
        return simplified_doors
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
