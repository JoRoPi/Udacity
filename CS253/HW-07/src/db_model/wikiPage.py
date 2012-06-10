# -*- coding: utf-8 -*-

import logging
from google.appengine.ext import db
from google.appengine.api import memcache
from user import User

class WikiPage(db.Model):
    wikiUrl = db.StringProperty(required=True)
    wikiContent = db.TextProperty(required=True)
    user = db.ReferenceProperty(User, required=True)
    version = db.IntegerProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    

#    def update_content(self, new_content):
#        self.wikiContent = new_content
#        self.put() # Habría que asegurarse que no han existido otros cambios antes de actualizar, utilizando un atransacción, volviendo a leer y comprobando que no ha cambiado y actualizando o avisando al usuario. 
#        # update memcache
#        mclient = memcache.Client()
#        memkey = WikiPage._memkey_by_url(self.wikiUrl)
#        while True:
#            dummy_wikipage = mclient.gets(memkey)
#            if mclient.cas(memkey, self):
#                break;
    
    @classmethod
    def by_id(cls, wpid):
        mclient = memcache.Client()
        memkey = cls._memkey_by_id(wpid)
        wikipage = mclient.get(memkey)
        if not wikipage:
            logging.info('memcache fail: WikiPage.get_by_id')
            wikipage = WikiPage.get_by_id(wpid, parent = cls._wikipages_key())
            if wikipage:
                mclient.set(memkey, wikipage)
        return wikipage
    
#    @classmethod
#    def by_url(cls, url):
#        mclient = memcache.Client()
#        memkey = cls._memkey_by_url(url)
#        wikipage = mclient.get(memkey)
#        if not wikipage:
#            logging.info('memcache fail: WikiPage.gql')
#            query = WikiPage.gql('WHERE wikiUrl=:wikiUrl', wikiUrl=url)
#            wikipage = query.get()
#            if wikipage:
#                mclient.set(memkey, wikipage)
#        return wikipage
    
    @classmethod
    def by_url(cls, url):
        mclient = memcache.Client()
        memkey = cls._memkey_by_url(url)
        wikipages = mclient.get(memkey)
        if not wikipages:
            logging.info('memcache fail: WikiPage.gql, list version')
            query = WikiPage.gql('WHERE wikiUrl=:wikiUrl ORDER BY version DESC', wikiUrl=url)
            wikipages = query.run()
            wikipages = list(wikipages)
            if len(wikipages):
                mclient.set(memkey, wikipages)
        return wikipages

    @classmethod
    def create_wikipage(cls, url, content, user):
        version = len(cls.by_url(url)) + 1
        wikipage = WikiPage(wikiUrl=url, wikiContent=content, user=user, version=version)
        wikipage.put()
        # update memcache
        mclient = memcache.Client()
        memkey = WikiPage._memkey_by_url(url)
        wikipages = mclient.get(memkey)
        if not wikipages:
            mclient.set(memkey, [wikipage])
        else:
            while True:
                wikipages = mclient.gets(memkey)
                wikipages.insert(0, wikipage)
                if mclient.cas(memkey, wikipages):
                    break;




    @classmethod
    def _wikipages_key(cls, group = 'cs252-wiki'):
        # Temporary disabled. return db.Key.from_path('wikipages', group)
        return db.Key.from_path('wikipages', group)

    @classmethod
    def _memkey_by_id(cls, wpid):
        return 'wikipage_by_id: %s' % wpid

    @classmethod
    def _memkey_by_url(cls, url):
        return 'wikipage_by_url: %s' % url
