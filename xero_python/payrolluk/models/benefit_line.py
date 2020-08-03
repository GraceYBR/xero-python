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


class BenefitLine(BaseModel):
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
        "benefit_type_id": "str",
        "display_name": "str",
        "amount": "float",
        "fixed_amount": "float",
        "percentage": "float",
    }

    attribute_map = {
        "benefit_type_id": "benefitTypeID",
        "display_name": "displayName",
        "amount": "amount",
        "fixed_amount": "fixedAmount",
        "percentage": "percentage",
    }

    def __init__(
        self,
        benefit_type_id=None,
        display_name=None,
        amount=None,
        fixed_amount=None,
        percentage=None,
    ):  # noqa: E501
        """BenefitLine - a model defined in OpenAPI"""  # noqa: E501

        self._benefit_type_id = None
        self._display_name = None
        self._amount = None
        self._fixed_amount = None
        self._percentage = None
        self.discriminator = None

        if benefit_type_id is not None:
            self.benefit_type_id = benefit_type_id
        if display_name is not None:
            self.display_name = display_name
        if amount is not None:
            self.amount = amount
        if fixed_amount is not None:
            self.fixed_amount = fixed_amount
        if percentage is not None:
            self.percentage = percentage

    @property
    def benefit_type_id(self):
        """Gets the benefit_type_id of this BenefitLine.  # noqa: E501

        Xero identifier for payroll benefit type  # noqa: E501

        :return: The benefit_type_id of this BenefitLine.  # noqa: E501
        :rtype: str
        """
        return self._benefit_type_id

    @benefit_type_id.setter
    def benefit_type_id(self, benefit_type_id):
        """Sets the benefit_type_id of this BenefitLine.

        Xero identifier for payroll benefit type  # noqa: E501

        :param benefit_type_id: The benefit_type_id of this BenefitLine.  # noqa: E501
        :type: str
        """

        self._benefit_type_id = benefit_type_id

    @property
    def display_name(self):
        """Gets the display_name of this BenefitLine.  # noqa: E501

        Benefit display name  # noqa: E501

        :return: The display_name of this BenefitLine.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this BenefitLine.

        Benefit display name  # noqa: E501

        :param display_name: The display_name of this BenefitLine.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def amount(self):
        """Gets the amount of this BenefitLine.  # noqa: E501

        The amount of the benefit line.  # noqa: E501

        :return: The amount of this BenefitLine.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BenefitLine.

        The amount of the benefit line.  # noqa: E501

        :param amount: The amount of this BenefitLine.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def fixed_amount(self):
        """Gets the fixed_amount of this BenefitLine.  # noqa: E501

        Benefit fixed amount  # noqa: E501

        :return: The fixed_amount of this BenefitLine.  # noqa: E501
        :rtype: float
        """
        return self._fixed_amount

    @fixed_amount.setter
    def fixed_amount(self, fixed_amount):
        """Sets the fixed_amount of this BenefitLine.

        Benefit fixed amount  # noqa: E501

        :param fixed_amount: The fixed_amount of this BenefitLine.  # noqa: E501
        :type: float
        """

        self._fixed_amount = fixed_amount

    @property
    def percentage(self):
        """Gets the percentage of this BenefitLine.  # noqa: E501

        Benefit rate percentage  # noqa: E501

        :return: The percentage of this BenefitLine.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this BenefitLine.

        Benefit rate percentage  # noqa: E501

        :param percentage: The percentage of this BenefitLine.  # noqa: E501
        :type: float
        """

        self._percentage = percentage
