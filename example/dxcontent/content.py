# -*- coding: utf-8 -*-

from plone.dexterity.content import Item
#from plone.dexterity.content import Container

from zope.interface import implements

from example.dxcontent.interfaces import (
    IDXContent,
)

class DXContent(Item):
    implements(IDXContent)



