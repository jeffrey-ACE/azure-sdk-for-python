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

try:
    from .query_py3 import Query
    from .response_py3 import Response
    from .query_context_py3 import QueryContext
    from .suggestions_py3 import Suggestions
    from .suggestion_group_py3 import SuggestionGroup
    from .identifiable_py3 import Identifiable
    from .error_py3 import Error
    from .error_response_py3 import ErrorResponse, ErrorResponseException
    from .response_base_py3 import ResponseBase
except (SyntaxError, ImportError):
    from .query import Query
    from .response import Response
    from .query_context import QueryContext
    from .suggestions import Suggestions
    from .suggestion_group import SuggestionGroup
    from .identifiable import Identifiable
    from .error import Error
    from .error_response import ErrorResponse, ErrorResponseException
    from .response_base import ResponseBase
from .auto_suggest_api_enums import (
    ErrorCode,
    ErrorSubCode,
)

__all__ = [
    'Query',
    'Response',
    'QueryContext',
    'Suggestions',
    'SuggestionGroup',
    'Identifiable',
    'Error',
    'ErrorResponse', 'ErrorResponseException',
    'ResponseBase',
    'ErrorCode',
    'ErrorSubCode',
]