# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import List, Optional, TYPE_CHECKING, Union

from .. import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Resource(_serialization.Model):
    """ARM resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class AgreementTerms(Resource):  # pylint: disable=too-many-instance-attributes
    """Terms properties for provided Publisher/Offer/Plan tuple.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar system_data: The system meta data relating to this resource.
    :vartype system_data: ~azure.mgmt.marketplaceordering.models.SystemData
    :ivar publisher: Publisher identifier string of image being deployed.
    :vartype publisher: str
    :ivar product: Offer identifier string of image being deployed.
    :vartype product: str
    :ivar plan: Plan identifier string of image being deployed.
    :vartype plan: str
    :ivar license_text_link: Link to HTML with Microsoft and Publisher terms.
    :vartype license_text_link: str
    :ivar privacy_policy_link: Link to the privacy policy of the publisher.
    :vartype privacy_policy_link: str
    :ivar marketplace_terms_link: Link to HTML with Azure Marketplace terms.
    :vartype marketplace_terms_link: str
    :ivar retrieve_datetime: Date and time in UTC of when the terms were accepted. This is empty if
     Accepted is false.
    :vartype retrieve_datetime: str
    :ivar signature: Terms signature.
    :vartype signature: str
    :ivar accepted: If any version of the terms have been accepted, otherwise false.
    :vartype accepted: bool
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "publisher": {"key": "properties.publisher", "type": "str"},
        "product": {"key": "properties.product", "type": "str"},
        "plan": {"key": "properties.plan", "type": "str"},
        "license_text_link": {"key": "properties.licenseTextLink", "type": "str"},
        "privacy_policy_link": {"key": "properties.privacyPolicyLink", "type": "str"},
        "marketplace_terms_link": {"key": "properties.marketplaceTermsLink", "type": "str"},
        "retrieve_datetime": {"key": "properties.retrieveDatetime", "type": "str"},
        "signature": {"key": "properties.signature", "type": "str"},
        "accepted": {"key": "properties.accepted", "type": "bool"},
    }

    def __init__(
        self,
        *,
        publisher: Optional[str] = None,
        product: Optional[str] = None,
        plan: Optional[str] = None,
        license_text_link: Optional[str] = None,
        privacy_policy_link: Optional[str] = None,
        marketplace_terms_link: Optional[str] = None,
        retrieve_datetime: Optional[str] = None,
        signature: Optional[str] = None,
        accepted: Optional[bool] = None,
        **kwargs
    ):
        """
        :keyword publisher: Publisher identifier string of image being deployed.
        :paramtype publisher: str
        :keyword product: Offer identifier string of image being deployed.
        :paramtype product: str
        :keyword plan: Plan identifier string of image being deployed.
        :paramtype plan: str
        :keyword license_text_link: Link to HTML with Microsoft and Publisher terms.
        :paramtype license_text_link: str
        :keyword privacy_policy_link: Link to the privacy policy of the publisher.
        :paramtype privacy_policy_link: str
        :keyword marketplace_terms_link: Link to HTML with Azure Marketplace terms.
        :paramtype marketplace_terms_link: str
        :keyword retrieve_datetime: Date and time in UTC of when the terms were accepted. This is empty
         if Accepted is false.
        :paramtype retrieve_datetime: str
        :keyword signature: Terms signature.
        :paramtype signature: str
        :keyword accepted: If any version of the terms have been accepted, otherwise false.
        :paramtype accepted: bool
        """
        super().__init__(**kwargs)
        self.system_data = None
        self.publisher = publisher
        self.product = product
        self.plan = plan
        self.license_text_link = license_text_link
        self.privacy_policy_link = privacy_policy_link
        self.marketplace_terms_link = marketplace_terms_link
        self.retrieve_datetime = retrieve_datetime
        self.signature = signature
        self.accepted = accepted


class ErrorResponse(_serialization.Model):
    """Error response indicates Microsoft.MarketplaceOrdering service is not able to process the incoming request. The reason is provided in the error message.

    :ivar error: The details of the error.
    :vartype error: ~azure.mgmt.marketplaceordering.models.ErrorResponseError
    """

    _attribute_map = {
        "error": {"key": "error", "type": "ErrorResponseError"},
    }

    def __init__(self, *, error: Optional["_models.ErrorResponseError"] = None, **kwargs):
        """
        :keyword error: The details of the error.
        :paramtype error: ~azure.mgmt.marketplaceordering.models.ErrorResponseError
        """
        super().__init__(**kwargs)
        self.error = error


class ErrorResponseError(_serialization.Model):
    """The details of the error.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Error code.
    :vartype code: str
    :ivar message: Error message indicating why the operation failed.
    :vartype message: str
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)
        self.code = None
        self.message = None


class Operation(_serialization.Model):
    """Microsoft.MarketplaceOrdering REST API operation.

    :ivar name: Operation name: {provider}/{resource}/{operation}.
    :vartype name: str
    :ivar display: The object that represents the operation.
    :vartype display: ~azure.mgmt.marketplaceordering.models.OperationDisplay
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "display": {"key": "display", "type": "OperationDisplay"},
    }

    def __init__(self, *, name: Optional[str] = None, display: Optional["_models.OperationDisplay"] = None, **kwargs):
        """
        :keyword name: Operation name: {provider}/{resource}/{operation}.
        :paramtype name: str
        :keyword display: The object that represents the operation.
        :paramtype display: ~azure.mgmt.marketplaceordering.models.OperationDisplay
        """
        super().__init__(**kwargs)
        self.name = name
        self.display = display


class OperationDisplay(_serialization.Model):
    """The object that represents the operation.

    :ivar provider: Service provider: Microsoft.MarketplaceOrdering.
    :vartype provider: str
    :ivar resource: Resource on which the operation is performed: Agreement, virtualmachine, etc.
    :vartype resource: str
    :ivar operation: Operation type: Get Agreement, Sign Agreement, Cancel Agreement etc.
    :vartype operation: str
    :ivar description: Operation description.
    :vartype description: str
    """

    _attribute_map = {
        "provider": {"key": "provider", "type": "str"},
        "resource": {"key": "resource", "type": "str"},
        "operation": {"key": "operation", "type": "str"},
        "description": {"key": "description", "type": "str"},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword provider: Service provider: Microsoft.MarketplaceOrdering.
        :paramtype provider: str
        :keyword resource: Resource on which the operation is performed: Agreement, virtualmachine,
         etc.
        :paramtype resource: str
        :keyword operation: Operation type: Get Agreement, Sign Agreement, Cancel Agreement etc.
        :paramtype operation: str
        :keyword description: Operation description.
        :paramtype description: str
        """
        super().__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class OperationListResult(_serialization.Model):
    """Result of the request to list MarketplaceOrdering operations. It contains a list of operations and a URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of Microsoft.MarketplaceOrdering operations supported by the
     Microsoft.MarketplaceOrdering resource provider.
    :vartype value: list[~azure.mgmt.marketplaceordering.models.Operation]
    :ivar next_link: URL to get the next set of operation list results if there are any.
    :vartype next_link: str
    """

    _validation = {
        "next_link": {"readonly": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[Operation]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, *, value: Optional[List["_models.Operation"]] = None, **kwargs):
        """
        :keyword value: List of Microsoft.MarketplaceOrdering operations supported by the
         Microsoft.MarketplaceOrdering resource provider.
        :paramtype value: list[~azure.mgmt.marketplaceordering.models.Operation]
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = None


class SystemData(_serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or ~azure.mgmt.marketplaceordering.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or ~azure.mgmt.marketplaceordering.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        "created_by": {"key": "createdBy", "type": "str"},
        "created_by_type": {"key": "createdByType", "type": "str"},
        "created_at": {"key": "createdAt", "type": "iso-8601"},
        "last_modified_by": {"key": "lastModifiedBy", "type": "str"},
        "last_modified_by_type": {"key": "lastModifiedByType", "type": "str"},
        "last_modified_at": {"key": "lastModifiedAt", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        **kwargs
    ):
        """
        :keyword created_by: The identity that created the resource.
        :paramtype created_by: str
        :keyword created_by_type: The type of identity that created the resource. Known values are:
         "User", "Application", "ManagedIdentity", and "Key".
        :paramtype created_by_type: str or ~azure.mgmt.marketplaceordering.models.CreatedByType
        :keyword created_at: The timestamp of resource creation (UTC).
        :paramtype created_at: ~datetime.datetime
        :keyword last_modified_by: The identity that last modified the resource.
        :paramtype last_modified_by: str
        :keyword last_modified_by_type: The type of identity that last modified the resource. Known
         values are: "User", "Application", "ManagedIdentity", and "Key".
        :paramtype last_modified_by_type: str or ~azure.mgmt.marketplaceordering.models.CreatedByType
        :keyword last_modified_at: The timestamp of resource last modification (UTC).
        :paramtype last_modified_at: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at
