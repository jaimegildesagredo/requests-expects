# -*- coding: utf-8 -*-

import flask
from expects import expect
from expects.testing import failure

from ..constants import *


class TestHeader(object):
    def test_should_pass_if_actual_has_expected_header(self):
        expect(response=self.response).to.have.header(IRRELEVANT_HEADER_KEY1)

    def test_should_pass_if_actual_has_expected_header_and_value(self):
        expect(response=self.response).to.have.header(IRRELEVANT_HEADER_KEY1,
                                                      IRRELEVANT_HEADER_VALUE1)

    def test_should_pass_if_actual_has_expected_header_in_lowercase(self):
        expect(response=self.response).to.have.header(IRRELEVANT_HEADER_KEY1.lower())

    def test_should_fail_if_actual_hasnt_expected_header(self):
        with failure(self.response,
                     'to have header {!r}'.format(IRRELEVANT_HEADER_KEY2)):

            expect(response=self.response).to.have.header(IRRELEVANT_HEADER_KEY2)

    def test_should_fail_if_actual_hasnt_expected_header_with_value(self):
        with failure(self.response,
                     'to have header {!r}'.format(IRRELEVANT_HEADER_KEY2)):

            expect(response=self.response).to.have.header(
                IRRELEVANT_HEADER_KEY2, IRRELEVANT_HEADER_VALUE2)

    def test_should_fail_if_actual_has_expected_header_without_value(self):
        with failure(self.response,
            'to have header {!r} with value {!r} but was'.format(
                IRRELEVANT_HEADER_KEY1, IRRELEVANT_HEADER_VALUE3)):

            expect(response=self.response).to.have.header(
                IRRELEVANT_HEADER_KEY1, IRRELEVANT_HEADER_VALUE3)

    def setup(self):
        self.response = flask.Response(
            headers={IRRELEVANT_HEADER_KEY1: IRRELEVANT_HEADER_VALUE1})


class TestNotHeader(object):
    def test_should_pass_if_actual_hasnt_expected_header(self):
        expect(response=self.response).not_to.have.header(IRRELEVANT_HEADER_KEY2)

    def test_should_pass_if_actual_hasnt_expected_header_with_value(self):
        expect(response=self.response).not_to.have.header(
            IRRELEVANT_HEADER_KEY2, IRRELEVANT_HEADER_VALUE2)

    def test_should_pass_if_actual_has_expected_header_without_value(self):
        expect(response=self.response).not_to.have.header(
            IRRELEVANT_HEADER_KEY1, IRRELEVANT_HEADER_VALUE3)

    def test_should_fail_if_actual_has_expected_header(self):
        with failure(self.response,
                     'not to have header {!r}'.format(IRRELEVANT_HEADER_KEY1)):

            expect(response=self.response).not_to.have.header(IRRELEVANT_HEADER_KEY1)

    def test_should_fail_if_actual_has_expected_header_and_value(self):
        with failure(self.response,
                     'not to have header {!r} with value {!r}'.format(
                         IRRELEVANT_HEADER_KEY1, IRRELEVANT_HEADER_VALUE1)):

            expect(response=self.response).not_to.have.header(
                IRRELEVANT_HEADER_KEY1, IRRELEVANT_HEADER_VALUE1)

    def setup(self):
        self.response = flask.Response(
            headers={IRRELEVANT_HEADER_KEY1: IRRELEVANT_HEADER_VALUE1})
