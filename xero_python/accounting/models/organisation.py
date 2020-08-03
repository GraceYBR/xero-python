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


class Organisation(BaseModel):
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
        "organisation_id": "str",
        "api_key": "str",
        "name": "str",
        "legal_name": "str",
        "pays_tax": "bool",
        "version": "str",
        "organisation_type": "str",
        "base_currency": "CurrencyCode",
        "country_code": "CountryCode",
        "is_demo_company": "bool",
        "organisation_status": "str",
        "registration_number": "str",
        "employer_identification_number": "str",
        "tax_number": "str",
        "financial_year_end_day": "int",
        "financial_year_end_month": "int",
        "sales_tax_basis": "str",
        "sales_tax_period": "str",
        "default_sales_tax": "str",
        "default_purchases_tax": "str",
        "period_lock_date": "date[ms-format]",
        "end_of_year_lock_date": "date[ms-format]",
        "created_date_utc": "datetime[ms-format]",
        "timezone": "TimeZone",
        "organisation_entity_type": "str",
        "short_code": "str",
        "_class": "str",
        "edition": "str",
        "line_of_business": "str",
        "addresses": "list[Address]",
        "phones": "list[Phone]",
        "external_links": "list[ExternalLink]",
        "payment_terms": "PaymentTerm",
    }

    attribute_map = {
        "organisation_id": "OrganisationID",
        "api_key": "APIKey",
        "name": "Name",
        "legal_name": "LegalName",
        "pays_tax": "PaysTax",
        "version": "Version",
        "organisation_type": "OrganisationType",
        "base_currency": "BaseCurrency",
        "country_code": "CountryCode",
        "is_demo_company": "IsDemoCompany",
        "organisation_status": "OrganisationStatus",
        "registration_number": "RegistrationNumber",
        "employer_identification_number": "EmployerIdentificationNumber",
        "tax_number": "TaxNumber",
        "financial_year_end_day": "FinancialYearEndDay",
        "financial_year_end_month": "FinancialYearEndMonth",
        "sales_tax_basis": "SalesTaxBasis",
        "sales_tax_period": "SalesTaxPeriod",
        "default_sales_tax": "DefaultSalesTax",
        "default_purchases_tax": "DefaultPurchasesTax",
        "period_lock_date": "PeriodLockDate",
        "end_of_year_lock_date": "EndOfYearLockDate",
        "created_date_utc": "CreatedDateUTC",
        "timezone": "Timezone",
        "organisation_entity_type": "OrganisationEntityType",
        "short_code": "ShortCode",
        "_class": "Class",
        "edition": "Edition",
        "line_of_business": "LineOfBusiness",
        "addresses": "Addresses",
        "phones": "Phones",
        "external_links": "ExternalLinks",
        "payment_terms": "PaymentTerms",
    }

    def __init__(
        self,
        organisation_id=None,
        api_key=None,
        name=None,
        legal_name=None,
        pays_tax=None,
        version=None,
        organisation_type=None,
        base_currency=None,
        country_code=None,
        is_demo_company=None,
        organisation_status=None,
        registration_number=None,
        employer_identification_number=None,
        tax_number=None,
        financial_year_end_day=None,
        financial_year_end_month=None,
        sales_tax_basis=None,
        sales_tax_period=None,
        default_sales_tax=None,
        default_purchases_tax=None,
        period_lock_date=None,
        end_of_year_lock_date=None,
        created_date_utc=None,
        timezone=None,
        organisation_entity_type=None,
        short_code=None,
        _class=None,
        edition=None,
        line_of_business=None,
        addresses=None,
        phones=None,
        external_links=None,
        payment_terms=None,
    ):  # noqa: E501
        """Organisation - a model defined in OpenAPI"""  # noqa: E501

        self._organisation_id = None
        self._api_key = None
        self._name = None
        self._legal_name = None
        self._pays_tax = None
        self._version = None
        self._organisation_type = None
        self._base_currency = None
        self._country_code = None
        self._is_demo_company = None
        self._organisation_status = None
        self._registration_number = None
        self._employer_identification_number = None
        self._tax_number = None
        self._financial_year_end_day = None
        self._financial_year_end_month = None
        self._sales_tax_basis = None
        self._sales_tax_period = None
        self._default_sales_tax = None
        self._default_purchases_tax = None
        self._period_lock_date = None
        self._end_of_year_lock_date = None
        self._created_date_utc = None
        self._timezone = None
        self._organisation_entity_type = None
        self._short_code = None
        self.__class = None
        self._edition = None
        self._line_of_business = None
        self._addresses = None
        self._phones = None
        self._external_links = None
        self._payment_terms = None
        self.discriminator = None

        if organisation_id is not None:
            self.organisation_id = organisation_id
        if api_key is not None:
            self.api_key = api_key
        if name is not None:
            self.name = name
        if legal_name is not None:
            self.legal_name = legal_name
        if pays_tax is not None:
            self.pays_tax = pays_tax
        if version is not None:
            self.version = version
        if organisation_type is not None:
            self.organisation_type = organisation_type
        if base_currency is not None:
            self.base_currency = base_currency
        if country_code is not None:
            self.country_code = country_code
        if is_demo_company is not None:
            self.is_demo_company = is_demo_company
        if organisation_status is not None:
            self.organisation_status = organisation_status
        if registration_number is not None:
            self.registration_number = registration_number
        if employer_identification_number is not None:
            self.employer_identification_number = employer_identification_number
        if tax_number is not None:
            self.tax_number = tax_number
        if financial_year_end_day is not None:
            self.financial_year_end_day = financial_year_end_day
        if financial_year_end_month is not None:
            self.financial_year_end_month = financial_year_end_month
        if sales_tax_basis is not None:
            self.sales_tax_basis = sales_tax_basis
        if sales_tax_period is not None:
            self.sales_tax_period = sales_tax_period
        if default_sales_tax is not None:
            self.default_sales_tax = default_sales_tax
        if default_purchases_tax is not None:
            self.default_purchases_tax = default_purchases_tax
        if period_lock_date is not None:
            self.period_lock_date = period_lock_date
        if end_of_year_lock_date is not None:
            self.end_of_year_lock_date = end_of_year_lock_date
        if created_date_utc is not None:
            self.created_date_utc = created_date_utc
        if timezone is not None:
            self.timezone = timezone
        if organisation_entity_type is not None:
            self.organisation_entity_type = organisation_entity_type
        if short_code is not None:
            self.short_code = short_code
        if _class is not None:
            self._class = _class
        if edition is not None:
            self.edition = edition
        if line_of_business is not None:
            self.line_of_business = line_of_business
        if addresses is not None:
            self.addresses = addresses
        if phones is not None:
            self.phones = phones
        if external_links is not None:
            self.external_links = external_links
        if payment_terms is not None:
            self.payment_terms = payment_terms

    @property
    def organisation_id(self):
        """Gets the organisation_id of this Organisation.  # noqa: E501

        Unique Xero identifier  # noqa: E501

        :return: The organisation_id of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this Organisation.

        Unique Xero identifier  # noqa: E501

        :param organisation_id: The organisation_id of this Organisation.  # noqa: E501
        :type: str
        """

        self._organisation_id = organisation_id

    @property
    def api_key(self):
        """Gets the api_key of this Organisation.  # noqa: E501

        Display a unique key used for Xero-to-Xero transactions  # noqa: E501

        :return: The api_key of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this Organisation.

        Display a unique key used for Xero-to-Xero transactions  # noqa: E501

        :param api_key: The api_key of this Organisation.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def name(self):
        """Gets the name of this Organisation.  # noqa: E501

        Display name of organisation shown in Xero  # noqa: E501

        :return: The name of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Organisation.

        Display name of organisation shown in Xero  # noqa: E501

        :param name: The name of this Organisation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def legal_name(self):
        """Gets the legal_name of this Organisation.  # noqa: E501

        Organisation name shown on Reports  # noqa: E501

        :return: The legal_name of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._legal_name

    @legal_name.setter
    def legal_name(self, legal_name):
        """Sets the legal_name of this Organisation.

        Organisation name shown on Reports  # noqa: E501

        :param legal_name: The legal_name of this Organisation.  # noqa: E501
        :type: str
        """

        self._legal_name = legal_name

    @property
    def pays_tax(self):
        """Gets the pays_tax of this Organisation.  # noqa: E501

        Boolean to describe if organisation is registered with a local tax authority i.e. true, false  # noqa: E501

        :return: The pays_tax of this Organisation.  # noqa: E501
        :rtype: bool
        """
        return self._pays_tax

    @pays_tax.setter
    def pays_tax(self, pays_tax):
        """Sets the pays_tax of this Organisation.

        Boolean to describe if organisation is registered with a local tax authority i.e. true, false  # noqa: E501

        :param pays_tax: The pays_tax of this Organisation.  # noqa: E501
        :type: bool
        """

        self._pays_tax = pays_tax

    @property
    def version(self):
        """Gets the version of this Organisation.  # noqa: E501

        See Version Types  # noqa: E501

        :return: The version of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Organisation.

        See Version Types  # noqa: E501

        :param version: The version of this Organisation.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "AU",
            "NZ",
            "GLOBAL",
            "UK",
            "US",
            "AUONRAMP",
            "NZONRAMP",
            "GLOBALONRAMP",
            "UKONRAMP",
            "USONRAMP",
            "None",
        ]  # noqa: E501
        if version not in allowed_values:
            raise ValueError(
                "Invalid value for `version` ({0}), must be one of {1}".format(  # noqa: E501
                    version, allowed_values
                )
            )

        self._version = version

    @property
    def organisation_type(self):
        """Gets the organisation_type of this Organisation.  # noqa: E501

        Organisation Type  # noqa: E501

        :return: The organisation_type of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._organisation_type

    @organisation_type.setter
    def organisation_type(self, organisation_type):
        """Sets the organisation_type of this Organisation.

        Organisation Type  # noqa: E501

        :param organisation_type: The organisation_type of this Organisation.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "ACCOUNTING_PRACTICE",
            "COMPANY",
            "CHARITY",
            "CLUB_OR_SOCIETY",
            "LOOK_THROUGH_COMPANY",
            "NOT_FOR_PROFIT",
            "PARTNERSHIP",
            "S_CORPORATION",
            "SELF_MANAGED_SUPERANNUATION_FUND",
            "SOLE_TRADER",
            "SUPERANNUATION_FUND",
            "TRUST",
            "None",
        ]  # noqa: E501
        if organisation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `organisation_type` ({0}), must be one of {1}".format(  # noqa: E501
                    organisation_type, allowed_values
                )
            )

        self._organisation_type = organisation_type

    @property
    def base_currency(self):
        """Gets the base_currency of this Organisation.  # noqa: E501


        :return: The base_currency of this Organisation.  # noqa: E501
        :rtype: CurrencyCode
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this Organisation.


        :param base_currency: The base_currency of this Organisation.  # noqa: E501
        :type: CurrencyCode
        """

        self._base_currency = base_currency

    @property
    def country_code(self):
        """Gets the country_code of this Organisation.  # noqa: E501


        :return: The country_code of this Organisation.  # noqa: E501
        :rtype: CountryCode
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Organisation.


        :param country_code: The country_code of this Organisation.  # noqa: E501
        :type: CountryCode
        """

        self._country_code = country_code

    @property
    def is_demo_company(self):
        """Gets the is_demo_company of this Organisation.  # noqa: E501

        Boolean to describe if organisation is a demo company.  # noqa: E501

        :return: The is_demo_company of this Organisation.  # noqa: E501
        :rtype: bool
        """
        return self._is_demo_company

    @is_demo_company.setter
    def is_demo_company(self, is_demo_company):
        """Sets the is_demo_company of this Organisation.

        Boolean to describe if organisation is a demo company.  # noqa: E501

        :param is_demo_company: The is_demo_company of this Organisation.  # noqa: E501
        :type: bool
        """

        self._is_demo_company = is_demo_company

    @property
    def organisation_status(self):
        """Gets the organisation_status of this Organisation.  # noqa: E501

        Will be set to ACTIVE if you can connect to organisation via the Xero API  # noqa: E501

        :return: The organisation_status of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._organisation_status

    @organisation_status.setter
    def organisation_status(self, organisation_status):
        """Sets the organisation_status of this Organisation.

        Will be set to ACTIVE if you can connect to organisation via the Xero API  # noqa: E501

        :param organisation_status: The organisation_status of this Organisation.  # noqa: E501
        :type: str
        """

        self._organisation_status = organisation_status

    @property
    def registration_number(self):
        """Gets the registration_number of this Organisation.  # noqa: E501

        Shows for New Zealand, Australian and UK organisations  # noqa: E501

        :return: The registration_number of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._registration_number

    @registration_number.setter
    def registration_number(self, registration_number):
        """Sets the registration_number of this Organisation.

        Shows for New Zealand, Australian and UK organisations  # noqa: E501

        :param registration_number: The registration_number of this Organisation.  # noqa: E501
        :type: str
        """

        self._registration_number = registration_number

    @property
    def employer_identification_number(self):
        """Gets the employer_identification_number of this Organisation.  # noqa: E501

        Shown if set. US Only.  # noqa: E501

        :return: The employer_identification_number of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._employer_identification_number

    @employer_identification_number.setter
    def employer_identification_number(self, employer_identification_number):
        """Sets the employer_identification_number of this Organisation.

        Shown if set. US Only.  # noqa: E501

        :param employer_identification_number: The employer_identification_number of this Organisation.  # noqa: E501
        :type: str
        """

        self._employer_identification_number = employer_identification_number

    @property
    def tax_number(self):
        """Gets the tax_number of this Organisation.  # noqa: E501

        Shown if set. Displays in the Xero UI as Tax File Number (AU), GST Number (NZ), VAT Number (UK) and Tax ID Number (US & Global).  # noqa: E501

        :return: The tax_number of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number):
        """Sets the tax_number of this Organisation.

        Shown if set. Displays in the Xero UI as Tax File Number (AU), GST Number (NZ), VAT Number (UK) and Tax ID Number (US & Global).  # noqa: E501

        :param tax_number: The tax_number of this Organisation.  # noqa: E501
        :type: str
        """

        self._tax_number = tax_number

    @property
    def financial_year_end_day(self):
        """Gets the financial_year_end_day of this Organisation.  # noqa: E501

        Calendar day e.g. 0-31  # noqa: E501

        :return: The financial_year_end_day of this Organisation.  # noqa: E501
        :rtype: int
        """
        return self._financial_year_end_day

    @financial_year_end_day.setter
    def financial_year_end_day(self, financial_year_end_day):
        """Sets the financial_year_end_day of this Organisation.

        Calendar day e.g. 0-31  # noqa: E501

        :param financial_year_end_day: The financial_year_end_day of this Organisation.  # noqa: E501
        :type: int
        """

        self._financial_year_end_day = financial_year_end_day

    @property
    def financial_year_end_month(self):
        """Gets the financial_year_end_month of this Organisation.  # noqa: E501

        Calendar Month e.g. 1-12  # noqa: E501

        :return: The financial_year_end_month of this Organisation.  # noqa: E501
        :rtype: int
        """
        return self._financial_year_end_month

    @financial_year_end_month.setter
    def financial_year_end_month(self, financial_year_end_month):
        """Sets the financial_year_end_month of this Organisation.

        Calendar Month e.g. 1-12  # noqa: E501

        :param financial_year_end_month: The financial_year_end_month of this Organisation.  # noqa: E501
        :type: int
        """

        self._financial_year_end_month = financial_year_end_month

    @property
    def sales_tax_basis(self):
        """Gets the sales_tax_basis of this Organisation.  # noqa: E501

        The accounting basis used for tax returns. See Sales Tax Basis  # noqa: E501

        :return: The sales_tax_basis of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._sales_tax_basis

    @sales_tax_basis.setter
    def sales_tax_basis(self, sales_tax_basis):
        """Sets the sales_tax_basis of this Organisation.

        The accounting basis used for tax returns. See Sales Tax Basis  # noqa: E501

        :param sales_tax_basis: The sales_tax_basis of this Organisation.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "PAYMENTS",
            "INVOICE",
            "NONE",
            "CASH",
            "ACCRUAL",
            "FLATRATECASH",
            "FLATRATEACCRUAL",
            "ACCRUALS",
            "None",
        ]  # noqa: E501
        if sales_tax_basis not in allowed_values:
            raise ValueError(
                "Invalid value for `sales_tax_basis` ({0}), must be one of {1}".format(  # noqa: E501
                    sales_tax_basis, allowed_values
                )
            )

        self._sales_tax_basis = sales_tax_basis

    @property
    def sales_tax_period(self):
        """Gets the sales_tax_period of this Organisation.  # noqa: E501

        The frequency with which tax returns are processed. See Sales Tax Period  # noqa: E501

        :return: The sales_tax_period of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._sales_tax_period

    @sales_tax_period.setter
    def sales_tax_period(self, sales_tax_period):
        """Sets the sales_tax_period of this Organisation.

        The frequency with which tax returns are processed. See Sales Tax Period  # noqa: E501

        :param sales_tax_period: The sales_tax_period of this Organisation.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "MONTHLY",
            "QUARTERLY1",
            "QUARTERLY2",
            "QUARTERLY3",
            "ANNUALLY",
            "ONEMONTHS",
            "TWOMONTHS",
            "SIXMONTHS",
            "1MONTHLY",
            "2MONTHLY",
            "3MONTHLY",
            "6MONTHLY",
            "QUARTERLY",
            "YEARLY",
            "NONE",
            "None",
        ]  # noqa: E501
        if sales_tax_period not in allowed_values:
            raise ValueError(
                "Invalid value for `sales_tax_period` ({0}), must be one of {1}".format(  # noqa: E501
                    sales_tax_period, allowed_values
                )
            )

        self._sales_tax_period = sales_tax_period

    @property
    def default_sales_tax(self):
        """Gets the default_sales_tax of this Organisation.  # noqa: E501

        The default for LineAmountTypes on sales transactions  # noqa: E501

        :return: The default_sales_tax of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._default_sales_tax

    @default_sales_tax.setter
    def default_sales_tax(self, default_sales_tax):
        """Sets the default_sales_tax of this Organisation.

        The default for LineAmountTypes on sales transactions  # noqa: E501

        :param default_sales_tax: The default_sales_tax of this Organisation.  # noqa: E501
        :type: str
        """

        self._default_sales_tax = default_sales_tax

    @property
    def default_purchases_tax(self):
        """Gets the default_purchases_tax of this Organisation.  # noqa: E501

        The default for LineAmountTypes on purchase transactions  # noqa: E501

        :return: The default_purchases_tax of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._default_purchases_tax

    @default_purchases_tax.setter
    def default_purchases_tax(self, default_purchases_tax):
        """Sets the default_purchases_tax of this Organisation.

        The default for LineAmountTypes on purchase transactions  # noqa: E501

        :param default_purchases_tax: The default_purchases_tax of this Organisation.  # noqa: E501
        :type: str
        """

        self._default_purchases_tax = default_purchases_tax

    @property
    def period_lock_date(self):
        """Gets the period_lock_date of this Organisation.  # noqa: E501

        Shown if set. See lock dates  # noqa: E501

        :return: The period_lock_date of this Organisation.  # noqa: E501
        :rtype: date
        """
        return self._period_lock_date

    @period_lock_date.setter
    def period_lock_date(self, period_lock_date):
        """Sets the period_lock_date of this Organisation.

        Shown if set. See lock dates  # noqa: E501

        :param period_lock_date: The period_lock_date of this Organisation.  # noqa: E501
        :type: date
        """

        self._period_lock_date = period_lock_date

    @property
    def end_of_year_lock_date(self):
        """Gets the end_of_year_lock_date of this Organisation.  # noqa: E501

        Shown if set. See lock dates  # noqa: E501

        :return: The end_of_year_lock_date of this Organisation.  # noqa: E501
        :rtype: date
        """
        return self._end_of_year_lock_date

    @end_of_year_lock_date.setter
    def end_of_year_lock_date(self, end_of_year_lock_date):
        """Sets the end_of_year_lock_date of this Organisation.

        Shown if set. See lock dates  # noqa: E501

        :param end_of_year_lock_date: The end_of_year_lock_date of this Organisation.  # noqa: E501
        :type: date
        """

        self._end_of_year_lock_date = end_of_year_lock_date

    @property
    def created_date_utc(self):
        """Gets the created_date_utc of this Organisation.  # noqa: E501

        Timestamp when the organisation was created in Xero  # noqa: E501

        :return: The created_date_utc of this Organisation.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_utc

    @created_date_utc.setter
    def created_date_utc(self, created_date_utc):
        """Sets the created_date_utc of this Organisation.

        Timestamp when the organisation was created in Xero  # noqa: E501

        :param created_date_utc: The created_date_utc of this Organisation.  # noqa: E501
        :type: datetime
        """

        self._created_date_utc = created_date_utc

    @property
    def timezone(self):
        """Gets the timezone of this Organisation.  # noqa: E501


        :return: The timezone of this Organisation.  # noqa: E501
        :rtype: TimeZone
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this Organisation.


        :param timezone: The timezone of this Organisation.  # noqa: E501
        :type: TimeZone
        """

        self._timezone = timezone

    @property
    def organisation_entity_type(self):
        """Gets the organisation_entity_type of this Organisation.  # noqa: E501

        Organisation Entity Type  # noqa: E501

        :return: The organisation_entity_type of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._organisation_entity_type

    @organisation_entity_type.setter
    def organisation_entity_type(self, organisation_entity_type):
        """Sets the organisation_entity_type of this Organisation.

        Organisation Entity Type  # noqa: E501

        :param organisation_entity_type: The organisation_entity_type of this Organisation.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "ACCOUNTING_PRACTICE",
            "COMPANY",
            "CHARITY",
            "CLUB_OR_SOCIETY",
            "LOOK_THROUGH_COMPANY",
            "NOT_FOR_PROFIT",
            "PARTNERSHIP",
            "S_CORPORATION",
            "SELF_MANAGED_SUPERANNUATION_FUND",
            "SOLE_TRADER",
            "SUPERANNUATION_FUND",
            "TRUST",
            "None",
        ]  # noqa: E501
        if organisation_entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `organisation_entity_type` ({0}), must be one of {1}".format(  # noqa: E501
                    organisation_entity_type, allowed_values
                )
            )

        self._organisation_entity_type = organisation_entity_type

    @property
    def short_code(self):
        """Gets the short_code of this Organisation.  # noqa: E501

        A unique identifier for the organisation. Potential uses.  # noqa: E501

        :return: The short_code of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._short_code

    @short_code.setter
    def short_code(self, short_code):
        """Sets the short_code of this Organisation.

        A unique identifier for the organisation. Potential uses.  # noqa: E501

        :param short_code: The short_code of this Organisation.  # noqa: E501
        :type: str
        """

        self._short_code = short_code

    @property
    def _class(self):
        """Gets the _class of this Organisation.  # noqa: E501

        Organisation Classes describe which plan the Xero organisation is on (e.g. DEMO, TRIAL, PREMIUM)  # noqa: E501

        :return: The _class of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Organisation.

        Organisation Classes describe which plan the Xero organisation is on (e.g. DEMO, TRIAL, PREMIUM)  # noqa: E501

        :param _class: The _class of this Organisation.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "DEMO",
            "TRIAL",
            "STARTER",
            "STANDARD",
            "PREMIUM",
            "PREMIUM_20",
            "PREMIUM_50",
            "PREMIUM_100",
            "LEDGER",
            "GST_CASHBOOK",
            "NON_GST_CASHBOOK",
            "None",
        ]  # noqa: E501
        if _class not in allowed_values:
            raise ValueError(
                "Invalid value for `_class` ({0}), must be one of {1}".format(  # noqa: E501
                    _class, allowed_values
                )
            )

        self.__class = _class

    @property
    def edition(self):
        """Gets the edition of this Organisation.  # noqa: E501

        BUSINESS or PARTNER. Partner edition organisations are sold exclusively through accounting partners and have restricted functionality (e.g. no access to invoicing)  # noqa: E501

        :return: The edition of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """Sets the edition of this Organisation.

        BUSINESS or PARTNER. Partner edition organisations are sold exclusively through accounting partners and have restricted functionality (e.g. no access to invoicing)  # noqa: E501

        :param edition: The edition of this Organisation.  # noqa: E501
        :type: str
        """
        allowed_values = ["BUSINESS", "PARTNER", "None"]  # noqa: E501
        if edition not in allowed_values:
            raise ValueError(
                "Invalid value for `edition` ({0}), must be one of {1}".format(  # noqa: E501
                    edition, allowed_values
                )
            )

        self._edition = edition

    @property
    def line_of_business(self):
        """Gets the line_of_business of this Organisation.  # noqa: E501

        Description of business type as defined in Organisation settings  # noqa: E501

        :return: The line_of_business of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._line_of_business

    @line_of_business.setter
    def line_of_business(self, line_of_business):
        """Sets the line_of_business of this Organisation.

        Description of business type as defined in Organisation settings  # noqa: E501

        :param line_of_business: The line_of_business of this Organisation.  # noqa: E501
        :type: str
        """

        self._line_of_business = line_of_business

    @property
    def addresses(self):
        """Gets the addresses of this Organisation.  # noqa: E501

        Address details for organisation – see Addresses  # noqa: E501

        :return: The addresses of this Organisation.  # noqa: E501
        :rtype: list[Address]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this Organisation.

        Address details for organisation – see Addresses  # noqa: E501

        :param addresses: The addresses of this Organisation.  # noqa: E501
        :type: list[Address]
        """

        self._addresses = addresses

    @property
    def phones(self):
        """Gets the phones of this Organisation.  # noqa: E501

        Phones details for organisation – see Phones  # noqa: E501

        :return: The phones of this Organisation.  # noqa: E501
        :rtype: list[Phone]
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        """Sets the phones of this Organisation.

        Phones details for organisation – see Phones  # noqa: E501

        :param phones: The phones of this Organisation.  # noqa: E501
        :type: list[Phone]
        """

        self._phones = phones

    @property
    def external_links(self):
        """Gets the external_links of this Organisation.  # noqa: E501

        Organisation profile links for popular services such as Facebook,Twitter, GooglePlus and LinkedIn. You can also add link to your website here. Shown if Organisation settings  is updated in Xero. See ExternalLinks below  # noqa: E501

        :return: The external_links of this Organisation.  # noqa: E501
        :rtype: list[ExternalLink]
        """
        return self._external_links

    @external_links.setter
    def external_links(self, external_links):
        """Sets the external_links of this Organisation.

        Organisation profile links for popular services such as Facebook,Twitter, GooglePlus and LinkedIn. You can also add link to your website here. Shown if Organisation settings  is updated in Xero. See ExternalLinks below  # noqa: E501

        :param external_links: The external_links of this Organisation.  # noqa: E501
        :type: list[ExternalLink]
        """

        self._external_links = external_links

    @property
    def payment_terms(self):
        """Gets the payment_terms of this Organisation.  # noqa: E501


        :return: The payment_terms of this Organisation.  # noqa: E501
        :rtype: PaymentTerm
        """
        return self._payment_terms

    @payment_terms.setter
    def payment_terms(self, payment_terms):
        """Sets the payment_terms of this Organisation.


        :param payment_terms: The payment_terms of this Organisation.  # noqa: E501
        :type: PaymentTerm
        """

        self._payment_terms = payment_terms
