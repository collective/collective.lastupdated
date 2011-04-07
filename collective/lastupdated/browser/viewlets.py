from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common
from zope.component import getMultiAdapter


class LastUpdatedViewlet(common.ViewletBase):
    index = ViewPageTemplateFile('viewlet_lastupdated.pt')

    def modified(self):
        """        http://svn.plone.org/svn/plone/Plone/trunk/Products/CMFPlone/browser/ploneview.py
        @return: Last modified as a string, local time format        """
        # Get Plone helper view
        # which we use to convert the date to local format
        plone=getMultiAdapter((self.context,self.request),name="plone")
        time=self.context.modified()
        return plone.toLocalizedTime(time)

