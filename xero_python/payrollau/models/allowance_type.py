# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.2.10
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class AllowanceType(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    CAR = "CAR"
    TRANSPORT = "TRANSPORT"
    TRAVEL = "TRAVEL"
    LAUNDRY = "LAUNDRY"
    MEALS = "MEALS"
    JOBKEEPER = "JOBKEEPER"
    OTHER = "OTHER"
