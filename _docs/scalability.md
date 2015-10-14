---
layout: docs
title: Scalability of docassemble
short_title: Scalability
---

**docassemble** is easily scalable.  It does not store any user
information in memory or in an in-memory cache.  Rather, it uses a SQL
database to store user answers and a filesystem to store user
documents.  As a result, a cluster of servers can serve responses to
client browsers if each cluster member is configured to point to the
same SQL database and mount the same filesystem.

Each server's configuration is defined in `/etc/docassemble/config.yml`.
The default configuration for the SQL connection is:

	db:
	  prefix: postgresql+psycopg2://
	  name: docassemble
	  user: null
	  password: null
	  host: null
	  port: null

This will cause **docassemble** to connect to PostgreSQL on the local
machine with peer authentication and use the database "docassemble."
This configuration can be modified to connect to use password
authentication on a remote server.

The location of uploaded user files is defined in this line of
`config.yml`:

    uploads: /usr/share/docassemble/files

When developers install new Python packages, the packages are unpacked
in `/var/www/.local` (i.e. the `.local` directory within `www-data`'s
home directory), and the web server is restarted by "touch"ing the
WSGI file.  The path of the WSGI file is defined in the Apache
configuration and in the **docassemble** configuration file:

    webapp: /var/lib/docassemble/flask.wsgi

Therefore, configuring a cluster of **docassemble** servers entails
creating a central network file server to host the following
directories, which the cluser members would mount:

* `/etc/docassemble`
* `/usr/share/docassemble/files`
* `/var/lib/docassemble/`
* `/var/www`

In addition, the `db` section of the `config.yml` file would be
modified to point to a central SQL server.

## Is docassemble thread-safe?

**docassemble** uses `locale` to represent dates and currency.
`locale` is not thread-safe if `locale.setlocale` is called by
different threads.

If your server provides interviews that all use the same locale, then
**docassemble** will be thread-safe.

If your interviews are going to change the locale (which they can do
by calling `docassemble.util.set_locale` and
`docassemble.util.update_locale`) then you should make sure that WSGI
is configured to use multiple processes rather than multiple threads.
The line in the Apache configuration would look something like this:

    WSGIDaemonProcess docassemble.webserver user=www-data group=www-data processes=5 threads=1

However, if the locale will not change and you would like to take
advantage of the performance benefit of multi-threading, you can
configure WSGI to use multiple threads:

    WSGIDaemonProcess docassemble.webserver user=www-data group=www-data threads=5