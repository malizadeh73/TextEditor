#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os


class Config:
    def __init__(self):
        self.applications_root = os.path.join(os.path.dirname(__file__), "")
        self.web = {
            'port': 8080,
            'server_ip': '127.0.0.1',
        }