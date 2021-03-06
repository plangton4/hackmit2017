# coding: utf-8

"""
    Amadeus Travel Innovation Sandbox

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TopSearchesSearchResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'market': 'str',
        'period': 'str',
        'origin': 'str',
        'destination': 'str',
        'results': 'list[TopSearchesSearchResult]'
    }

    attribute_map = {
        'market': 'market',
        'period': 'period',
        'origin': 'origin',
        'destination': 'destination',
        'results': 'results'
    }

    def __init__(self, market=None, period=None, origin=None, destination=None, results=None):
        """
        TopSearchesSearchResponse - a model defined in Swagger
        """

        self._market = None
        self._period = None
        self._origin = None
        self._destination = None
        self._results = None

        self.market = market
        self.period = period
        self.origin = origin
        self.destination = destination
        self.results = results

    @property
    def market(self):
        """
        Gets the market of this TopSearchesSearchResponse.
        Country code

        :return: The market of this TopSearchesSearchResponse.
        :rtype: str
        """
        return self._market

    @market.setter
    def market(self, market):
        """
        Sets the market of this TopSearchesSearchResponse.
        Country code

        :param market: The market of this TopSearchesSearchResponse.
        :type: str
        """
        if market is None:
            raise ValueError("Invalid value for `market`, must not be `None`")

        self._market = market

    @property
    def period(self):
        """
        Gets the period of this TopSearchesSearchResponse.
        The date period, in <a href=\"https://en.wikipedia.org/wiki/ISO_8601\">ISO 8601</a> date format YYYY-MM or YYYY

        :return: The period of this TopSearchesSearchResponse.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this TopSearchesSearchResponse.
        The date period, in <a href=\"https://en.wikipedia.org/wiki/ISO_8601\">ISO 8601</a> date format YYYY-MM or YYYY

        :param period: The period of this TopSearchesSearchResponse.
        :type: str
        """
        if period is None:
            raise ValueError("Invalid value for `period`, must not be `None`")

        self._period = period

    @property
    def origin(self):
        """
        Gets the origin of this TopSearchesSearchResponse.
        <a href=\"https://en.wikipedia.org/wiki/International_Air_Transport_Association_airport_code\">IATA code</a>

        :return: The origin of this TopSearchesSearchResponse.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """
        Sets the origin of this TopSearchesSearchResponse.
        <a href=\"https://en.wikipedia.org/wiki/International_Air_Transport_Association_airport_code\">IATA code</a>

        :param origin: The origin of this TopSearchesSearchResponse.
        :type: str
        """
        if origin is None:
            raise ValueError("Invalid value for `origin`, must not be `None`")

        self._origin = origin

    @property
    def destination(self):
        """
        Gets the destination of this TopSearchesSearchResponse.
        <a href=\"https://en.wikipedia.org/wiki/International_Air_Transport_Association_airport_code\">IATA code</a>

        :return: The destination of this TopSearchesSearchResponse.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this TopSearchesSearchResponse.
        <a href=\"https://en.wikipedia.org/wiki/International_Air_Transport_Association_airport_code\">IATA code</a>

        :param destination: The destination of this TopSearchesSearchResponse.
        :type: str
        """
        if destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")

        self._destination = destination

    @property
    def results(self):
        """
        Gets the results of this TopSearchesSearchResponse.

        :return: The results of this TopSearchesSearchResponse.
        :rtype: list[TopSearchesSearchResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this TopSearchesSearchResponse.

        :param results: The results of this TopSearchesSearchResponse.
        :type: list[TopSearchesSearchResult]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")

        self._results = results

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TopSearchesSearchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
