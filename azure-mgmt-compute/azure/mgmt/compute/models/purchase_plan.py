# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PurchasePlan(Model):
    """
    Used for establishing the purchase context of any 3rd Party artifact
    through MarketPlace.

    :param str publisher: Gets or sets the publisher ID.
    :param str name: Gets or sets the plan ID.
    :param str product: Gets or sets the product ID.
    """ 

    _validation = {
        'publisher': {'required': True},
        'name': {'required': True},
        'product': {'required': True},
    }

    _attribute_map = {
        'publisher': {'key': 'publisher', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'product': {'key': 'product', 'type': 'str'},
    }

    def __init__(self, publisher, name, product, **kwargs):
        self.publisher = publisher
        self.name = name
        self.product = product