# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.2.10
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class LeaveBalance(BaseModel):
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
        "leave_name": "str",
        "leave_type_id": "str",
        "number_of_units": "float",
        "type_of_units": "str",
    }

    attribute_map = {
        "leave_name": "LeaveName",
        "leave_type_id": "LeaveTypeID",
        "number_of_units": "NumberOfUnits",
        "type_of_units": "TypeOfUnits",
    }

    def __init__(
        self,
        leave_name=None,
        leave_type_id=None,
        number_of_units=None,
        type_of_units=None,
    ):  # noqa: E501
        """LeaveBalance - a model defined in OpenAPI"""  # noqa: E501

        self._leave_name = None
        self._leave_type_id = None
        self._number_of_units = None
        self._type_of_units = None
        self.discriminator = None

        if leave_name is not None:
            self.leave_name = leave_name
        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if type_of_units is not None:
            self.type_of_units = type_of_units

    @property
    def leave_name(self):
        """Gets the leave_name of this LeaveBalance.  # noqa: E501

        The name of the leave type  # noqa: E501

        :return: The leave_name of this LeaveBalance.  # noqa: E501
        :rtype: str
        """
        return self._leave_name

    @leave_name.setter
    def leave_name(self, leave_name):
        """Sets the leave_name of this LeaveBalance.

        The name of the leave type  # noqa: E501

        :param leave_name: The leave_name of this LeaveBalance.  # noqa: E501
        :type: str
        """

        self._leave_name = leave_name

    @property
    def leave_type_id(self):
        """Gets the leave_type_id of this LeaveBalance.  # noqa: E501

        Identifier of the leave type (see PayItems)  # noqa: E501

        :return: The leave_type_id of this LeaveBalance.  # noqa: E501
        :rtype: str
        """
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        """Sets the leave_type_id of this LeaveBalance.

        Identifier of the leave type (see PayItems)  # noqa: E501

        :param leave_type_id: The leave_type_id of this LeaveBalance.  # noqa: E501
        :type: str
        """

        self._leave_type_id = leave_type_id

    @property
    def number_of_units(self):
        """Gets the number_of_units of this LeaveBalance.  # noqa: E501

        The balance of the leave available  # noqa: E501

        :return: The number_of_units of this LeaveBalance.  # noqa: E501
        :rtype: float
        """
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        """Sets the number_of_units of this LeaveBalance.

        The balance of the leave available  # noqa: E501

        :param number_of_units: The number_of_units of this LeaveBalance.  # noqa: E501
        :type: float
        """

        self._number_of_units = number_of_units

    @property
    def type_of_units(self):
        """Gets the type_of_units of this LeaveBalance.  # noqa: E501

        The type of units as specified by the LeaveType (see PayItems)  # noqa: E501

        :return: The type_of_units of this LeaveBalance.  # noqa: E501
        :rtype: str
        """
        return self._type_of_units

    @type_of_units.setter
    def type_of_units(self, type_of_units):
        """Sets the type_of_units of this LeaveBalance.

        The type of units as specified by the LeaveType (see PayItems)  # noqa: E501

        :param type_of_units: The type_of_units of this LeaveBalance.  # noqa: E501
        :type: str
        """

        self._type_of_units = type_of_units
