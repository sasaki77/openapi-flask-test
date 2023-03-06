import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.request_error import RequestError  # noqa: E501
from openapi_server.models.user import User  # noqa: E501
from openapi_server import util


def get_user(name):  # noqa: E501
    """get_user

     # noqa: E501

    :param name: user name
    :type name: str

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_users():  # noqa: E501
    """get_users

     # noqa: E501


    :rtype: Union[List[User], Tuple[List[User], int], Tuple[List[User], int, Dict[str, str]]
    """
    return 'do some magic!'


def post_user(name, user=None):  # noqa: E501
    """post_user

     # noqa: E501

    :param name: user name
    :type name: str
    :param user: 
    :type user: dict | bytes

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
