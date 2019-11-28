import requests

from constants import API_ENDPOINT_FUEL_BATTERY


def get_vehicle_fuel(id, logger):
    """ post call gm api to get fuel percentage

        :param id: vehicle id
        :param logger: logging object to log info, debug, warning, error messages
        :return: a dict object that contains vehicle attributes as per smart car api spec
        """
    data = {'id': id,
            'responseType': 'JSON'}
    headers = {'Content-Type':'application/json'}

    try:
        r = requests.post(url=API_ENDPOINT_FUEL_BATTERY, json=data, headers=headers)
        fuel_percentage = r.json()['data']['tankLevel']['value']
        if fuel_percentage == 'null':
            msg='This vehicle is not fuel powered, please try checking the battery percentage using .../id/battery'
            logger.error(msg)
            return None
        return {'percentage': fuel_percentage}
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
