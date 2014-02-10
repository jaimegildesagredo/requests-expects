# -*- coding: utf-8 -*-

from expects import expect

from ..helpers import failure
from .. import mixins


class TestJson(mixins.ContentType):
    def test_should_pass_if_actual_has_application_json_content_type(self):
        expect(response=self.response('application/json')).to.be.json

    def test_should_fail_if_actual_has_text_xml_content_type(self):
        with failure():
            expect(response=self.response('text/xml')).to.be.json


class TestNotJson(mixins.ContentType):
    def test_should_pass_if_actual_has_text_xml_content_type(self):
        expect(response=self.response('text/xml')).not_to.be.json

    def test_should_fail_if_actual_has_application_json_content_type(self):
        with failure():
            expect(response=self.response('application/json')).not_to.be.json
