# -*- coding: utf-8 -*-

import flask
from expects import expect

from ..helpers import failure


class TestStatus(object):
    def test_should_pass_if_actual_has_expected_status(self):
        expect(response=self.response_ok).to.have.status(200)

    def test_should_fail_if_actual_hasnt_expected_status(self):
        with failure():
            expect(response=self.response_ok).to.have.status(400)

    def setup(self):
        self.response_ok = flask.Response(status=200)


class TestNotStatus(object):
    def test_should_pass_if_actual_hasnt_expected_status(self):
        expect(response=self.response_ok).not_to.have.status(201)

    def test_should_fail_if_actual_has_expected_status(self):
        with failure():
            expect(response=self.response_ok).not_to.have.status(200)

    def setup(self):
        self.response_ok = flask.Response(status=200)
