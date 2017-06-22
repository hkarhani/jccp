
# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

from contrail_heat.resources import contrail
try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import attributes
from heat.engine import constraints
from heat.engine import properties
try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging
import uuid

from vnc_api import vnc_api

LOG = logging.getLogger(__name__)


class ContrailDomain(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, DOMAIN_LIMITS, DOMAIN_LIMITS_PROJECT_LIMIT, DOMAIN_LIMITS_VIRTUAL_NETWORK_LIMIT, DOMAIN_LIMITS_SECURITY_GROUP_LIMIT
    ) = (
        'name', 'fq_name', 'display_name', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'domain_limits', 'domain_limits_project_limit', 'domain_limits_virtual_network_limit', 'domain_limits_security_group_limit'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('NAME.'),
            update_allowed=True,
            required=False,
        ),
        FQ_NAME: properties.Schema(
            properties.Schema.STRING,
            _('FQ_NAME.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        ANNOTATIONS: properties.Schema(
            properties.Schema.MAP,
            _('ANNOTATIONS.'),
            update_allowed=True,
            required=False,
            schema={
                ANNOTATIONS_KEY_VALUE_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('ANNOTATIONS_KEY_VALUE_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            ANNOTATIONS_KEY_VALUE_PAIR_KEY: properties.Schema(
                                properties.Schema.STRING,
                                _('ANNOTATIONS_KEY_VALUE_PAIR_KEY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            ANNOTATIONS_KEY_VALUE_PAIR_VALUE: properties.Schema(
                                properties.Schema.STRING,
                                _('ANNOTATIONS_KEY_VALUE_PAIR_VALUE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        DOMAIN_LIMITS: properties.Schema(
            properties.Schema.MAP,
            _('DOMAIN_LIMITS.'),
            update_allowed=True,
            required=False,
            schema={
                DOMAIN_LIMITS_PROJECT_LIMIT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('DOMAIN_LIMITS_PROJECT_LIMIT.'),
                    update_allowed=True,
                    required=False,
                ),
                DOMAIN_LIMITS_VIRTUAL_NETWORK_LIMIT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('DOMAIN_LIMITS_VIRTUAL_NETWORK_LIMIT.'),
                    update_allowed=True,
                    required=False,
                ),
                DOMAIN_LIMITS_SECURITY_GROUP_LIMIT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('DOMAIN_LIMITS_SECURITY_GROUP_LIMIT.'),
                    update_allowed=True,
                    required=False,
                ),
            }
        ),
    }

    attributes_schema = {
        NAME: attributes.Schema(
            _('NAME.'),
        ),
        FQ_NAME: attributes.Schema(
            _('FQ_NAME.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        DOMAIN_LIMITS: attributes.Schema(
            _('DOMAIN_LIMITS.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        obj_0 = vnc_api.Domain(name=self.properties[self.NAME])

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.ANNOTATIONS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY))
                    if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_annotations(obj_1)
        if self.properties.get(self.DOMAIN_LIMITS) is not None:
            obj_1 = vnc_api.DomainLimitsType()
            if self.properties.get(self.DOMAIN_LIMITS, {}).get(self.DOMAIN_LIMITS_PROJECT_LIMIT) is not None:
                obj_1.set_project_limit(self.properties.get(self.DOMAIN_LIMITS, {}).get(self.DOMAIN_LIMITS_PROJECT_LIMIT))
            if self.properties.get(self.DOMAIN_LIMITS, {}).get(self.DOMAIN_LIMITS_VIRTUAL_NETWORK_LIMIT) is not None:
                obj_1.set_virtual_network_limit(self.properties.get(self.DOMAIN_LIMITS, {}).get(self.DOMAIN_LIMITS_VIRTUAL_NETWORK_LIMIT))
            if self.properties.get(self.DOMAIN_LIMITS, {}).get(self.DOMAIN_LIMITS_SECURITY_GROUP_LIMIT) is not None:
                obj_1.set_security_group_limit(self.properties.get(self.DOMAIN_LIMITS, {}).get(self.DOMAIN_LIMITS_SECURITY_GROUP_LIMIT))
            obj_0.set_domain_limits(obj_1)

        try:
            obj_uuid = super(ContrailDomain, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().domain_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.ANNOTATIONS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY))
                    if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_annotations(obj_1)
        if prop_diff.get(self.DOMAIN_LIMITS) is not None:
            obj_1 = vnc_api.DomainLimitsType()
            if prop_diff.get(self.DOMAIN_LIMITS, {}).get(self.DOMAIN_LIMITS_PROJECT_LIMIT) is not None:
                obj_1.set_project_limit(prop_diff.get(self.DOMAIN_LIMITS, {}).get(self.DOMAIN_LIMITS_PROJECT_LIMIT))
            if prop_diff.get(self.DOMAIN_LIMITS, {}).get(self.DOMAIN_LIMITS_VIRTUAL_NETWORK_LIMIT) is not None:
                obj_1.set_virtual_network_limit(prop_diff.get(self.DOMAIN_LIMITS, {}).get(self.DOMAIN_LIMITS_VIRTUAL_NETWORK_LIMIT))
            if prop_diff.get(self.DOMAIN_LIMITS, {}).get(self.DOMAIN_LIMITS_SECURITY_GROUP_LIMIT) is not None:
                obj_1.set_security_group_limit(prop_diff.get(self.DOMAIN_LIMITS, {}).get(self.DOMAIN_LIMITS_SECURITY_GROUP_LIMIT))
            obj_0.set_domain_limits(obj_1)

        try:
            self.vnc_lib().domain_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().domain_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('domain %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().domain_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::Domain': ContrailDomain,
    }
