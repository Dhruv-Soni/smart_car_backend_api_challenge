import requests

from constants import API_ENDPOINT_VEHICLE_INFO


def check_gm_response(jsonified_resp):
    """checks if the response recieved from gm api is valid

    :param jsonified_resp: json object containing response from gm api
    :return: True if valid, else False
    """
    present_data = ['vin', 'color', 'fourDoorSedan', 'twoDoorCoupe', 'driveTrain']
    for i in jsonified_resp['data']:
        if i not in present_data:
            return False
    return True


def extract_gm_data(jsonified_resp):
    """ Extract data from gm api and fill it into a dict to match smart car api spec

    :param jsonified_resp: json object containing response from gm api
    :return: dict that contains attributes to be used by json api
    """

    attributes = jsonified_resp['data']
    resp = {'vin': attributes['vin']['value'],
            'color': attributes['color']['value'],
            'doorCount': '',
            'driveTrain': attributes['driveTrain']['value']}

    if attributes['fourDoorSedan']['value'] == 'True':
        resp['doorCount'] = 4
    elif attributes['twoDoorCoupe']['value'] == 'True':
        resp['doorCount'] = 2

    return resp


def get_vehicle_attributes(id, logger):
    """ post call to the gm api to get attributes

    :param id: vehicle id
    :param logger: logging object to log info, debug, warning, error messages
    :return: a dict object that contains vehicle attributes as per smart car api spec
    """
    data = {'id': id,
            'responseType': 'JSON'}
    headers = {'Content-Type':'application/json'}

    try:
        r = requests.post(url=API_ENDPOINT_VEHICLE_INFO, json=data, headers=headers)

        if check_gm_response(r.json()) is False:
            msg = 'Attributes dont match the expected GM api attributes: {}'.format(r.json())
            logger.error(msg)
            raise Exception(msg)

        get_attr = extract_gm_data(r.json())
        msg = 'The attributes received from the GM api are: {}'.format(get_attr)
        logger.info(msg)
        return get_attr
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
