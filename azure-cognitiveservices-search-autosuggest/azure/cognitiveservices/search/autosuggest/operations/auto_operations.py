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

from msrest.pipeline import ClientRawResponse

from .. import models


class AutoOperations(object):
    """AutoOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar x_bing_apis_sdk: Activate swagger compliance. Constant value: "true".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config
        self.x_bing_apis_sdk = "true"

    def suggest(
            self, query, accept_language=None, user_agent=None, client_id=None, client_ip=None, location=None, market=None, custom_headers=None, raw=False, **operation_config):
        """The Auto Suggest API lets you send a search query to Bing and get back
        a list of auto suggestions that are relevant to the search query. This
        section provides technical details about the query parameters and
        headers that you use to request news and the JSON response objects that
        contain them.

        :param query: The user's search query string. The query string cannot
         be empty. The query string may contain [Bing Advanced
         Operators](http://msdn.microsoft.com/library/ff795620.aspx). For
         example, to limit news to a specific domain, use the
         [site:](http://msdn.microsoft.com/library/ff795613.aspx) operator. Use
         this parameter only with the Auto Suggest API.
        :type query: str
        :param accept_language: A comma-delimited list of one or more
         languages to use for user interface strings. The list is in decreasing
         order of preference. For additional information, including expected
         format, see
         [RFC2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
         This header and the
         [setLang](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-autosuggest-api-v7-reference#setLang)
         query parameter are mutually exclusive; do not specify both. If you
         set this header, you must also specify the
         [cc](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-news-api-v7-reference#cc)
         query parameter. To determine the market to return results for, Bing
         uses the first supported language it finds from the list and combines
         it with the cc parameter value. If the list does not include a
         supported language, Bing finds the closest language and market that
         supports the request or it uses an aggregated or default market for
         the results. To determine the market that Bing used, see the
         BingAPIs-Market header. Use this header and the cc query parameter
         only if you specify multiple languages. Otherwise, use the
         [mkt](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-autosuggest-api-v7-reference#mkt)
         and
         [setLang](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-autosuggest-api-v7-reference#setLang)
         query parameters. A user interface string is a string that's used as a
         label in a user interface. There are few user interface strings in the
         JSON response objects. Any links to Bing.com properties in the
         response objects apply the specified language.
        :type accept_language: str
        :param user_agent: The user agent originating the request. Bing uses
         the user agent to provide mobile users with an optimized experience.
         Although optional, you are encouraged to always specify this header.
         The user-agent should be the same string that any commonly used
         browser sends. For information about user agents, see [RFC
         2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html). The
         following are examples of user-agent strings. Windows Phone:
         Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0;
         IEMobile/10.0; ARM; Touch; NOKIA; Lumia 822). Android: Mozilla / 5.0
         (Linux; U; Android 2.3.5; en - us; SCH - I500 Build / GINGERBREAD)
         AppleWebKit / 533.1 (KHTML; like Gecko) Version / 4.0 Mobile Safari /
         533.1. iPhone: Mozilla / 5.0 (iPhone; CPU iPhone OS 6_1 like Mac OS X)
         AppleWebKit / 536.26 (KHTML; like Gecko) Mobile / 10B142 iPhone4; 1
         BingWeb / 3.03.1428.20120423. PC: Mozilla / 5.0 (Windows NT 6.3;
         WOW64; Trident / 7.0; Touch; rv:11.0) like Gecko. iPad: Mozilla / 5.0
         (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit / 537.51.1 (KHTML, like
         Gecko) Version / 7.0 Mobile / 11A465 Safari / 9537.53
        :type user_agent: str
        :param client_id: Bing uses this header to provide users with
         consistent behavior across Bing API calls. Bing often flights new
         features and improvements, and it uses the client ID as a key for
         assigning traffic on different flights. If you do not use the same
         client ID for a user across multiple requests, then Bing may assign
         the user to multiple conflicting flights. Being assigned to multiple
         conflicting flights can lead to an inconsistent user experience. For
         example, if the second request has a different flight assignment than
         the first, the experience may be unexpected. Also, Bing can use the
         client ID to tailor web results to that client ID’s search history,
         providing a richer experience for the user. Bing also uses this header
         to help improve result rankings by analyzing the activity generated by
         a client ID. The relevance improvements help with better quality of
         results delivered by Bing APIs and in turn enables higher
         click-through rates for the API consumer. IMPORTANT: Although
         optional, you should consider this header required. Persisting the
         client ID across multiple requests for the same end user and device
         combination enables 1) the API consumer to receive a consistent user
         experience, and 2) higher click-through rates via better quality of
         results from the Bing APIs. Each user that uses your application on
         the device must have a unique, Bing generated client ID. If you do not
         include this header in the request, Bing generates an ID and returns
         it in the X-MSEdge-ClientID response header. The only time that you
         should NOT include this header in a request is the first time the user
         uses your app on that device. Use the client ID for each Bing API
         request that your app makes for this user on the device. Persist the
         client ID. To persist the ID in a browser app, use a persistent HTTP
         cookie to ensure the ID is used across all sessions. Do not use a
         session cookie. For other apps such as mobile apps, use the device's
         persistent storage to persist the ID. The next time the user uses your
         app on that device, get the client ID that you persisted. Bing
         responses may or may not include this header. If the response includes
         this header, capture the client ID and use it for all subsequent Bing
         requests for the user on that device. If you include the
         X-MSEdge-ClientID, you must not include cookies in the request.
        :type client_id: str
        :param client_ip: The IPv4 or IPv6 address of the client device. The
         IP address is used to discover the user's location. Bing uses the
         location information to determine safe search behavior. Although
         optional, you are encouraged to always specify this header and the
         X-Search-Location header. Do not obfuscate the address (for example,
         by changing the last octet to 0). Obfuscating the address results in
         the location not being anywhere near the device's actual location,
         which may result in Bing serving erroneous results.
        :type client_ip: str
        :param location: A semicolon-delimited list of key/value pairs that
         describe the client's geographical location. Bing uses the location
         information to determine safe search behavior and to return relevant
         local content. Specify the key/value pair as <key>:<value>. The
         following are the keys that you use to specify the user's location.
         lat (required): The latitude of the client's location, in degrees. The
         latitude must be greater than or equal to -90.0 and less than or equal
         to +90.0. Negative values indicate southern latitudes and positive
         values indicate northern latitudes. long (required): The longitude of
         the client's location, in degrees. The longitude must be greater than
         or equal to -180.0 and less than or equal to +180.0. Negative values
         indicate western longitudes and positive values indicate eastern
         longitudes. re (required): The radius, in meters, which specifies the
         horizontal accuracy of the coordinates. Pass the value returned by the
         device's location service. Typical values might be 22m for GPS/Wi-Fi,
         380m for cell tower triangulation, and 18,000m for reverse IP lookup.
         ts (optional): The UTC UNIX timestamp of when the client was at the
         location. (The UNIX timestamp is the number of seconds since January
         1, 1970.) head (optional): The client's relative heading or direction
         of travel. Specify the direction of travel as degrees from 0 through
         360, counting clockwise relative to true north. Specify this key only
         if the sp key is nonzero. sp (optional): The horizontal velocity
         (speed), in meters per second, that the client device is traveling.
         alt (optional): The altitude of the client device, in meters. are
         (optional): The radius, in meters, that specifies the vertical
         accuracy of the coordinates. Specify this key only if you specify the
         alt key. Although many of the keys are optional, the more information
         that you provide, the more accurate the location results are. Although
         optional, you are encouraged to always specify the user's geographical
         location. Providing the location is especially important if the
         client's IP address does not accurately reflect the user's physical
         location (for example, if the client uses VPN). For optimal results,
         you should include this header and the X-MSEdge-ClientIP header, but
         at a minimum, you should include this header.
        :type location: str
        :param market: The market where the results come from. Typically, mkt
         is the country where the user is making the request from. However, it
         could be a different country if the user is not located in a country
         where Bing delivers results. The market must be in the form <language
         code>-<country code>. For example, en-US. The string is case
         insensitive. For a list of possible market values, see [Market
         Codes](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-autosuggest-api-v7-reference#market-codes).
         NOTE: If known, you are encouraged to always specify the market.
         Specifying the market helps Bing route the request and return an
         appropriate and optimal response. If you specify a market that is not
         listed in [Market
         Codes](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-autosuggest-api-v7-reference#market-codes),
         Bing uses a best fit market code based on an internal mapping that is
         subject to change. This parameter and the
         [cc](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-autosuggest-api-v7-reference#cc)
         query parameter are mutually exclusive—do not specify both.
        :type market: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SuggestionGroup or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.search.autosuggest.models.SuggestionGroup or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.cognitiveservices.search.autosuggest.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.suggest.metadata['url']

        # Construct parameters
        query_parameters = {}
        if market is not None:
            query_parameters['mkt'] = self._serialize.query("market", market, 'str')
        query_parameters['q'] = self._serialize.query("query", query, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['X-BingApis-SDK'] = self._serialize.header("self.x_bing_apis_sdk", self.x_bing_apis_sdk, 'str')
        if accept_language is not None:
            header_parameters['Accept-Language'] = self._serialize.header("accept_language", accept_language, 'str')
        if user_agent is not None:
            header_parameters['User-Agent'] = self._serialize.header("user_agent", user_agent, 'str')
        if client_id is not None:
            header_parameters['X-MSEdge-ClientID'] = self._serialize.header("client_id", client_id, 'str')
        if client_ip is not None:
            header_parameters['X-MSEdge-ClientIP'] = self._serialize.header("client_ip", client_ip, 'str')
        if location is not None:
            header_parameters['X-Search-Location'] = self._serialize.header("location", location, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SuggestionGroup', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    suggest.metadata = {'url': '/suggestions'}