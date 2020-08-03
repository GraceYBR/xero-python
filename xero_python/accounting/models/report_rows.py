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


class ReportRows(BaseModel):
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
        "row_type": "RowType",
        "title": "str",
        "cells": "list[ReportCell]",
        "rows": "list[ReportRow]",
    }

    attribute_map = {
        "row_type": "RowType",
        "title": "Title",
        "cells": "Cells",
        "rows": "Rows",
    }

    def __init__(self, row_type=None, title=None, cells=None, rows=None):  # noqa: E501
        """ReportRows - a model defined in OpenAPI"""  # noqa: E501

        self._row_type = None
        self._title = None
        self._cells = None
        self._rows = None
        self.discriminator = None

        if row_type is not None:
            self.row_type = row_type
        if title is not None:
            self.title = title
        if cells is not None:
            self.cells = cells
        if rows is not None:
            self.rows = rows

    @property
    def row_type(self):
        """Gets the row_type of this ReportRows.  # noqa: E501


        :return: The row_type of this ReportRows.  # noqa: E501
        :rtype: RowType
        """
        return self._row_type

    @row_type.setter
    def row_type(self, row_type):
        """Sets the row_type of this ReportRows.


        :param row_type: The row_type of this ReportRows.  # noqa: E501
        :type: RowType
        """

        self._row_type = row_type

    @property
    def title(self):
        """Gets the title of this ReportRows.  # noqa: E501


        :return: The title of this ReportRows.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ReportRows.


        :param title: The title of this ReportRows.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def cells(self):
        """Gets the cells of this ReportRows.  # noqa: E501


        :return: The cells of this ReportRows.  # noqa: E501
        :rtype: list[ReportCell]
        """
        return self._cells

    @cells.setter
    def cells(self, cells):
        """Sets the cells of this ReportRows.


        :param cells: The cells of this ReportRows.  # noqa: E501
        :type: list[ReportCell]
        """

        self._cells = cells

    @property
    def rows(self):
        """Gets the rows of this ReportRows.  # noqa: E501


        :return: The rows of this ReportRows.  # noqa: E501
        :rtype: list[ReportRow]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this ReportRows.


        :param rows: The rows of this ReportRows.  # noqa: E501
        :type: list[ReportRow]
        """

        self._rows = rows
