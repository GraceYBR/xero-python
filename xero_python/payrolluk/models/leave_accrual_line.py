# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.2.10
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class LeaveAccrualLine(BaseModel):
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
    openapi_types = {"leave_type_id": "str", "number_of_units": "float"}

    attribute_map = {"leave_type_id": "leaveTypeID", "number_of_units": "numberOfUnits"}

    def __init__(self, leave_type_id=None, number_of_units=None):  # noqa: E501
        """LeaveAccrualLine - a model defined in OpenAPI"""  # noqa: E501

        self._leave_type_id = None
        self._number_of_units = None
        self.discriminator = None

        if leave_type_id is not None:
            self.leave_type_id = leave_type_id
        if number_of_units is not None:
            self.number_of_units = number_of_units

    @property
    def leave_type_id(self):
        """Gets the leave_type_id of this LeaveAccrualLine.  # noqa: E501

        Xero identifier for the Leave type  # noqa: E501

        :return: The leave_type_id of this LeaveAccrualLine.  # noqa: E501
        :rtype: str
        """
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        """Sets the leave_type_id of this LeaveAccrualLine.

        Xero identifier for the Leave type  # noqa: E501

        :param leave_type_id: The leave_type_id of this LeaveAccrualLine.  # noqa: E501
        :type: str
        """

        self._leave_type_id = leave_type_id

    @property
    def number_of_units(self):
        """Gets the number_of_units of this LeaveAccrualLine.  # noqa: E501

        Leave accrual number of units  # noqa: E501

        :return: The number_of_units of this LeaveAccrualLine.  # noqa: E501
        :rtype: float
        """
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        """Sets the number_of_units of this LeaveAccrualLine.

        Leave accrual number of units  # noqa: E501

        :param number_of_units: The number_of_units of this LeaveAccrualLine.  # noqa: E501
        :type: float
        """

        self._number_of_units = number_of_units
