# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, List, Optional, TYPE_CHECKING

from .. import _serialization

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class ErrorDetails(_serialization.Model):
    """Error details.

    :ivar code: Error code identifying the specific error.
    :vartype code: str
    :ivar message: A human-readable error message.
    :vartype message: str
    """

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, code: Optional[str] = None, message: Optional[str] = None, **kwargs):
        """
        :keyword code: Error code identifying the specific error.
        :paramtype code: str
        :keyword message: A human-readable error message.
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message


class ErrorResponse(_serialization.Model):
    """Error response.

    :ivar error: Error info.
    :vartype error: ~azure.mgmt.workloadmonitor.models.ErrorResponseError
    """

    _attribute_map = {
        "error": {"key": "error", "type": "ErrorResponseError"},
    }

    def __init__(self, *, error: Optional["_models.ErrorResponseError"] = None, **kwargs):
        """
        :keyword error: Error info.
        :paramtype error: ~azure.mgmt.workloadmonitor.models.ErrorResponseError
        """
        super().__init__(**kwargs)
        self.error = error


class ErrorResponseError(_serialization.Model):
    """Error info.

    :ivar code: Service-defined error code. This code serves as a sub-status for the HTTP error
     code specified in the response.
    :vartype code: str
    :ivar message: Human-readable representation of the error.
    :vartype message: str
    :ivar details: Error details.
    :vartype details: list[~azure.mgmt.workloadmonitor.models.ErrorDetails]
    """

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "details": {"key": "details", "type": "[ErrorDetails]"},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        details: Optional[List["_models.ErrorDetails"]] = None,
        **kwargs
    ):
        """
        :keyword code: Service-defined error code. This code serves as a sub-status for the HTTP error
         code specified in the response.
        :paramtype code: str
        :keyword message: Human-readable representation of the error.
        :paramtype message: str
        :keyword details: Error details.
        :paramtype details: list[~azure.mgmt.workloadmonitor.models.ErrorDetails]
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message
        self.details = details


class Resource(_serialization.Model):
    """The resource model definition for the ARM proxy resource, 'microsoft.workloadmonitor/monitors'.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The resource Id.
    :vartype id: str
    :ivar name: The resource name.
    :vartype name: str
    :ivar type: The resource type.
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


class HealthMonitor(Resource):  # pylint: disable=too-many-instance-attributes
    """Information about the monitor’s current health status.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The resource Id.
    :vartype id: str
    :ivar name: The resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :ivar monitor_name: Human-readable name of the monitor.
    :vartype monitor_name: str
    :ivar monitor_type: Type of the monitor.
    :vartype monitor_type: str
    :ivar monitored_object: Dynamic monitored object of the monitor.
    :vartype monitored_object: str
    :ivar parent_monitor_name: Name of the parent monitor.
    :vartype parent_monitor_name: str
    :ivar previous_monitor_state: Previous health state of the monitor. Known values are:
     "Healthy", "Critical", "Warning", "Unknown", "Disabled", and "None".
    :vartype previous_monitor_state: str or ~azure.mgmt.workloadmonitor.models.HealthState
    :ivar current_monitor_state: Current health state of the monitor. Known values are: "Healthy",
     "Critical", "Warning", "Unknown", "Disabled", and "None".
    :vartype current_monitor_state: str or ~azure.mgmt.workloadmonitor.models.HealthState
    :ivar evaluation_timestamp: Timestamp of the monitor's last health evaluation.
    :vartype evaluation_timestamp: str
    :ivar current_state_first_observed_timestamp: Timestamp of the monitor's last health state
     change.
    :vartype current_state_first_observed_timestamp: str
    :ivar last_reported_timestamp: Timestamp of the monitor's last reported health state.
    :vartype last_reported_timestamp: str
    :ivar evidence: Evidence validating the monitor's current health state.
    :vartype evidence: JSON
    :ivar monitor_configuration: The configuration settings at the time of the monitor's health
     evaluation.
    :vartype monitor_configuration: JSON
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "previous_monitor_state": {"readonly": True},
        "current_monitor_state": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "monitor_name": {"key": "properties.monitorName", "type": "str"},
        "monitor_type": {"key": "properties.monitorType", "type": "str"},
        "monitored_object": {"key": "properties.monitoredObject", "type": "str"},
        "parent_monitor_name": {"key": "properties.parentMonitorName", "type": "str"},
        "previous_monitor_state": {"key": "properties.previousMonitorState", "type": "str"},
        "current_monitor_state": {"key": "properties.currentMonitorState", "type": "str"},
        "evaluation_timestamp": {"key": "properties.evaluationTimestamp", "type": "str"},
        "current_state_first_observed_timestamp": {
            "key": "properties.currentStateFirstObservedTimestamp",
            "type": "str",
        },
        "last_reported_timestamp": {"key": "properties.lastReportedTimestamp", "type": "str"},
        "evidence": {"key": "properties.evidence", "type": "object"},
        "monitor_configuration": {"key": "properties.monitorConfiguration", "type": "object"},
    }

    def __init__(
        self,
        *,
        monitor_name: Optional[str] = None,
        monitor_type: Optional[str] = None,
        monitored_object: Optional[str] = None,
        parent_monitor_name: Optional[str] = None,
        evaluation_timestamp: Optional[str] = None,
        current_state_first_observed_timestamp: Optional[str] = None,
        last_reported_timestamp: Optional[str] = None,
        evidence: Optional[JSON] = None,
        monitor_configuration: Optional[JSON] = None,
        **kwargs
    ):
        """
        :keyword monitor_name: Human-readable name of the monitor.
        :paramtype monitor_name: str
        :keyword monitor_type: Type of the monitor.
        :paramtype monitor_type: str
        :keyword monitored_object: Dynamic monitored object of the monitor.
        :paramtype monitored_object: str
        :keyword parent_monitor_name: Name of the parent monitor.
        :paramtype parent_monitor_name: str
        :keyword evaluation_timestamp: Timestamp of the monitor's last health evaluation.
        :paramtype evaluation_timestamp: str
        :keyword current_state_first_observed_timestamp: Timestamp of the monitor's last health state
         change.
        :paramtype current_state_first_observed_timestamp: str
        :keyword last_reported_timestamp: Timestamp of the monitor's last reported health state.
        :paramtype last_reported_timestamp: str
        :keyword evidence: Evidence validating the monitor's current health state.
        :paramtype evidence: JSON
        :keyword monitor_configuration: The configuration settings at the time of the monitor's health
         evaluation.
        :paramtype monitor_configuration: JSON
        """
        super().__init__(**kwargs)
        self.monitor_name = monitor_name
        self.monitor_type = monitor_type
        self.monitored_object = monitored_object
        self.parent_monitor_name = parent_monitor_name
        self.previous_monitor_state = None
        self.current_monitor_state = None
        self.evaluation_timestamp = evaluation_timestamp
        self.current_state_first_observed_timestamp = current_state_first_observed_timestamp
        self.last_reported_timestamp = last_reported_timestamp
        self.evidence = evidence
        self.monitor_configuration = monitor_configuration


class HealthMonitorList(_serialization.Model):
    """Information about the current health statuses of the monitors.

    :ivar value: Array of health monitors of the virtual machine.
    :vartype value: list[~azure.mgmt.workloadmonitor.models.HealthMonitor]
    :ivar next_link: Link to next page if the list is too long.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[HealthMonitor]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: Optional[List["_models.HealthMonitor"]] = None, next_link: Optional[str] = None, **kwargs
    ):
        """
        :keyword value: Array of health monitors of the virtual machine.
        :paramtype value: list[~azure.mgmt.workloadmonitor.models.HealthMonitor]
        :keyword next_link: Link to next page if the list is too long.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class HealthMonitorStateChange(Resource):  # pylint: disable=too-many-instance-attributes
    """Information about the monitor’s health state change at the provided timestamp.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The resource Id.
    :vartype id: str
    :ivar name: The resource name.
    :vartype name: str
    :ivar type: The resource type.
    :vartype type: str
    :ivar monitor_name: Human-readable name of the monitor.
    :vartype monitor_name: str
    :ivar monitor_type: Type of the monitor.
    :vartype monitor_type: str
    :ivar monitored_object: Dynamic monitored object of the monitor.
    :vartype monitored_object: str
    :ivar evaluation_timestamp: Timestamp of the monitor's last health evaluation.
    :vartype evaluation_timestamp: str
    :ivar current_state_first_observed_timestamp: Timestamp of the monitor's last health state
     change.
    :vartype current_state_first_observed_timestamp: str
    :ivar previous_monitor_state: Previous health state of the monitor. Known values are:
     "Healthy", "Critical", "Warning", "Unknown", "Disabled", and "None".
    :vartype previous_monitor_state: str or ~azure.mgmt.workloadmonitor.models.HealthState
    :ivar current_monitor_state: Current health state of the monitor. Known values are: "Healthy",
     "Critical", "Warning", "Unknown", "Disabled", and "None".
    :vartype current_monitor_state: str or ~azure.mgmt.workloadmonitor.models.HealthState
    :ivar evidence: Evidence validating the monitor's current health state.
    :vartype evidence: JSON
    :ivar monitor_configuration: The configuration settings at the time of the monitor's health
     evaluation.
    :vartype monitor_configuration: JSON
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "previous_monitor_state": {"readonly": True},
        "current_monitor_state": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "monitor_name": {"key": "properties.monitorName", "type": "str"},
        "monitor_type": {"key": "properties.monitorType", "type": "str"},
        "monitored_object": {"key": "properties.monitoredObject", "type": "str"},
        "evaluation_timestamp": {"key": "properties.evaluationTimestamp", "type": "str"},
        "current_state_first_observed_timestamp": {
            "key": "properties.currentStateFirstObservedTimestamp",
            "type": "str",
        },
        "previous_monitor_state": {"key": "properties.previousMonitorState", "type": "str"},
        "current_monitor_state": {"key": "properties.currentMonitorState", "type": "str"},
        "evidence": {"key": "properties.evidence", "type": "object"},
        "monitor_configuration": {"key": "properties.monitorConfiguration", "type": "object"},
    }

    def __init__(
        self,
        *,
        monitor_name: Optional[str] = None,
        monitor_type: Optional[str] = None,
        monitored_object: Optional[str] = None,
        evaluation_timestamp: Optional[str] = None,
        current_state_first_observed_timestamp: Optional[str] = None,
        evidence: Optional[JSON] = None,
        monitor_configuration: Optional[JSON] = None,
        **kwargs
    ):
        """
        :keyword monitor_name: Human-readable name of the monitor.
        :paramtype monitor_name: str
        :keyword monitor_type: Type of the monitor.
        :paramtype monitor_type: str
        :keyword monitored_object: Dynamic monitored object of the monitor.
        :paramtype monitored_object: str
        :keyword evaluation_timestamp: Timestamp of the monitor's last health evaluation.
        :paramtype evaluation_timestamp: str
        :keyword current_state_first_observed_timestamp: Timestamp of the monitor's last health state
         change.
        :paramtype current_state_first_observed_timestamp: str
        :keyword evidence: Evidence validating the monitor's current health state.
        :paramtype evidence: JSON
        :keyword monitor_configuration: The configuration settings at the time of the monitor's health
         evaluation.
        :paramtype monitor_configuration: JSON
        """
        super().__init__(**kwargs)
        self.monitor_name = monitor_name
        self.monitor_type = monitor_type
        self.monitored_object = monitored_object
        self.evaluation_timestamp = evaluation_timestamp
        self.current_state_first_observed_timestamp = current_state_first_observed_timestamp
        self.previous_monitor_state = None
        self.current_monitor_state = None
        self.evidence = evidence
        self.monitor_configuration = monitor_configuration


class HealthMonitorStateChangeList(_serialization.Model):
    """Information about the health state changes of the monitor within the provided time window.

    :ivar value: Array of health state changes within the specified time window.
    :vartype value: list[~azure.mgmt.workloadmonitor.models.HealthMonitorStateChange]
    :ivar next_link: Link to next page if the list is too long.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[HealthMonitorStateChange]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self,
        *,
        value: Optional[List["_models.HealthMonitorStateChange"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword value: Array of health state changes within the specified time window.
        :paramtype value: list[~azure.mgmt.workloadmonitor.models.HealthMonitorStateChange]
        :keyword next_link: Link to next page if the list is too long.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class Operation(_serialization.Model):
    """Operation supported by the resource provider.

    All required parameters must be populated in order to send to Azure.

    :ivar name: The name of the operation being performed on this particular object. Required.
    :vartype name: str
    :ivar display: The localized display information for this particular operation or action.
     Required.
    :vartype display: ~azure.mgmt.workloadmonitor.models.OperationDisplay
    :ivar origin: The intended executor of the operation. Required.
    :vartype origin: str
    """

    _validation = {
        "name": {"required": True},
        "display": {"required": True},
        "origin": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "display": {"key": "display", "type": "OperationDisplay"},
        "origin": {"key": "origin", "type": "str"},
    }

    def __init__(self, *, name: str, display: "_models.OperationDisplay", origin: str, **kwargs):
        """
        :keyword name: The name of the operation being performed on this particular object. Required.
        :paramtype name: str
        :keyword display: The localized display information for this particular operation or action.
         Required.
        :paramtype display: ~azure.mgmt.workloadmonitor.models.OperationDisplay
        :keyword origin: The intended executor of the operation. Required.
        :paramtype origin: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.display = display
        self.origin = origin


class OperationDisplay(_serialization.Model):
    """The localized display information for this particular operation or action.

    All required parameters must be populated in order to send to Azure.

    :ivar provider: Operation resource provider name. Required.
    :vartype provider: str
    :ivar resource: Resource on which the operation is performed. Required.
    :vartype resource: str
    :ivar operation: Human-readable, friendly name for the operation. Required.
    :vartype operation: str
    :ivar description: Operation description. Required.
    :vartype description: str
    """

    _validation = {
        "provider": {"required": True},
        "resource": {"required": True},
        "operation": {"required": True},
        "description": {"required": True},
    }

    _attribute_map = {
        "provider": {"key": "provider", "type": "str"},
        "resource": {"key": "resource", "type": "str"},
        "operation": {"key": "operation", "type": "str"},
        "description": {"key": "description", "type": "str"},
    }

    def __init__(self, *, provider: str, resource: str, operation: str, description: str, **kwargs):
        """
        :keyword provider: Operation resource provider name. Required.
        :paramtype provider: str
        :keyword resource: Resource on which the operation is performed. Required.
        :paramtype resource: str
        :keyword operation: Human-readable, friendly name for the operation. Required.
        :paramtype operation: str
        :keyword description: Operation description. Required.
        :paramtype description: str
        """
        super().__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class OperationList(_serialization.Model):
    """List of available REST API operations.

    :ivar value: Array of available REST API operations.
    :vartype value: list[~azure.mgmt.workloadmonitor.models.Operation]
    :ivar next_link: Link to next page if the list is too long.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[Operation]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, *, value: Optional[List["_models.Operation"]] = None, next_link: Optional[str] = None, **kwargs):
        """
        :keyword value: Array of available REST API operations.
        :paramtype value: list[~azure.mgmt.workloadmonitor.models.Operation]
        :keyword next_link: Link to next page if the list is too long.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link
