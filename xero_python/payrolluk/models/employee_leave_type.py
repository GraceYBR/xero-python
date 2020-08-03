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


class EmployeeLeaveType(BaseModel):
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
        "leave_type_id": "str",
        "schedule_of_accrual": "str",
        "hours_accrued_annually": "float",
        "maximum_to_accrue": "float",
        "opening_balance": "float",
        "rate_accrued_hourly": "float",
    }

    attribute_map = {
        "leave_type_id": "leaveTypeID",
        "schedule_of_accrual": "scheduleOfAccrual",
        "hours_accrued_annually": "hoursAccruedAnnually",
        "maximum_to_accrue": "maximumToAccrue",
        "opening_balance": "openingBalance",
        "rate_accrued_hourly": "rateAccruedHourly",
    }

    def __init__(
        self,
        leave_type_id=None,
        schedule_of_accrual=None,
        hours_accrued_annually=None,
        maximum_to_accrue=None,
        opening_balance=None,
        rate_accrued_hourly=None,
    ):  # noqa: E501
        """EmployeeLeaveType - a model defined in OpenAPI"""  # noqa: E501

        self._leave_type_id = None
        self._schedule_of_accrual = None
        self._hours_accrued_annually = None
        self._maximum_to_accrue = None
        self._opening_balance = None
        self._rate_accrued_hourly = None
        self.discriminator = None

        self.leave_type_id = leave_type_id
        self.schedule_of_accrual = schedule_of_accrual
        if hours_accrued_annually is not None:
            self.hours_accrued_annually = hours_accrued_annually
        if maximum_to_accrue is not None:
            self.maximum_to_accrue = maximum_to_accrue
        if opening_balance is not None:
            self.opening_balance = opening_balance
        if rate_accrued_hourly is not None:
            self.rate_accrued_hourly = rate_accrued_hourly

    @property
    def leave_type_id(self):
        """Gets the leave_type_id of this EmployeeLeaveType.  # noqa: E501

        The Xero identifier for leave type  # noqa: E501

        :return: The leave_type_id of this EmployeeLeaveType.  # noqa: E501
        :rtype: str
        """
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        """Sets the leave_type_id of this EmployeeLeaveType.

        The Xero identifier for leave type  # noqa: E501

        :param leave_type_id: The leave_type_id of this EmployeeLeaveType.  # noqa: E501
        :type: str
        """
        if leave_type_id is None:
            raise ValueError(
                "Invalid value for `leave_type_id`, must not be `None`"
            )  # noqa: E501

        self._leave_type_id = leave_type_id

    @property
    def schedule_of_accrual(self):
        """Gets the schedule_of_accrual of this EmployeeLeaveType.  # noqa: E501

        The schedule of accrual  # noqa: E501

        :return: The schedule_of_accrual of this EmployeeLeaveType.  # noqa: E501
        :rtype: str
        """
        return self._schedule_of_accrual

    @schedule_of_accrual.setter
    def schedule_of_accrual(self, schedule_of_accrual):
        """Sets the schedule_of_accrual of this EmployeeLeaveType.

        The schedule of accrual  # noqa: E501

        :param schedule_of_accrual: The schedule_of_accrual of this EmployeeLeaveType.  # noqa: E501
        :type: str
        """
        if schedule_of_accrual is None:
            raise ValueError(
                "Invalid value for `schedule_of_accrual`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "BeginningOfCalendarYear",
            "OnAnniversaryDate",
            "EachPayPeriod",
            "OnHourWorked",
            "None",
        ]  # noqa: E501
        if schedule_of_accrual not in allowed_values:
            raise ValueError(
                "Invalid value for `schedule_of_accrual` ({0}), must be one of {1}".format(  # noqa: E501
                    schedule_of_accrual, allowed_values
                )
            )

        self._schedule_of_accrual = schedule_of_accrual

    @property
    def hours_accrued_annually(self):
        """Gets the hours_accrued_annually of this EmployeeLeaveType.  # noqa: E501

        The number of hours accrued for the leave annually. This is 0 when the scheduleOfAccrual chosen is \"OnHourWorked\"  # noqa: E501

        :return: The hours_accrued_annually of this EmployeeLeaveType.  # noqa: E501
        :rtype: float
        """
        return self._hours_accrued_annually

    @hours_accrued_annually.setter
    def hours_accrued_annually(self, hours_accrued_annually):
        """Sets the hours_accrued_annually of this EmployeeLeaveType.

        The number of hours accrued for the leave annually. This is 0 when the scheduleOfAccrual chosen is \"OnHourWorked\"  # noqa: E501

        :param hours_accrued_annually: The hours_accrued_annually of this EmployeeLeaveType.  # noqa: E501
        :type: float
        """

        self._hours_accrued_annually = hours_accrued_annually

    @property
    def maximum_to_accrue(self):
        """Gets the maximum_to_accrue of this EmployeeLeaveType.  # noqa: E501

        The maximum number of hours that can be accrued for the leave  # noqa: E501

        :return: The maximum_to_accrue of this EmployeeLeaveType.  # noqa: E501
        :rtype: float
        """
        return self._maximum_to_accrue

    @maximum_to_accrue.setter
    def maximum_to_accrue(self, maximum_to_accrue):
        """Sets the maximum_to_accrue of this EmployeeLeaveType.

        The maximum number of hours that can be accrued for the leave  # noqa: E501

        :param maximum_to_accrue: The maximum_to_accrue of this EmployeeLeaveType.  # noqa: E501
        :type: float
        """

        self._maximum_to_accrue = maximum_to_accrue

    @property
    def opening_balance(self):
        """Gets the opening_balance of this EmployeeLeaveType.  # noqa: E501

        The initial number of hours assigned when the leave was added to the employee  # noqa: E501

        :return: The opening_balance of this EmployeeLeaveType.  # noqa: E501
        :rtype: float
        """
        return self._opening_balance

    @opening_balance.setter
    def opening_balance(self, opening_balance):
        """Sets the opening_balance of this EmployeeLeaveType.

        The initial number of hours assigned when the leave was added to the employee  # noqa: E501

        :param opening_balance: The opening_balance of this EmployeeLeaveType.  # noqa: E501
        :type: float
        """

        self._opening_balance = opening_balance

    @property
    def rate_accrued_hourly(self):
        """Gets the rate_accrued_hourly of this EmployeeLeaveType.  # noqa: E501

        The number of hours added to the leave balance for every hour worked by the employee. This is normally 0, unless the scheduleOfAccrual chosen is \"OnHourWorked\"  # noqa: E501

        :return: The rate_accrued_hourly of this EmployeeLeaveType.  # noqa: E501
        :rtype: float
        """
        return self._rate_accrued_hourly

    @rate_accrued_hourly.setter
    def rate_accrued_hourly(self, rate_accrued_hourly):
        """Sets the rate_accrued_hourly of this EmployeeLeaveType.

        The number of hours added to the leave balance for every hour worked by the employee. This is normally 0, unless the scheduleOfAccrual chosen is \"OnHourWorked\"  # noqa: E501

        :param rate_accrued_hourly: The rate_accrued_hourly of this EmployeeLeaveType.  # noqa: E501
        :type: float
        """

        self._rate_accrued_hourly = rate_accrued_hourly
