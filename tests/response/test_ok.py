# -*- coding: utf-8 -*-

import flask
from expects import expect

from ..helpers import failure


class TestOk(object):
    def test_should_pass_if_actual_has_200_status(self):
        expect(response=self.response(200)).to.be.ok

    def test_should_pass_if_actual_has_201_status(self):
        expect(response=self.response(201)).to.be.ok

    def test_should_pass_if_actual_has_302_status(self):
        expect(response=self.response(302)).to.be.ok

    def test_should_fail_if_actual_has_400_status(self):
        with failure():
            expect(response=self.response(400)).to.be.ok

    def test_should_fail_if_actual_has_500_status(self):
        with failure():
            expect(response=self.response(500)).to.be.ok

    def response(self, status):
        return flask.Response(status=status)


class TestNotOk(object):
    def test_should_pass_if_actual_has_400_status(self):
        expect(response=self.response(400)).not_to.be.ok

    def test_should_fail_if_actual_has_200_status(self):
        with failure():
            expect(response=self.response(200)).not_to.be.ok

    def test_should_fail_if_actual_has_302_status(self):
        with failure():
            expect(response=self.response(302)).not_to.be.ok

    def response(self, status):
        return flask.Response(status=status)
