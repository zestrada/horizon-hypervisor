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

from horizon import tables
from django.utils.translation import ugettext_lazy as _

class HypervisorListTable(tables.DataTable):
    ID = tables.Column('id', verbose_name=_("ID"))
    hostname = tables.Column('hypervisor_hostname', verbose_name=_("Hostname"))

    class Meta:
        name = "hypervisors_list"
        verbose_name = _("Hypervisor List")

class HypervisorStatsTable(tables.DataTable):
    prop = tables.Column('property', verbose_name=_("Property"))
    val = tables.Column('value', verbose_name=_("Value"))

    class Meta:
        name = "hypervisors_stats"
        verbose_name = _("Hypervisor Stats")
