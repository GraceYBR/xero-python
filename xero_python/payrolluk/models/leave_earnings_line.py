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


class LeaveEarningsLine(BaseModel):
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
        "earnings_rate_id": "str",
        "rate_per_unit": "float",
        "number_of_units": "float",
        "fixed_amount": "float",
        "amount": "float",
        "is_linked_to_timesheet": "bool",
    }

    attribute_map = {
        "earnings_rate_id": "earningsRateID",
        "rate_per_unit": "ratePerUnit",
        "number_of_units": "numberOfUnits",
        "fixed_amount": "fixedAmount",
        "amount": "amount",
        "is_linked_to_timesheet": "isLinkedToTimesheet",
    }

    def __init__(
        self,
        earnings_rate_id=None,
        rate_per_unit=None,
        number_of_units=None,
        fixed_amount=None,
        amount=None,
        is_linked_to_timesheet=None,
    ):  # noqa: E501
        """LeaveEarningsLine - a model defined in OpenAPI"""  # noqa: E501

        self._earnings_rate_id = None
        self._rate_per_unit = None
        self._number_of_units = None
        self._fixed_amount = None
        self._amount = None
        self._is_linked_to_timesheet = None
        self.discriminator = None

        if earnings_rate_id is not None:
            self.earnings_rate_id = earnings_rate_id
        if rate_per_unit is not None:
            self.rate_per_unit = rate_per_unit
        if number_of_units is not None:
            self.number_of_units = number_of_units
        if fixed_amount is not None:
            self.fixed_amount = fixed_amount
        if amount is not None:
            self.amount = amount
        if is_linked_to_timesheet is not None:
            self.is_linked_to_timesheet = is_linked_to_timesheet

    @property
    def earnings_rate_id(self):
        """Gets the earnings_rate_id of this LeaveEarningsLine.  # noqa: E501

        Xero identifier for payroll leave earnings rate  # noqa: E501

        :return: The earnings_rate_id of this LeaveEarningsLine.  # noqa: E501
        :rtype: str
        """
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        """Sets the earnings_rate_id of this LeaveEarningsLine.

        Xero identifier for payroll leave earnings rate  # noqa: E501

        :param earnings_rate_id: The earnings_rate_id of this LeaveEarningsLine.  # noqa: E501
        :type: str
        """

        self._earnings_rate_id = earnings_rate_id

    @property
    def rate_per_unit(self):
        """Gets the rate_per_unit of this LeaveEarningsLine.  # noqa: E501

        Rate per unit for leave earnings line  # noqa: E501

        :return: The rate_per_unit of this LeaveEarningsLine.  # noqa: E501
        :rtype: float
        """
        return self._rate_per_unit

    @rate_per_unit.setter
    def rate_per_unit(self, rate_per_unit):
        """Sets the rate_per_unit of this LeaveEarningsLine.

        Rate per unit for leave earnings line  # noqa: E501

        :param rate_per_unit: The rate_per_unit of this LeaveEarningsLine.  # noqa: E501
        :type: float
        """

        self._rate_per_unit = rate_per_unit

    @property
    def number_of_units(self):
        """Gets the number_of_units of this LeaveEarningsLine.  # noqa: E501

        Leave earnings number of units  # noqa: E501

        :return: The number_of_units of this LeaveEarningsLine.  # noqa: E501
        :rtype: float
        """
        return self._number_of_units

    @number_of_units.setter
    def number_of_units(self, number_of_units):
        """Sets the number_of_units of this LeaveEarningsLine.

        Leave earnings number of units  # noqa: E501

        :param number_of_units: The number_of_units of this LeaveEarningsLine.  # noqa: E501
        :type: float
        """

        self._number_of_units = number_of_units

    @property
    def fixed_amount(self):
        """Gets the fixed_amount of this LeaveEarningsLine.  # noqa: E501

        Leave earnings fixed amount. Only applicable if the EarningsRate RateType is Fixed  # noqa: E501

        :return: The fixed_amount of this LeaveEarningsLine.  # noqa: E501
        :rtype: float
        """
        return self._fixed_amount

    @fixed_amount.setter
    def fixed_amount(self, fixed_amount):
        """Sets the fixed_amount of this LeaveEarningsLine.

        Leave earnings fixed amount. Only applicable if the EarningsRate RateType is Fixed  # noqa: E501

        :param fixed_amount: The fixed_amount of this LeaveEarningsLine.  # noqa: E501
        :type: float
        """

        self._fixed_amount = fixed_amount

    @property
    def amount(self):
        """Gets the amount of this LeaveEarningsLine.  # noqa: E501

        The amount of the earnings line.  # noqa: E501

        :return: The amount of this LeaveEarningsLine.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this LeaveEarningsLine.

        The amount of the earnings line.  # noqa: E501

        :param amount: The amount of this LeaveEarningsLine.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def is_linked_to_timesheet(self):
        """Gets the is_linked_to_timesheet of this LeaveEarningsLine.  # noqa: E501

        Identifies if the leave earnings is taken from the timesheet. False for leave earnings line  # noqa: E501

        :return: The is_linked_to_timesheet of this LeaveEarningsLine.  # noqa: E501
        :rtype: bool
        """
        return self._is_linked_to_timesheet

    @is_linked_to_timesheet.setter
    def is_linked_to_timesheet(self, is_linked_to_timesheet):
        """Sets the is_linked_to_timesheet of this LeaveEarningsLine.

        Identifies if the leave earnings is taken from the timesheet. False for leave earnings line  # noqa: E501

        :param is_linked_to_timesheet: The is_linked_to_timesheet of this LeaveEarningsLine.  # noqa: E501
        :type: bool
        """

        self._is_linked_to_timesheet = is_linked_to_timesheet
