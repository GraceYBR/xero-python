# coding: utf-8

"""
    Xero Projects API

    This is the Xero Projects API  # noqa: E501

    OpenAPI spec version: 2.2.10
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ProjectCreateOrUpdate(BaseModel):
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
        "contact_id": "str",
        "name": "str",
        "estimate_amount": "float",
        "deadline_utc": "datetime",
    }

    attribute_map = {
        "contact_id": "contactId",
        "name": "name",
        "estimate_amount": "estimateAmount",
        "deadline_utc": "deadlineUtc",
    }

    def __init__(
        self, contact_id=None, name=None, estimate_amount=None, deadline_utc=None
    ):  # noqa: E501
        """ProjectCreateOrUpdate - a model defined in OpenAPI"""  # noqa: E501

        self._contact_id = None
        self._name = None
        self._estimate_amount = None
        self._deadline_utc = None
        self.discriminator = None

        if contact_id is not None:
            self.contact_id = contact_id
        self.name = name
        if estimate_amount is not None:
            self.estimate_amount = estimate_amount
        if deadline_utc is not None:
            self.deadline_utc = deadline_utc

    @property
    def contact_id(self):
        """Gets the contact_id of this ProjectCreateOrUpdate.  # noqa: E501

        Identifier of the contact this project was created for.  # noqa: E501

        :return: The contact_id of this ProjectCreateOrUpdate.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this ProjectCreateOrUpdate.

        Identifier of the contact this project was created for.  # noqa: E501

        :param contact_id: The contact_id of this ProjectCreateOrUpdate.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def name(self):
        """Gets the name of this ProjectCreateOrUpdate.  # noqa: E501

        Name of the project.  # noqa: E501

        :return: The name of this ProjectCreateOrUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectCreateOrUpdate.

        Name of the project.  # noqa: E501

        :param name: The name of this ProjectCreateOrUpdate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def estimate_amount(self):
        """Gets the estimate_amount of this ProjectCreateOrUpdate.  # noqa: E501


        :return: The estimate_amount of this ProjectCreateOrUpdate.  # noqa: E501
        :rtype: float
        """
        return self._estimate_amount

    @estimate_amount.setter
    def estimate_amount(self, estimate_amount):
        """Sets the estimate_amount of this ProjectCreateOrUpdate.


        :param estimate_amount: The estimate_amount of this ProjectCreateOrUpdate.  # noqa: E501
        :type: float
        """

        self._estimate_amount = estimate_amount

    @property
    def deadline_utc(self):
        """Gets the deadline_utc of this ProjectCreateOrUpdate.  # noqa: E501

        Deadline for the project. UTC Date Time in ISO-8601 format.  # noqa: E501

        :return: The deadline_utc of this ProjectCreateOrUpdate.  # noqa: E501
        :rtype: datetime
        """
        return self._deadline_utc

    @deadline_utc.setter
    def deadline_utc(self, deadline_utc):
        """Sets the deadline_utc of this ProjectCreateOrUpdate.

        Deadline for the project. UTC Date Time in ISO-8601 format.  # noqa: E501

        :param deadline_utc: The deadline_utc of this ProjectCreateOrUpdate.  # noqa: E501
        :type: datetime
        """

        self._deadline_utc = deadline_utc
