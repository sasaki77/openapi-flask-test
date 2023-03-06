# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class RequestError(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, detail=None, status=None, title=None, type=None):  # noqa: E501
        """RequestError - a model defined in OpenAPI

        :param detail: The detail of this RequestError.  # noqa: E501
        :type detail: str
        :param status: The status of this RequestError.  # noqa: E501
        :type status: int
        :param title: The title of this RequestError.  # noqa: E501
        :type title: str
        :param type: The type of this RequestError.  # noqa: E501
        :type type: str
        """
        self.openapi_types = {
            'detail': str,
            'status': int,
            'title': str,
            'type': str
        }

        self.attribute_map = {
            'detail': 'detail',
            'status': 'status',
            'title': 'title',
            'type': 'type'
        }

        self._detail = detail
        self._status = status
        self._title = title
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'RequestError':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RequestError of this RequestError.  # noqa: E501
        :rtype: RequestError
        """
        return util.deserialize_model(dikt, cls)

    @property
    def detail(self):
        """Gets the detail of this RequestError.


        :return: The detail of this RequestError.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this RequestError.


        :param detail: The detail of this RequestError.
        :type detail: str
        """

        self._detail = detail

    @property
    def status(self):
        """Gets the status of this RequestError.


        :return: The status of this RequestError.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RequestError.


        :param status: The status of this RequestError.
        :type status: int
        """

        self._status = status

    @property
    def title(self):
        """Gets the title of this RequestError.


        :return: The title of this RequestError.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this RequestError.


        :param title: The title of this RequestError.
        :type title: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this RequestError.


        :return: The type of this RequestError.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RequestError.


        :param type: The type of this RequestError.
        :type type: str
        """

        self._type = type