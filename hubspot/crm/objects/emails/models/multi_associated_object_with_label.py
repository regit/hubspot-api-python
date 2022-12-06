# coding: utf-8

"""
    Emails

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.objects.emails.configuration import Configuration


class MultiAssociatedObjectWithLabel(object):
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
    openapi_types = {"to_object_id": "int", "association_types": "list[AssociationSpecWithLabel]"}

    attribute_map = {"to_object_id": "toObjectId", "association_types": "associationTypes"}

    def __init__(self, to_object_id=None, association_types=None, local_vars_configuration=None):  # noqa: E501
        """MultiAssociatedObjectWithLabel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._to_object_id = None
        self._association_types = None
        self.discriminator = None

        self.to_object_id = to_object_id
        self.association_types = association_types

    @property
    def to_object_id(self):
        """Gets the to_object_id of this MultiAssociatedObjectWithLabel.  # noqa: E501


        :return: The to_object_id of this MultiAssociatedObjectWithLabel.  # noqa: E501
        :rtype: int
        """
        return self._to_object_id

    @to_object_id.setter
    def to_object_id(self, to_object_id):
        """Sets the to_object_id of this MultiAssociatedObjectWithLabel.


        :param to_object_id: The to_object_id of this MultiAssociatedObjectWithLabel.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and to_object_id is None:  # noqa: E501
            raise ValueError("Invalid value for `to_object_id`, must not be `None`")  # noqa: E501

        self._to_object_id = to_object_id

    @property
    def association_types(self):
        """Gets the association_types of this MultiAssociatedObjectWithLabel.  # noqa: E501


        :return: The association_types of this MultiAssociatedObjectWithLabel.  # noqa: E501
        :rtype: list[AssociationSpecWithLabel]
        """
        return self._association_types

    @association_types.setter
    def association_types(self, association_types):
        """Sets the association_types of this MultiAssociatedObjectWithLabel.


        :param association_types: The association_types of this MultiAssociatedObjectWithLabel.  # noqa: E501
        :type: list[AssociationSpecWithLabel]
        """
        if self.local_vars_configuration.client_side_validation and association_types is None:  # noqa: E501
            raise ValueError("Invalid value for `association_types`, must not be `None`")  # noqa: E501

        self._association_types = association_types

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
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
        if not isinstance(other, MultiAssociatedObjectWithLabel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MultiAssociatedObjectWithLabel):
            return True

        return self.to_dict() != other.to_dict()
