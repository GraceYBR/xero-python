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


class HistoryRecords(BaseModel):
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
    openapi_types = {"history_records": "list[HistoryRecord]"}

    attribute_map = {"history_records": "HistoryRecords"}

    def __init__(self, history_records=None):  # noqa: E501
        """HistoryRecords - a model defined in OpenAPI"""  # noqa: E501

        self._history_records = None
        self.discriminator = None

        if history_records is not None:
            self.history_records = history_records

    @property
    def history_records(self):
        """Gets the history_records of this HistoryRecords.  # noqa: E501


        :return: The history_records of this HistoryRecords.  # noqa: E501
        :rtype: list[HistoryRecord]
        """
        return self._history_records

    @history_records.setter
    def history_records(self, history_records):
        """Sets the history_records of this HistoryRecords.


        :param history_records: The history_records of this HistoryRecords.  # noqa: E501
        :type: list[HistoryRecord]
        """

        self._history_records = history_records
