# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""IIIF API for Invenio."""

from __future__ import absolute_import, print_function

from flask_iiif import IIIF
from flask_restful import Api

from . import config
from .handlers import image_opener


class InvenioIIIF(object):
    """Invenio-IIIF extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions['invenio-iiif'] = self

        ext = IIIF(app=app)
        api = Api(app=app)
        ext.init_restful(api, prefix='/iiif/')
        ext.uuid_to_image_opener_handler(image_opener)
        # ext.api_decorator_handler(self.protect_api)

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith('IIIF_'):
                app.config.setdefault(k, getattr(config, k))
