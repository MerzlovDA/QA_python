# -*- coding: utf-8 -*-
import pytest
from group import Group
from ApplicationTest import ApplicationTest


@pytest.fixture
def app(request):
    fixture = ApplicationTest()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="123", header="123", footer="132"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
