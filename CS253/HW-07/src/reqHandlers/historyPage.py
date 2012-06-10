# -*- coding: utf-8 -*-

from wikiBasePage import WikiBasePage
from db_model.wikiPage import WikiPage

class HistoryPage(WikiBasePage):
    def default_template_values(self):
        return super(HistoryPage, self).default_template_values()
    
    def render_front(self, template_values=None):
        super(HistoryPage, self).render_front('history.html', template_values)
        
    def get(self, wiki_page_url):
        super(HistoryPage, self).get()
        
        super(HistoryPage, self).set_main_user_options()
        
        wikiPages = WikiPage.by_url(wiki_page_url)
        
        if len(wikiPages):
            # Set top-main-options about page options
            super(HistoryPage, self).set_main_view_option(wiki_page_url)
            if self.user:
                super(HistoryPage, self).set_main_edit_option(wiki_page_url, prefix=True)
                
            self.template_values['wikiPages'] = wikiPages
        else:
            if not self.user:
                self.template_values[self._tp_pageNotExistError] = True
            
        self.render_front(self.set_template_values(self.template_values))
        
#        <div class="blogpost-item-list">
#            <div class="blogpost-head-item-list">&nbsp;
#                <div class="blogpost-subject-item-list">
#                    <a class="blogpost-link-item-list" href="{{home_page}}/{{blogpost.key().id()}}">{{blogpost.subject}}</a>
#                </div>
#                <div class="blogpost-created-item-list">{{blogpost.created.strftime('%h %d, %Y')}}</div>
#            </div>
#            <div class="blogpost-content-item-list">{{blogpost.content_ajust_render() | safe}}</div>
#            <br>
#            <br>
#        </div>
