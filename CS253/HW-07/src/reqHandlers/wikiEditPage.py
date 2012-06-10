# -*- coding: utf-8 -*-

from wikiBasePage import WikiBasePage
from db_model.wikiPage import WikiPage

class WikiEditPage(WikiBasePage):
    def default_template_values(self):
        return super(WikiEditPage, self).default_template_values()
    
    def render_front(self, template_values=None):
        super(WikiEditPage, self).render_front('wikiedit.html', template_values)
        
    def get(self, wiki_page_url):
        super(WikiEditPage, self).get()
        
        super(WikiEditPage, self).set_main_user_options()
        
        wikiPages = WikiPage.by_url(wiki_page_url)
        
        if len(wikiPages):
            # Set top-main-options about page options
            super(WikiEditPage, self).set_main_history_option(wiki_page_url, prefix=True)
            if self.user:
                super(WikiEditPage, self).set_main_view_option(wiki_page_url)
                
            self.template_values[self._tp_wikiPageContent] = wikiPages[0].wikiContent
        else:
            if not self.user:
                self.template_values[self._tp_pageNotExistError] = True
            
        self.render_front(self.set_template_values(self.template_values))
        
    def post(self, wiki_page_url):
#        wikiPage = WikiPage.by_url(wiki_page_url)
#        
#        if wikiPage:
#            wikiPage.update_content(self.request.get(self._id_content))
#        else:
#            WikiPage.create_wikipage(wiki_page_url, self.request.get(self._id_content), self.user)
        WikiPage.create_wikipage(wiki_page_url, self.request.get(self._id_content), self.user)
        
        self.redirect(wiki_page_url.replace(self._edit_url_mode_prefix, ''))




    _id_content = 'content'
