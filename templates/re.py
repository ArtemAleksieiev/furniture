#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
name = u"виктор"

def valid_username(username):
    USER_RE = re.compile(u"^[а-я0-9_-]{3,15}$")
    return username and USER_RE.match(username)

print valid_username(name)