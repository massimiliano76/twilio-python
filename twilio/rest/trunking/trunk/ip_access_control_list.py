# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class IpAccessControlListList(ListResource):

    def __init__(self, domain, trunk_sid):
        super(IpAccessControlListList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'trunk_sid': trunk_sid,
        }
        self._uri = "/Trunks/{trunk_sid}/IpAccessControlLists".format(**self._instance_kwargs)

    def create(self, ip_access_control_list_sid):
        data = values.of({
            "IpAccessControlListSid": ip_access_control_list_sid,
        })
        
        return self._domain.create(
            IpAccessControlListInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._domain.read_limits(limit, page_size)
        
        params = values.of({})
        params.update(kwargs)
        
        return self._domain.read(
            self,
            IpAccessControlListInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, page_token=None, page=None, page_size=None, **kwargs):
        params = values.of({})
        params.update(kwargs)
        
        return self._domain.page(
            self,
            IpAccessControlListInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )


class IpAccessControlListContext(InstanceContext):

    def __init__(self, domain, trunk_sid, sid):
        super(IpAccessControlListContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'trunk_sid': trunk_sid,
            'sid': sid,
        }
        self._uri = "/Trunks/{trunk_sid}/IpAccessControlLists/{sid}".format(**self._instance_kwargs)

    def fetch(self):
        return self._domain.fetch(
            IpAccessControlListInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
        )

    def delete(self):
        return self._domain.delete("delete", self._uri)


class IpAccessControlListInstance(InstanceResource):

    def __init__(self, domain, payload, trunk_sid, sid=None):
        super(IpAccessControlListInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._sid = payload['sid']
        self._trunk_sid = payload['trunk_sid']
        self._friendly_name = payload['friendly_name']
        self._date_created = deserialize.iso8601_datetime(payload['date_created'])
        self._date_updated = deserialize.iso8601_datetime(payload['date_updated'])
        self._url = payload['url']
        
        # Context
        self._lazy_context = None
        self._context_trunk_sid = trunk_sid
        self._context_sid = sid or self._sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = IpAccessControlListContext(
                self._domain,
                self._context_trunk_sid,
                self._context_sid,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._account_sid

    @property
    def sid(self):
        """ The sid """
        return self._sid

    @property
    def trunk_sid(self):
        """ The trunk_sid """
        return self._trunk_sid

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._friendly_name

    @property
    def date_created(self):
        """ The date_created """
        return self._date_created

    @property
    def date_updated(self):
        """ The date_updated """
        return self._date_updated

    @property
    def url(self):
        """ The url """
        return self._url

    def fetch(self):
        self._context.fetch()

    def delete(self):
        self._context.delete()
