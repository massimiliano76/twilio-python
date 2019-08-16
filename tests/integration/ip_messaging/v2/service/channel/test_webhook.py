# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class WebhookTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                       .channels(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                       .webhooks.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://chat.twilio.com/v2/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Channels/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Webhooks',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 5,
                    "first_page_url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks?PageSize=5&Page=0",
                    "previous_page_url": null,
                    "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks?PageSize=5&Page=0",
                    "next_page_url": null,
                    "key": "webhooks"
                },
                "webhooks": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "channel_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "type": "webhook",
                        "configuration": {
                            "url": "dummy",
                            "method": "GET",
                            "filters": [
                                "onMessageSent",
                                "onChannelDestroyed"
                            ],
                            "retry_count": 2
                        },
                        "date_created": "2016-03-24T21:05:50Z",
                        "date_updated": "2016-03-24T21:05:50Z",
                        "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "channel_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "type": "trigger",
                        "configuration": {
                            "url": "dummy",
                            "method": "POST",
                            "filters": [
                                "keyword1",
                                "keyword2"
                            ],
                            "retry_count": 3
                        },
                        "date_created": "2016-03-24T21:05:50Z",
                        "date_updated": "2016-03-24T21:05:50Z",
                        "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    },
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "channel_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "type": "studio",
                        "configuration": {
                            "flow_sid": "FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                        },
                        "date_created": "2016-03-24T21:05:50Z",
                        "date_updated": "2016-03-24T21:05:50Z",
                        "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))

        actual = self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .channels(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .webhooks.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 5,
                    "first_page_url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks?PageSize=5&Page=0",
                    "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks?PageSize=5&Page=0",
                    "previous_page_url": null,
                    "next_page_url": null,
                    "key": "webhooks"
                },
                "webhooks": []
            }
            '''
        ))

        actual = self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .channels(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .webhooks.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                       .channels(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                       .webhooks(sid="WHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://chat.twilio.com/v2/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Channels/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Webhooks/WHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "channel_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "type": "studio",
                "configuration": {
                    "flow_sid": "FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                },
                "date_created": "2016-03-24T21:05:50Z",
                "date_updated": "2016-03-24T21:05:50Z",
                "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .channels(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .webhooks(sid="WHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                       .channels(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                       .webhooks.create(type="webhook")

        values = {'Type': "webhook", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://chat.twilio.com/v2/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Channels/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Webhooks',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "channel_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "type": "webhook",
                "configuration": {
                    "url": "dummy",
                    "method": "GET",
                    "filters": [
                        "onMessageSent",
                        "onChannelDestroyed"
                    ],
                    "retry_count": 2
                },
                "date_created": "2016-03-24T21:05:50Z",
                "date_updated": "2016-03-24T21:05:50Z",
                "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .channels(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .webhooks.create(type="webhook")

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                       .channels(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                       .webhooks(sid="WHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://chat.twilio.com/v2/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Channels/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Webhooks/WHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "channel_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "type": "trigger",
                "configuration": {
                    "url": "dummy",
                    "method": "POST",
                    "filters": [
                        "keyword1",
                        "keyword2"
                    ],
                    "retry_count": 3
                },
                "date_created": "2016-03-24T21:05:50Z",
                "date_updated": "2016-03-24T21:05:51Z",
                "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .channels(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .webhooks(sid="WHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                       .channels(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                       .webhooks(sid="WHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://chat.twilio.com/v2/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Channels/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Webhooks/WHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .channels(sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .webhooks(sid="WHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)
