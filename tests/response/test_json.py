# -*- coding: utf-8 -*-

from expects import expect
from expects.testing import failure

from .. import mixins


class TestJson(mixins.ContentType):
    def test_should_pass_if_actual_has_application_json_content_type(self):
        expect(response=self.response('application/json')).to.be.json

    def test_should_fail_if_actual_has_text_xml_content_type(self):
        response = self.response('text/xml')

        with failure(response, 'to be json'):
            expect(response=response).to.be.json


class TestNotJson(mixins.ContentType):
    def test_should_pass_if_actual_has_text_xml_content_type(self):
        expect(response=self.response('text/xml')).not_to.be.json

    def test_should_fail_if_actual_has_application_json_content_type(self):
        response = self.response('application/json')

        with failure(response, 'not to be json'):
            expect(response=response).not_to.be.json
