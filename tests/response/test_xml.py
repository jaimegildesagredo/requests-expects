# -*- coding: utf-8 -*-

from expects import expect
from expects.testing import failure

from .. import mixins


class TestXml(mixins.ContentType):
    def test_should_pass_if_actual_has_text_xml_content_type(self):
        expect(response=self.response('text/xml')).to.be.xml

    def test_should_pass_if_actual_has_application_xml_content_type(self):
        expect(response=self.response('application/xml')).to.be.xml

    def test_should_fail_if_actual_has_application_json_content_type(self):
        response = self.response('application/json')

        with failure(response, 'to be xml'):
            expect(response=response).to.be.xml


class TestNotXml(mixins.ContentType):
    def test_should_pass_if_actual_has_application_json_content_type(self):
        expect(response=self.response('application/json')).not_to.be.xml

    def test_should_fail_if_actual_has_text_xml_content_type(self):
        response = self.response('text/xml')

        with failure(response, 'not to be xml'):
            expect(response=response).not_to.be.xml

    def test_should_fail_if_actual_has_application_xml_content_type(self):
        response = self.response('application/xml')

        with failure(response, 'not to be xml'):
            expect(response=response).not_to.be.xml
