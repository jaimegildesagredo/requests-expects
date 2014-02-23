# -*- coding: utf-8 -*-

import flask
from expects import expect
from expects.testing import failure

from ..constants import *


class TestHeaders(object):
    def test_should_pass_if_actual_has_headers_in_args(self):
        expect(response=self.response).to.have.headers(IRRELEVANT_HEADER_KEY1,
                                                       IRRELEVANT_HEADER_KEY2)

    def test_should_pass_if_actual_has_headers_in_kwargs(self):
        expect(response=self.response).to.have.headers(
            content_type=IRRELEVANT_HEADER_VALUE1,
            content_length=IRRELEVANT_HEADER_VALUE2)

    def test_should_pass_if_actual_has_headers_in_args_and_kwargs(self):
        expect(response=self.response).to.have.headers(
            IRRELEVANT_HEADER_KEY1, content_length=IRRELEVANT_HEADER_VALUE2)

    def test_should_pass_if_actual_has_headers_in_args_in_lowercase(self):
        expect(response=self.response).to.have.headers(
            IRRELEVANT_HEADER_KEY1.lower(), IRRELEVANT_HEADER_KEY2.lower())

    def test_should_fail_if_actual_hasnt_header_in_args(self):
        with failure(self.response,
                     'to have header {!r}'.format(IRRELEVANT_HEADER_KEY3)):

            expect(response=self.response).to.have.headers(
                IRRELEVANT_HEADER_KEY1, IRRELEVANT_HEADER_KEY3)

    def test_should_fail_if_actual_hasnt_header_in_kwargs(self):
        with failure(self.response, "to have header 'expires'"):
            expect(response=self.response).to.have.headers(
                content_type=IRRELEVANT_HEADER_VALUE1,
                expires=IRRELEVANT_HEADER_VALUE3)

    def test_should_fail_if_actual_has_header_without_value_in_kwargs(self):
        with failure(self.response,
                     "to have header 'content-length' with value '25'"):

            expect(response=self.response).to.have.headers(
                content_type=IRRELEVANT_HEADER_VALUE1,
                content_length='25')

    def setup(self):
        self.response = flask.Response(headers={
            IRRELEVANT_HEADER_KEY1: IRRELEVANT_HEADER_VALUE1,
            IRRELEVANT_HEADER_KEY2: IRRELEVANT_HEADER_VALUE2})


class TestNotHeaders(object):
    def test_should_pass_if_actual_hasnt_headers_in_args(self):
        expect(response=self.response).not_to.have.headers(
            IRRELEVANT_HEADER_KEY3, IRRELEVANT_HEADER_KEY4)

    def test_should_pass_if_actual_hasnt_headers_in_kwargs(self):
        expect(response=self.response).not_to.have.headers(
            etag=IRRELEVANT_HEADER_VALUE4,
            expires=IRRELEVANT_HEADER_VALUE3)

    def test_should_pass_if_actual_hasnt_headers_in_args_and_kwargs(self):
        expect(response=self.response).not_to.have.headers(
            IRRELEVANT_HEADER_KEY4, expires=IRRELEVANT_HEADER_VALUE3)

    def test_should_pass_if_actual_has_header_in_kwargs_without_value(self):
        expect(response=self.response).not_to.have.headers(
            content_type=IRRELEVANT_HEADER_VALUE2,
            expires=IRRELEVANT_HEADER_VALUE3)

    def test_should_fail_if_actual_has_header_in_args(self):
        with failure(self.response,
                     'not to have header {!r}'.format(IRRELEVANT_HEADER_KEY1)):

            expect(response=self.response).not_to.have.headers(
                IRRELEVANT_HEADER_KEY1, IRRELEVANT_HEADER_KEY2)

    def test_should_fail_if_actual_has_header_in_kwargs(self):
        with failure(self.response, "not to have header 'content-type'"):
            expect(response=self.response).not_to.have.headers(
                content_type=IRRELEVANT_HEADER_VALUE1)

    def setup(self):
        self.response = flask.Response(headers={
            IRRELEVANT_HEADER_KEY1: IRRELEVANT_HEADER_VALUE1,
            IRRELEVANT_HEADER_KEY2: IRRELEVANT_HEADER_VALUE2})
