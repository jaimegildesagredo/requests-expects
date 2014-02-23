# -*- coding: utf-8 -*-

import flask


class ContentType(object):
    def response(self, content_type):
        return flask.Response(headers={'Content-Type': content_type})


class Status(object):
    def response(self, status):
        return flask.Response(status=status)
