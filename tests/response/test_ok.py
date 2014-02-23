# -*- coding: utf-8 -*-

from expects import expect
from expects.testing import failure

from .. import mixins


class TestOk(mixins.Status):
    def test_should_pass_if_actual_has_200_status(self):
        expect(response=self.response(200)).to.be.ok

    def test_should_pass_if_actual_has_201_status(self):
        expect(response=self.response(201)).to.be.ok

    def test_should_pass_if_actual_has_302_status(self):
        expect(response=self.response(302)).to.be.ok

    def test_should_fail_if_actual_has_400_status(self):
        response = self.response(400)

        with failure(response, 'to be ok'):
            expect(response=response).to.be.ok

    def test_should_fail_if_actual_has_500_status(self):
        response = self.response(500)

        with failure(response, 'to be ok'):
            expect(response=response).to.be.ok


class TestNotOk(mixins.Status):
    def test_should_pass_if_actual_has_400_status(self):
        expect(response=self.response(400)).not_to.be.ok

    def test_should_fail_if_actual_has_200_status(self):
        response = self.response(200)

        with failure(response, 'not to be ok'):
            expect(response=response).not_to.be.ok

    def test_should_fail_if_actual_has_302_status(self):
        response = self.response(302)

        with failure(response, 'not to be ok'):
            expect(response=response).not_to.be.ok
