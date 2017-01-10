# -*- coding: utf-8 -*-
# Copyright 2014 Objectif Libre
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: Stéphane Albert
#
from oslo_context import context
from pecan import hooks

from devicedemo.common import policy
from devicedemo import messaging


class RPCHook(hooks.PecanHook):
    def __init__(self):
        self._rpc_client = messaging.get_client()

    def before(self, state):
        state.request.rpc_client = self._rpc_client


class ContextHook(hooks.PecanHook):
    def on_route(self, state):
        headers = state.request.headers

        roles = headers.get('X-Roles', '').split(',')
        is_admin = policy.check_is_admin(roles)

        creds = {
            'user': headers.get('X-User') or headers.get('X-User-Id'),
            'tenant': headers.get('X-Tenant') or headers.get('X-Tenant-Id'),
            'auth_token': headers.get('X-Auth-Token'),
            'is_admin': is_admin,
            'roles': roles,
        }

        state.request.context = context.RequestContext(**creds)
