# -*- coding: utf-8 -*-

import flask
from expects import expect
from expects.testing import failure

IRRELEVANT_STATUS1 = 200
IRRELEVANT_STATUS2 = 400


class TestStatus(object):
    def test_should_pass_if_actual_has_expected_status(self):
        expect(response=self.response).to.have.status(IRRELEVANT_STATUS1)

    def test_should_fail_if_actual_hasnt_expected_status(self):
        with failure(self.response,
                     'to have status {!r}'.format(IRRELEVANT_STATUS2)):

            expect(response=self.response).to.have.status(IRRELEVANT_STATUS2)

    def setup(self):
        self.response = flask.Response(status=IRRELEVANT_STATUS1)


class TestNotStatus(object):
    def test_should_pass_if_actual_hasnt_expected_status(self):
        expect(response=self.response).not_to.have.status(IRRELEVANT_STATUS2)

    def test_should_fail_if_actual_has_expected_status(self):
        with failure(self.response,
                     'not to have status {!r}'.format(IRRELEVANT_STATUS1)):

            expect(response=self.response).not_to.have.status(IRRELEVANT_STATUS1)

    def setup(self):
        self.response = flask.Response(status=200)
