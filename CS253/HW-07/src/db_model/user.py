# -*- coding: utf-8 -*-

import re
import logging
from google.appengine.ext import db
from google.appengine.api import memcache
import utils.hashing as hashing

class User(db.Model):
    username = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    email = db.StringProperty(required=False)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    
    
    @classmethod
    def by_id(cls, uid):
        mclient = memcache.Client()
        memkey = cls._memkey_by_id(uid)
        user = mclient.get(memkey)
        if not user:
            logging.info('memcache fail: User.get_by_id')
            user = User.get_by_id(uid, parent = cls._users_key())
            if user:
                mclient.set(memkey, user)
        return user

    
    VAL_ERROR_INVALID_USERNAME = 1
    VAL_ERROR_INVALID_PASSWORD = 2
    VAL_ERROR_PASSWORDS_MISMATCH = 3
    VAL_ERROR_INVALID_EMAIL = 4
    VAL_ERROR_USER_EXIST = 5
    
    @classmethod
    def create_user(cls, username, password, verify_password, email):
        val_errors = set()
        cls.valid_username(username, val_errors)
        cls.valid_password(password, val_errors)
        cls.valid_verify(password, verify_password, val_errors)
        cls.valid_email(email, val_errors)
        
        if val_errors:
            return None, val_errors
        else:
            mclient = memcache.Client()
            user = User(username=username, password='%s' % (hashing.make_pw_hash(username, password)), email=email)
            user.put()
            memkey = cls._memkey_by_id(user.key().id())
            mclient.set(memkey, user)
            return user, None
    
    # Validations
    @classmethod
    def valid_username(cls, username, val_errors):
        user_validation_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        if not(user_validation_re.match(username)):
            val_errors.add(User.VAL_ERROR_INVALID_USERNAME)
            return False
        return cls.valid_user_exist(username, val_errors)
        
    @classmethod
    def valid_password(cls, password, val_errors):
        password_validation_re = re.compile(r"^.{3,20}$")
        if not (password_validation_re.match(password)):
            val_errors.add(User.VAL_ERROR_INVALID_PASSWORD)
            return False
        return True

    @classmethod
    def valid_verify(cls, password, verify, val_errors):
        if password != verify:
            val_errors.add(User.VAL_ERROR_PASSWORDS_MISMATCH)
            return False
        return True

    @classmethod
    def valid_email(cls, email, val_errors):
        email_validation_re = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
        if email and not(email_validation_re.match(email)):
            val_errors.add(User.VAL_ERROR_INVALID_EMAIL)
            return False
        return True
    
    @classmethod
    def valid_user_exist(cls, username, val_errors):
        (user, memkey, mclient) = cls._get_by_username(username)
        if user:
            val_errors.add(User.VAL_ERROR_USER_EXIST)
            if memkey:
                mclient.set(memkey, user)
            return False
        return True
    
    @classmethod
    def get_verified_user(cls, username, password):
        (user, memkey, mclient) = cls._get_by_username(username)
        if user:
            if not hashing.valid_pw(username, password, user.password):
                user = None
            elif memkey:
                mclient.set(memkey, user)
        return user





    @classmethod
    def _users_key(cls, group = 'cs252-wiki'):
        # Temporary disabled. return db.Key.from_path('users', group)
        return None
    
    @classmethod
    def _memkey_by_username(cls, username):
        return 'user_by_username: %s' % username

    @classmethod
    def _memkey_by_id(cls, uid):
        return 'user_by_id: %s' % uid
    
    @classmethod
    def _get_by_username(cls, username):
        """ ret (user, memkey, mclient)
            user - Can be None if not found in memcache nor DB
            memkey  - If not None, user was get from DB and is a good idea set in memcache
            mclient - memcache.Client()
        """
        mclient = memcache.Client()
        memkey = cls._memkey_by_username(username)
        user = mclient.get(memkey)
        if user:
            memkey = None
        else:
            logging.info('memcache fail: User.gql')
            query = User.gql('WHERE username=:username', username=username)
            user = query.get()
        return (user, memkey, mclient)
