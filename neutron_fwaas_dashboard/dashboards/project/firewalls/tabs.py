#    Copyright 2013, Big Switch Networks, Inc.
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

from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tabs

from neutron_fwaas_dashboard.api import fwaas as api_fwaas
from neutron_fwaas_dashboard.dashboards.project.firewalls import tables

FirewallsTable = tables.FirewallsTable
PoliciesTable = tables.PoliciesTable
RulesTable = tables.RulesTable


class RulesTab(tabs.TableTab):
    table_classes = (RulesTable,)
    name = _("Firewall Rules")
    slug = "rules"
    template_name = "horizon/common/_detail_table.html"

    def get_rulestable_data(self):
        try:
            tenant_id = self.request.user.tenant_id
            request = self.tab_group.request
            rules = api_fwaas.rule_list_for_tenant(request, tenant_id)
        except Exception:
            rules = []
            exceptions.handle(self.tab_group.request,
                              _('Unable to retrieve rules list.'))

        return rules


class PoliciesTab(tabs.TableTab):
    table_classes = (PoliciesTable,)
    name = _("Firewall Policies")
    slug = "policies"
    template_name = "horizon/common/_detail_table.html"

    def get_policiestable_data(self):
        try:
            tenant_id = self.request.user.tenant_id
            request = self.tab_group.request
            policies = api_fwaas.policy_list_for_tenant(request, tenant_id)
        except Exception:
            policies = []
            exceptions.handle(self.tab_group.request,
                              _('Unable to retrieve policies list.'))

        return policies


class FirewallsTab(tabs.TableTab):
    table_classes = (FirewallsTable,)
    name = _("Firewalls")
    slug = "firewalls"
    template_name = "horizon/common/_detail_table.html"

    def get_firewallstable_data(self):
        try:
            tenant_id = self.request.user.tenant_id
            request = self.tab_group.request
            firewalls = api_fwaas.firewall_list_for_tenant(request, tenant_id)
        except Exception:
            firewalls = []
            exceptions.handle(self.tab_group.request,
                              _('Unable to retrieve firewall list.'))
        return firewalls


class RuleDetailsTab(tabs.Tab):
    name = _("Rule")
    slug = "ruledetails"
    template_name = "project/firewalls/_rule_details.html"

    def get_context_data(self, request):
        return {"rule": self.tab_group.kwargs['rule']}


class PolicyDetailsTab(tabs.Tab):
    name = _("Policy")
    slug = "policydetails"
    template_name = "project/firewalls/_policy_details.html"

    def get_context_data(self, request):
        return {"policy": self.tab_group.kwargs['policy']}


class FirewallDetailsTab(tabs.Tab):
    name = _("Firewall")
    slug = "firewalldetails"
    template_name = "project/firewalls/_firewall_details.html"

    def get_context_data(self, request):
        return {"firewall": self.tab_group.kwargs['firewall']}


class FirewallTabs(tabs.TabGroup):
    slug = "fwtabs"
    tabs = (FirewallsTab, PoliciesTab, RulesTab)
    sticky = True


class RuleDetailsTabs(tabs.TabGroup):
    slug = "ruletabs"
    tabs = (RuleDetailsTab,)


class PolicyDetailsTabs(tabs.TabGroup):
    slug = "policytabs"
    tabs = (PolicyDetailsTab,)


class FirewallDetailsTabs(tabs.TabGroup):
    slug = "firewalltabs"
    tabs = (FirewallDetailsTab,)
