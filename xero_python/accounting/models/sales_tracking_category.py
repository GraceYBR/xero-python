# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.2.10
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class SalesTrackingCategory(BaseModel):
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
    openapi_types = {"tracking_category_name": "str", "tracking_option_name": "str"}

    attribute_map = {
        "tracking_category_name": "TrackingCategoryName",
        "tracking_option_name": "TrackingOptionName",
    }

    def __init__(
        self, tracking_category_name=None, tracking_option_name=None
    ):  # noqa: E501
        """SalesTrackingCategory - a model defined in OpenAPI"""  # noqa: E501

        self._tracking_category_name = None
        self._tracking_option_name = None
        self.discriminator = None

        if tracking_category_name is not None:
            self.tracking_category_name = tracking_category_name
        if tracking_option_name is not None:
            self.tracking_option_name = tracking_option_name

    @property
    def tracking_category_name(self):
        """Gets the tracking_category_name of this SalesTrackingCategory.  # noqa: E501

        The default sales tracking category name for contacts  # noqa: E501

        :return: The tracking_category_name of this SalesTrackingCategory.  # noqa: E501
        :rtype: str
        """
        return self._tracking_category_name

    @tracking_category_name.setter
    def tracking_category_name(self, tracking_category_name):
        """Sets the tracking_category_name of this SalesTrackingCategory.

        The default sales tracking category name for contacts  # noqa: E501

        :param tracking_category_name: The tracking_category_name of this SalesTrackingCategory.  # noqa: E501
        :type: str
        """

        self._tracking_category_name = tracking_category_name

    @property
    def tracking_option_name(self):
        """Gets the tracking_option_name of this SalesTrackingCategory.  # noqa: E501

        The default purchase tracking category name for contacts  # noqa: E501

        :return: The tracking_option_name of this SalesTrackingCategory.  # noqa: E501
        :rtype: str
        """
        return self._tracking_option_name

    @tracking_option_name.setter
    def tracking_option_name(self, tracking_option_name):
        """Sets the tracking_option_name of this SalesTrackingCategory.

        The default purchase tracking category name for contacts  # noqa: E501

        :param tracking_option_name: The tracking_option_name of this SalesTrackingCategory.  # noqa: E501
        :type: str
        """

        self._tracking_option_name = tracking_option_name
