# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


class SharedTable(object):
    def __init__(self, capacity=10):
        pass

    def add_dict(self, dict_id, capacity=10, new_if_exists=False):
        pass

    def put(self, dict_id, key, value):
        pass

    def get(self, dict_id, key, default=None):
        pass
