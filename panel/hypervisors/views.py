# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Zachary J Estrada
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

from django.conf import settings

from openstack_dashboard import api

from novaclient import base
from horizon import tables

from .tables import HypervisorListTable

class IndexView(tables.DataTableView):
    table_class = HypervisorListTable
    template_name = 'admin/hypervisors/list.html'

    def get_data(self):
        nova = api.nova.novaclient(self.request)
        hypervisor_list = nova.hypervisors.list(False)
        return hypervisor_list
