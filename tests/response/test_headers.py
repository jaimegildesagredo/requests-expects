# -*- coding: utf-8 -*-

import flask
from expects import expect

from ..helpers import failure


class TestHeaders(object):
    def test_should_pass_if_actual_has_headers_in_args(self):
        expect(response=self.response).to.have.headers('Content-Type',
                                                       'Content-Length')

    def test_should_pass_if_actual_has_headers_in_kwargs(self):
        expect(response=self.response).to.have.headers(
            content_type='application/json', content_length='10')

    def test_should_pass_if_actual_has_headers_in_args_and_kwargs(self):
        expect(response=self.response).to.have.headers('content-type',
                                                       content_length='10')

    def test_should_pass_if_actual_has_headers_in_args_in_lowercase(self):
        expect(response=self.response).to.have.headers('content-type',
                                                       'content-length')

    def test_should_fail_if_actual_hasnt_header_in_args(self):
        with failure():
            expect(response=self.response).to.have.headers('Content-Type',
                                                           'Expires')

    def test_should_fail_if_actual_hasnt_header_in_kwargs(self):
        with failure():
            expect(response=self.response).to.have.headers(
                content_type='application/json',
                expires='Thu, 01 Dec 1994 16:00:00 GMT')

    def test_should_fail_if_actual_has_header_without_value_in_kwargs(self):
        with failure():
            expect(response=self.response).to.have.headers(
                content_type='application/json', content_length='25')

    def setup(self):
        self.response = flask.Response(headers={
            'Content-Type': 'application/json', 'Content-Length': '10'})


class TestNotHeaders(object):
    def test_should_pass_if_actual_hasnt_headers_in_args(self):
        expect(response=self.response).not_to.have.headers('ETag', 'Expires')

    def test_should_pass_if_actual_hasnt_headers_in_kwargs(self):
        expect(response=self.response).not_to.have.headers(
            etag='a79cf83e92c3d16b8e5f9a8f7e66c674',
            expires='Thu, 01 Dec 1994 16:00:00 GMT')

    def test_should_pass_if_actual_hasnt_headers_in_args_and_kwargs(self):
        expect(response=self.response).not_to.have.headers(
            'etag', expires='Thu, 01 Dec 1994 16:00:00 GMT')

    def test_should_pass_if_actual_has_header_in_kwargs_without_value(self):
        expect(response=self.response).not_to.have.headers(
            content_type='application/pdf',
            expires='Thu, 01 Dec 1994 16:00:00 GMT')

    def test_should_fail_if_actual_has_header_in_args(self):
        with failure():
            expect(response=self.response).not_to.have.headers(
                'Content-Type', 'Content-Length')

    def test_should_fail_if_actual_has_header_in_kwargs(self):
        with failure():
            expect(response=self.response).not_to.have.headers(
                content_type='application/json', content_length='10')

    def setup(self):
        self.response = flask.Response(headers={
            'Content-Type': 'application/json', 'Content-Length': '10'})
