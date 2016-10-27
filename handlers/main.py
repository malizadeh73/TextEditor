#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import json
import datetime
from models import *
from handlers.base import WebBaseHandler
from hazm import *
from random import randint


class TextEditorHandler(WebBaseHandler):

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        token = self.get_argument("token", None)
        text = self.get_argument("text", None)
        date = datetime.datetime.now().date()
        find_user = True
        try:
            user = User.select().where(User.token == token).get()
        except:
            find_user = False
        if find_user:
            if user.date == date:
                if user.counter <= 20:
                    counter = user.counter + 1
                    User.update(counter=counter).where(User.token == token).execute()
                    normalizer = Normalizer()
                    text = normalizer.normalize(text)
                    self.result['Res'] = text
                    self.write(self.result)
                else:
                    self.result['Err'] = 1
                    self.result['Msg'] = "شما در هر روز فقط 20 بار میتوانید درخواست دهید."
                    self.write(self.result)
            else:
                User.update(counter=1, date=date).where(User.token == token).execute()
                normalizer = Normalizer()
                text = normalizer.normalize(text)
                self.result['Res'] = text
                self.write(self.result)
        else:
            self.result['Err'] = 1
            self.result['Msg'] = "توکن معتبر نیست"
            self.write(self.result)


class RegisterHandler(WebBaseHandler):

    def get(self, *args, **kwargs):
        self.render("register.html")

    def post(self, *args, **kwargs):
        email = self.get_argument("email", None)
        if email == "":
            self.result['Err'] = 1
            self.result['Msg'] = "لطفا فیلد ایمیل را پر کنید."
            self.write(json.dumps(self.result))
        else:
            date = datetime.datetime.now().date()
            token = randint(0, 999999999)
            counter = 0
            find_user = True
            try:
                user = User.select().where(User.email == email).get()
            except:
                find_user = False
            if find_user:
                self.result['Err'] = 1
                self.result['Msg'] = "ایمیل تکراری است."
                self.write(json.dumps(self.result))
            else:
                User.create(
                    email=email,
                    date=date,
                    token=token,
                    counter=counter
                )
                self.result['Res'] = token
                self.write(json.dumps(self.result))

