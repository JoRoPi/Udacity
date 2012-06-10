# -*- coding: utf-8 -*-

from wikiBasePage import WikiBasePage
from db_model.wikiPage import WikiPage

class WikiMainPage(WikiBasePage):
    def default_template_values(self):
        init_template_values = {self._tp_wikiPageContent: '** Not Set **',
                                }
        return super(WikiMainPage, self).default_template_values(init_template_values)
    
    def render_front(self, template_values=None):
        super(WikiMainPage, self).render_front('wikifront.html', template_values)
        
    def get(self, wiki_page_url):
        super(WikiMainPage, self).get()
        
        super(WikiMainPage, self).set_main_user_options()
        
        wikiPages = WikiPage.by_url(wiki_page_url)
        
        if wikiPages and len(wikiPages):
            # Set top-main-options about page options
            super(WikiMainPage, self).set_main_history_option(wiki_page_url, prefix=True)
            if self.user:
                super(WikiMainPage, self).set_main_edit_option(wiki_page_url, prefix=True)
                
            version = self.request.get('v')
            
            if version.isdigit() and int(version) > 0 and int(version) <= len(wikiPages):
                version = len(wikiPages) - int(version)
            else:
                version = 0
            self.template_values[self._tp_wikiPageContent] = wikiPages[version].wikiContent.replace('\n', '<br>')
        else:
            if not self.user:
                self.template_values[self._tp_pageNotExistError] = True
            else:
                self.redirect(self._edit_url_mode_prefix + wiki_page_url)
            
        self.render_front(self.set_template_values(self.template_values))
    
    
