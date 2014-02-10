# -*- coding: utf-8 -*-

import flask
from expects import expect

from ..helpers import failure


class TestHeader(object):
    def test_should_pass_if_actual_has_expected_header(self):
        expect(response=self.response).to.have.header('Content-Type')

    def test_should_pass_if_actual_has_expected_header_and_value(self):
        expect(response=self.response).to.have.header('Content-Type',
                                                      'application/json')

    def test_should_pass_if_actual_has_expected_header_in_lowercase(self):
        expect(response=self.response).to.have.header('content-type')

    def test_should_fail_if_actual_hasnt_expected_header(self):
        with failure():
            expect(response=self.response).to.have.header('Expires')

    def test_should_fail_if_actual_hasnt_expected_header_with_value(self):
        with failure():
            expect(response=self.response).to.have.header(
                'Expires', 'Thu, 01 Dec 1994 16:00:00 GMT')

    def test_should_fail_if_actual_has_expected_header_without_value(self):
        with failure():
            expect(response=self.response).to.have.header(
                'Content-Type', 'application/pdf')

    def setup(self):
        self.response = flask.Response(
            headers={'Content-Type': 'application/json'})


class TestNotHeader(object):
    def test_should_pass_if_actual_hasnt_expected_header(self):
        expect(response=self.response).not_to.have.header('Expires')

    def test_should_pass_if_actual_hasnt_expected_header_with_value(self):
        expect(response=self.response).not_to.have.header(
            'Expires', 'Thu, 01 Dec 1994 16:00:00 GMT')

    def test_should_pass_if_actual_has_expected_header_without_value(self):
        expect(response=self.response).not_to.have.header(
            'Content-Type', 'application/pdf')

    def test_should_fail_if_actual_has_expected_header(self):
        with failure():
            expect(response=self.response).not_to.have.header('Content-Type')

    def test_should_fail_if_actual_has_expected_header_and_value(self):
        with failure():
            expect(response=self.response).not_to.have.header(
                'Content-Type', 'application/json')

    def setup(self):
        self.response = flask.Response(
            headers={'Content-Type': 'application/json'})
