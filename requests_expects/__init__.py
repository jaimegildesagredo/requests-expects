# -*- coding: utf-8 -*-

from expects.expectation import Expectation
from expects import matchers


class Response(Expectation):
    @property
    def to(self):
        return self

    @property
    def have(self):
        return self

    @property
    def be(self):
        return self

    def status(self, expected):
        self._assert(self._actual.status_code == expected, expected)

    def header(self, *args):
        self._assert(*matchers.key(self._actual.headers, *args))

    def headers(self, *args, **kwargs):
        # FIXME(jaimegildesagredo): This code is basically equivalent to:
        #                           expect(self._actual.headers).to.have.keys(*args, **kwargs)

        self._message.pop()

        has_header = self.header

        try:
            kwargs = dict(*args, **kwargs)
        except (TypeError, ValueError):
            for name in args:
                has_header(name)
        finally:
            for name, value in kwargs.items():
                name = name.replace('_', '-')
                has_header(name, value)

    @property
    def ok(self):
        self._assert(self._actual.status_code < 400)

    @property
    def json(self):
        self._assert('application/json' in self._actual.headers['Content-Type'])

    @property
    def xml(self):
        content_type = self._actual.headers['Content-Type']

        self._assert('text/xml' in content_type or
                     'application/xml' in content_type)

    @property
    def html(self):
        self._assert('text/html' in self._actual.headers['Content-Type'])
