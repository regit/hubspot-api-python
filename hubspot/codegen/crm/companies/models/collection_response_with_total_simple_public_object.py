# coding: utf-8

"""
    Companies

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.codegen.crm.companies.configuration import Configuration


class CollectionResponseWithTotalSimplePublicObject(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'total': 'int',
        'results': 'list[SimplePublicObject]',
        'paging': 'Paging'
    }

    attribute_map = {
        'total': 'total',
        'results': 'results',
        'paging': 'paging'
    }

    def __init__(self, total=None, results=None, paging=None, local_vars_configuration=None):  # noqa: E501
        """CollectionResponseWithTotalSimplePublicObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total = None
        self._results = None
        self._paging = None
        self.discriminator = None

        self.total = total
        self.results = results
        if paging is not None:
            self.paging = paging

    @property
    def total(self):
        """Gets the total of this CollectionResponseWithTotalSimplePublicObject.  # noqa: E501

        The number of available results  # noqa: E501

        :return: The total of this CollectionResponseWithTotalSimplePublicObject.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CollectionResponseWithTotalSimplePublicObject.

        The number of available results  # noqa: E501

        :param total: The total of this CollectionResponseWithTotalSimplePublicObject.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total is None:  # noqa: E501
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def results(self):
        """Gets the results of this CollectionResponseWithTotalSimplePublicObject.  # noqa: E501


        :return: The results of this CollectionResponseWithTotalSimplePublicObject.  # noqa: E501
        :rtype: list[SimplePublicObject]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this CollectionResponseWithTotalSimplePublicObject.


        :param results: The results of this CollectionResponseWithTotalSimplePublicObject.  # noqa: E501
        :type: list[SimplePublicObject]
        """
        if self.local_vars_configuration.client_side_validation and results is None:  # noqa: E501
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

    @property
    def paging(self):
        """Gets the paging of this CollectionResponseWithTotalSimplePublicObject.  # noqa: E501


        :return: The paging of this CollectionResponseWithTotalSimplePublicObject.  # noqa: E501
        :rtype: Paging
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this CollectionResponseWithTotalSimplePublicObject.


        :param paging: The paging of this CollectionResponseWithTotalSimplePublicObject.  # noqa: E501
        :type: Paging
        """

        self._paging = paging

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CollectionResponseWithTotalSimplePublicObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CollectionResponseWithTotalSimplePublicObject):
            return True

        return self.to_dict() != other.to_dict()
