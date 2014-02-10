# -*- coding: utf-8 -*-

from expects import expect

from ..helpers import failure
from .. import mixins


class TestHtml(mixins.ContentType):
    def test_should_pass_if_actual_has_text_html_content_type(self):
        expect(response=self.response('text/html')).to.be.html

    def test_should_fail_if_actual_has_application_json_content_type(self):
        with failure():
            expect(response=self.response('application/json')).to.be.html


class TestNotHtml(mixins.ContentType):
    def test_should_pass_if_actual_has_application_json_content_type(self):
        expect(response=self.response('application/json')).not_to.be.html

    def test_should_fail_if_actual_has_text_html_content_type(self):
        with failure():
            expect(response=self.response('text/html')).not_to.be.html
