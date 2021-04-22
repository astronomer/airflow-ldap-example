""""
This configuration is for a typical OpenLDAP setup (where LDAP searches require a special account)

SQLALCHEMY_DATABASE_URI:        Airflow metadatabase URI. By default, this is taken from airflow.cfg
CSRF_ENABLED:                   Enable CSRF protection. Should be set to True

AUTH_TYPE:                      Authentication method to be used. Note that the value must be imported from
                                "flask_appbuilder.security.manager". Possible Values are: AUTH_DB, AUTH_LDAP,
                                AUTH_OAUTH, AUTH_OID, and AUTH_REMOTE_USER
AUTH_ROLE_ADMIN:                The role of the bind user (most of the time, it is Admin)
AUTH_LDAP_SERVER:               The LDAP server URI

AUTH_USER_REGISTRATION:         Boolean for automatically creating users on first log-in
AUTH_USER_REGISTRATION_ROLE:    The role which first-time users logging in will be assigned
                                Possible Values: Admin, Viewer, User, Op, Public
AUTH_LDAP_FIRSTNAME_FIELD:      First Name field in LDAP. Example: givenName
AUTH_LDAP_LASTNAME_FIELD:       Last Name field in LDAP. Example: sn
AUTH_LDAP_EMAIL_FIELD:          Email field in LDAP. Example: mail

AUTH_LDAP_SEARCH:               Update with the LDAP path under which you’d like the users to have access to Airflow.
                                Example: dc=example,dc=com.
AUTH_LDAP_UID_FIELD:            The UID (unique identifier) field in LDAP
AUTH_LDAP_BIND_USER:            The path of the LDAP proxy user to bind on to the top level.
                                Example: cn=airflow,ou=users,dc=example,dc=com.
AUTH_LDAP_BIND_PASSWORD:        Password for the bind user

AUTH_LDAP_USE_TLS:              Boolean whether TLS is being used
AUTH_LDAP_ALLOW_SELF_SIGNED:    Boolean to allow self-signed certificates
AUTH_LDAP_TLS_CACERTFILE:       Location of the certificate

#dc – domain component
#cn – common name
#ou – org units

Reference:
https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/security/manager.py
https://flask-appbuilder.readthedocs.io/en/latest/security.html#authentication-ldap

Inspired by:
https://gist.github.com/prakshalj0512/3f8f84b72f7a3053d145f829558cece7
"""


import os
from airflow import configuration as conf
from flask_appbuilder.security.manager import AUTH_LDAP


SQLALCHEMY_DATABASE_URI = conf.get("core", "SQL_ALCHEMY_CONN")
CSRF_ENABLED = True

AUTH_TYPE = AUTH_LDAP
AUTH_ROLE_ADMIN = "Admin"
AUTH_LDAP_SERVER = "ldap://ldap-server:10389"

# registration configs
AUTH_USER_REGISTRATION = True
AUTH_LDAP_FIRSTNAME_FIELD = "givenName"
AUTH_LDAP_LASTNAME_FIELD = "sn"
AUTH_LDAP_EMAIL_FIELD = "mail"
# Required if not mapping from LDAP DN
# AUTH_USER_REGISTRATION_ROLE = "Viewer"

# search configs
AUTH_LDAP_SEARCH = "ou=people,dc=planetexpress,dc=com"
AUTH_LDAP_UID_FIELD = "uid"
AUTH_LDAP_BIND_USER = "cn=admin,dc=planetexpress,dc=com"
AUTH_LDAP_BIND_PASSWORD = "GoodNewsEveryone"

# mapping from LDAP DN to airflow roles
AUTH_ROLES_MAPPING = {
    "cn=admin_staff,ou=people,dc=planetexpress,dc=com": ["Admin"],
    "cn=ship_crew,ou=people,dc=planetexpress,dc=com": ["Viewer"],
}
AUTH_LDAP_GROUP_FIELD = "memberOf"
AUTH_ROLES_SYNC_AT_LOGIN = True
PERMANENT_SESSION_LIFETIME = 1800

# LDAPS
AUTH_LDAP_USE_TLS = False
AUTH_LDAP_ALLOW_SELF_SIGNED = False
AUTH_LDAP_TLS_CACERTFILE = '/etc/ssl/certs/ca-certificates.crt'
