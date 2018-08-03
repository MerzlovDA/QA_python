# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.ApplicationTest import ApplicationTest


@pytest.fixture
def app(request):
    fixture = ApplicationTest()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="123", header="123", footer="132"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
