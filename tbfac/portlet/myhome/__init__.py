from zope.i18nmessageid import MessageFactory
MyHomeMessageFactory = MessageFactory('tbfac.portlet.myhome')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
