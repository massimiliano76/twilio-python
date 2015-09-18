# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest import serialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class SmsMessageList(ListResource):

    def __init__(self, domain, account_sid):
        super(SmsMessageList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
        }
        self._uri = "/Accounts/{account_sid}/SMS/Messages.json".format(**self._instance_kwargs)

    def create(self, to, from_, status_callback=values.unset,
               application_sid=values.unset, body=values.unset,
               media_url=values.unset):
        data = values.of({
            "To": to,
            "From": from_,
            "Body": body,
            "MediaUrl": media_url,
            "StatusCallback": status_callback,
            "ApplicationSid": application_sid,
        })
        
        return self._domain.create(
            SmsMessageInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def read(self, to=values.unset, from_=values.unset, date_sent=values.unset,
             limit=None, page_size=None, **kwargs):
        limits = self._domain.read_limits(limit, page_size)
        
        params = values.of({
            "To": to,
            "From": from_,
            "DateSent": serialize.iso8601_date(date_sent),
        })
        params.update(kwargs)
        
        return self._domain.read(
            self,
            SmsMessageInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, to=values.unset, from_=values.unset, date_sent=values.unset,
             page_token=None, page=None, page_size=None, **kwargs):
        params = values.of({
            "To": to,
            "From": from_,
        })
        params.update(kwargs)
        
        return self._domain.page(
            self,
            SmsMessageInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )


class SmsMessageContext(InstanceContext):

    def __init__(self, domain, account_sid, sid):
        super(SmsMessageContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = "/Accounts/{account_sid}/SMS/Messages/{sid}.json".format(**self._instance_kwargs)

    def delete(self):
        return self._domain.delete("delete", self._uri)

    def fetch(self):
        return self._domain.fetch(
            SmsMessageInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
        )

    def update(self, body=values.unset):
        data = values.of({
            "Body": body,
        })
        
        return self._domain.update(
            SmsMessageInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )


class SmsMessageInstance(InstanceResource):

    def __init__(self, domain, payload, account_sid, sid=None):
        super(SmsMessageInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._api_version = payload['api_version']
        self._body = payload['body']
        self._date_created = deserialize.iso8601_datetime(payload['date_created'])
        self._date_updated = deserialize.iso8601_datetime(payload['date_updated'])
        self._date_sent = deserialize.iso8601_datetime(payload['date_sent'])
        self._direction = payload['direction']
        self._error_code = payload['error_code']
        self._error_message = payload['error_message']
        self._from_ = payload['from_']
        self._num_media = payload['num_media']
        self._num_segments = payload['num_segments']
        self._price = payload['price']
        self._price_unit = payload['price_unit']
        self._sid = payload['sid']
        self._status = payload['status']
        self._subresource_uris = payload['subresource_uris']
        self._to = payload['to']
        self._uri = payload['uri']
        
        # Context
        self._lazy_context = None
        self._context_account_sid = account_sid
        self._context_sid = sid or self._sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = SmsMessageContext(
                self._domain,
                self._context_account_sid,
                self._context_sid,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._account_sid

    @property
    def api_version(self):
        """ The api_version """
        return self._api_version

    @property
    def body(self):
        """ The body """
        return self._body

    @property
    def date_created(self):
        """ The date_created """
        return self._date_created

    @property
    def date_updated(self):
        """ The date_updated """
        return self._date_updated

    @property
    def date_sent(self):
        """ The date_sent """
        return self._date_sent

    @property
    def direction(self):
        """ The direction """
        return self._direction

    @property
    def error_code(self):
        """ The error_code """
        return self._error_code

    @property
    def error_message(self):
        """ The error_message """
        return self._error_message

    @property
    def from_(self):
        """ The from """
        return self._from_

    @property
    def num_media(self):
        """ The num_media """
        return self._num_media

    @property
    def num_segments(self):
        """ The num_segments """
        return self._num_segments

    @property
    def price(self):
        """ The price """
        return self._price

    @property
    def price_unit(self):
        """ The price_unit """
        return self._price_unit

    @property
    def sid(self):
        """ The sid """
        return self._sid

    @property
    def status(self):
        """ The status """
        return self._status

    @property
    def subresource_uris(self):
        """ The subresource_uris """
        return self._subresource_uris

    @property
    def to(self):
        """ The to """
        return self._to

    @property
    def uri(self):
        """ The uri """
        return self._uri

    def delete(self):
        self._context.delete()

    def fetch(self):
        self._context.fetch()

    def update(self, body=values.unset):
        self._context.update(
            body=body,
        )
