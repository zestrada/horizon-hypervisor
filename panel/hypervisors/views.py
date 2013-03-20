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
from .tables import HypervisorStatsTable

class IndexView(tables.MultiTableView):
    table_classes = (HypervisorListTable,HypervisorStatsTable)
    template_name = 'admin/hypervisors/index.html'

    def get_hypervisors_list_data(self):
        nova = api.nova.novaclient(self.request)
        hypervisor_list = nova.hypervisors.list(False)
        return hypervisor_list

    def get_hypervisors_stats_data(self):
        nova = api.nova.novaclient(self.request)
        hypervisor_stats = nova.hypervisors.statistics()._info.copy()
        statList = []
        for k,v in hypervisor_stats.items():
            statList.append(HypStat(k,v))
        return statList

class HypStat(object):
    property = ""
    value = ""
    def __init__(self,prop,val):
        self.id = prop
        self.property = prop
        self.value = val
