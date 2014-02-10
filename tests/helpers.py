# -*- coding: utf-8 -*-

import contextlib


@contextlib.contextmanager
def failure():
    try:
        yield
    except AssertionError:
        pass
    except Exception as error:
        raise AssertionError(
            'Expected AssertionError to be raised but {} raised'.format(type(error)))
    else:
        raise AssertionError(
            'Expected AssertionError to be raised but not raised')
