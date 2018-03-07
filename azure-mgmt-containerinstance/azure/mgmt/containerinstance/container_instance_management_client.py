# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.container_groups_operations import ContainerGroupsOperations
from .operations.operations import Operations
from .operations.container_group_usage_operations import ContainerGroupUsageOperations
from .operations.async_container_group_operation_operations import AsyncContainerGroupOperationOperations
from .operations.container_logs_operations import ContainerLogsOperations
from .operations.start_container_operations import StartContainerOperations
from . import models


class ContainerInstanceManagementClientConfiguration(AzureConfiguration):
    """Configuration for ContainerInstanceManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(ContainerInstanceManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-containerinstance/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class ContainerInstanceManagementClient(object):
    """ContainerInstanceManagementClient

    :ivar config: Configuration for client.
    :vartype config: ContainerInstanceManagementClientConfiguration

    :ivar container_groups: ContainerGroups operations
    :vartype container_groups: azure.mgmt.containerinstance.operations.ContainerGroupsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.containerinstance.operations.Operations
    :ivar container_group_usage: ContainerGroupUsage operations
    :vartype container_group_usage: azure.mgmt.containerinstance.operations.ContainerGroupUsageOperations
    :ivar async_container_group_operation: AsyncContainerGroupOperation operations
    :vartype async_container_group_operation: azure.mgmt.containerinstance.operations.AsyncContainerGroupOperationOperations
    :ivar container_logs: ContainerLogs operations
    :vartype container_logs: azure.mgmt.containerinstance.operations.ContainerLogsOperations
    :ivar start_container: StartContainer operations
    :vartype start_container: azure.mgmt.containerinstance.operations.StartContainerOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = ContainerInstanceManagementClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-02-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.container_groups = ContainerGroupsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.container_group_usage = ContainerGroupUsageOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.async_container_group_operation = AsyncContainerGroupOperationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.container_logs = ContainerLogsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.start_container = StartContainerOperations(
            self._client, self.config, self._serialize, self._deserialize)
