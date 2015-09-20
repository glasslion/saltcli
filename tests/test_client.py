# -*- coding: utf-8 -*-
import os.path
from salt.client import LocalClient


def test_cmd():
    local = LocalClient()
    ret = local.cmd('*', 'test.ping')
    assert ret == {'master': True}
