# -*- coding: utf-8 -*-

from handlerBase import HandlerBase

class WikiBasePage(HandlerBase):
    def default_template_values(self, init_values=None):
        if not init_values:
            init_values = {}
        
        values = {self._tp_wikiPageContent: '',
                  self._tp_loginLink: False,
                  self._tp_signupLink: False,
                  self._tp_logoutLink: False,
                  self._tp_userName: '',
                  self._tp_editLink: False,
                  self._tp_viewLink: False,
                  self._tp_historyLink: False,
                  self._tp_editLinkUrl: '',
                  self._tp_viewLinkUrl: '',
                  self._tp_historyLinkUrl: '',
                  self._tp_pageNotExistError: False}
        
        values.update(init_values)
        return values
    
    def get(self):
        self.template_values = {}
    
    def set_main_user_options(self):
        """Set top-main-options about user logged o anonymous"""
        if self.user:
            self.template_values[self._tp_logoutLink] = True
            self.template_values[self._tp_userName] = self.user.username
        else:
            self.template_values[self._tp_loginLink] = True
            self.template_values[self._tp_signupLink] = True

    def set_main_history_option(self, url, prefix=False):
        if prefix: url = self._history_url_prefix + url
        self.template_values[self._tp_historyLink] = True
        self.template_values[self._tp_historyLinkUrl] = url
        
    def unset_history_prefix(self, url):
        return url.replace(self._history_url_prefix, '')

    def set_main_edit_option(self, url, prefix=False):
        if prefix: url = self.set_edit_prefix(url)
        self.template_values[self._tp_editLink] = True
        self.template_values[self._tp_editLinkUrl] = url
        
    def set_edit_prefix(self, url):
        return self._edit_url_mode_prefix + url
        
    def unset_edit_prefix(self, url):
        return url.replace(self._edit_url_mode_prefix, '')

    def set_main_view_option(self, url):
        self.template_values[self._tp_viewLink] = True
        self.template_values[self._tp_viewLinkUrl] = url
    


    _tp_wikiPageContent = 'wikiPageContent'
    _tp_loginLink = 'loginLink'
    _tp_signupLink = 'signupLink'
    _tp_logoutLink = 'logoutLink'
    _tp_userName = 'userName'
    _tp_editLink = 'editLink'
    _tp_viewLink = 'viewLink'
    _tp_historyLink = 'historyLink'
    _tp_editLinkUrl = 'editLinkUrl'
    _tp_viewLinkUrl = 'viewLinkUrl'
    _tp_historyLinkUrl = 'historyLinkUrl'
    _tp_pageNotExistError = 'pageNotExistError'
    
    _edit_url_mode_prefix = '/_edit'
    _history_url_prefix = '/_history'
    
