# -*- coding: utf-8 -*-

from expects.expectation import Expectation


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
        # FIXME(jaimegildesagredo): This code is basically equivalent to:
        #                           expect(self._actual.headers).to.have.key(*args)

        expected_name = args[0]

        try:
            expected_value = args[1]
        except IndexError:
            pass
        else:
            try:
                value = self._actual.headers[expected_name]
            except KeyError:
                pass
            else:
                self._assert(value == expected_value,
                             '{!r} with value {!r} but was {!r}'.format(
                                 expected_name, expected_value, value))

                return

        self._assert(expected_name in self._actual.headers, expected_name)

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
