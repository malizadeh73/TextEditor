#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web


class WebBaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(WebBaseHandler, self).__init__(application, request, **kwargs)
        self.result = dict(
            Err="0",
            Msg="0",
            Res="0"
        )

    def on_finish(self):
        pass

