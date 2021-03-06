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


class CarSearchResult(object):
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
        'provider': 'Company',
        'location': 'Geolocation',
        'airport': 'str',
        'cars': 'list[Vehicle]'
    }

    attribute_map = {
        'provider': 'provider',
        'location': 'location',
        'airport': 'airport',
        'cars': 'cars'
    }

    def __init__(self, provider=None, location=None, airport=None, cars=None):
        """
        CarSearchResult - a model defined in Swagger
        """

        self._provider = None
        self._location = None
        self._airport = None
        self._cars = None

        self.provider = provider
        if location is not None:
          self.location = location
        if airport is not None:
          self.airport = airport
        if cars is not None:
          self.cars = cars

    @property
    def provider(self):
        """
        Gets the provider of this CarSearchResult.
        Details of the car company offering this rental.

        :return: The provider of this CarSearchResult.
        :rtype: Company
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this CarSearchResult.
        Details of the car company offering this rental.

        :param provider: The provider of this CarSearchResult.
        :type: Company
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")

        self._provider = provider

    @property
    def location(self):
        """
        Gets the location of this CarSearchResult.
        This car rental company's approximate geolocation. The exact quality of this parameter depends on the provider but it's usually quite accurate.

        :return: The location of this CarSearchResult.
        :rtype: Geolocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this CarSearchResult.
        This car rental company's approximate geolocation. The exact quality of this parameter depends on the provider but it's usually quite accurate.

        :param location: The location of this CarSearchResult.
        :type: Geolocation
        """

        self._location = location

    @property
    def airport(self):
        """
        Gets the airport of this CarSearchResult.
        The exact quality of this parameter depends on the provider but it's usually quite accurate.

        :return: The airport of this CarSearchResult.
        :rtype: str
        """
        return self._airport

    @airport.setter
    def airport(self, airport):
        """
        Sets the airport of this CarSearchResult.
        The exact quality of this parameter depends on the provider but it's usually quite accurate.

        :param airport: The airport of this CarSearchResult.
        :type: str
        """

        self._airport = airport

    @property
    def cars(self):
        """
        Gets the cars of this CarSearchResult.
        Further details about each of the vehicles offered by this car rental provider.

        :return: The cars of this CarSearchResult.
        :rtype: list[Vehicle]
        """
        return self._cars

    @cars.setter
    def cars(self, cars):
        """
        Sets the cars of this CarSearchResult.
        Further details about each of the vehicles offered by this car rental provider.

        :param cars: The cars of this CarSearchResult.
        :type: list[Vehicle]
        """

        self._cars = cars

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
        if not isinstance(other, CarSearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
