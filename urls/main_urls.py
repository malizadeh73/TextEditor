#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.main import *

url_patterns = [
    ("/register", RegisterHandler, None, "register"),
    ("/api/text_editor", TextEditorHandler, None, "text_editor"),

]
