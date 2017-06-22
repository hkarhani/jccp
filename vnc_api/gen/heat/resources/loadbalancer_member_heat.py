
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


class ContrailLoadbalancerMember(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, LOADBALANCER_MEMBER_PROPERTIES, LOADBALANCER_MEMBER_PROPERTIES_ADMIN_STATE, LOADBALANCER_MEMBER_PROPERTIES_STATUS, LOADBALANCER_MEMBER_PROPERTIES_STATUS_DESCRIPTION, LOADBALANCER_MEMBER_PROPERTIES_PROTOCOL_PORT, LOADBALANCER_MEMBER_PROPERTIES_WEIGHT, LOADBALANCER_MEMBER_PROPERTIES_ADDRESS, DISPLAY_NAME, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, LOADBALANCER_POOL
    ) = (
        'name', 'fq_name', 'loadbalancer_member_properties', 'loadbalancer_member_properties_admin_state', 'loadbalancer_member_properties_status', 'loadbalancer_member_properties_status_description', 'loadbalancer_member_properties_protocol_port', 'loadbalancer_member_properties_weight', 'loadbalancer_member_properties_address', 'display_name', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'loadbalancer_pool'
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
        LOADBALANCER_MEMBER_PROPERTIES: properties.Schema(
            properties.Schema.MAP,
            _('LOADBALANCER_MEMBER_PROPERTIES.'),
            update_allowed=True,
            required=False,
            schema={
                LOADBALANCER_MEMBER_PROPERTIES_ADMIN_STATE: properties.Schema(
                    properties.Schema.BOOLEAN,
                    _('LOADBALANCER_MEMBER_PROPERTIES_ADMIN_STATE.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_MEMBER_PROPERTIES_STATUS: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_MEMBER_PROPERTIES_STATUS.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_MEMBER_PROPERTIES_STATUS_DESCRIPTION: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_MEMBER_PROPERTIES_STATUS_DESCRIPTION.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_MEMBER_PROPERTIES_PROTOCOL_PORT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('LOADBALANCER_MEMBER_PROPERTIES_PROTOCOL_PORT.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_MEMBER_PROPERTIES_WEIGHT: properties.Schema(
                    properties.Schema.INTEGER,
                    _('LOADBALANCER_MEMBER_PROPERTIES_WEIGHT.'),
                    update_allowed=True,
                    required=False,
                ),
                LOADBALANCER_MEMBER_PROPERTIES_ADDRESS: properties.Schema(
                    properties.Schema.STRING,
                    _('LOADBALANCER_MEMBER_PROPERTIES_ADDRESS.'),
                    update_allowed=True,
                    required=False,
                ),
            }
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
        LOADBALANCER_POOL: properties.Schema(
            properties.Schema.STRING,
            _('LOADBALANCER_POOL.'),
            update_allowed=True,
            required=False,
        ),
    }

    attributes_schema = {
        NAME: attributes.Schema(
            _('NAME.'),
        ),
        FQ_NAME: attributes.Schema(
            _('FQ_NAME.'),
        ),
        LOADBALANCER_MEMBER_PROPERTIES: attributes.Schema(
            _('LOADBALANCER_MEMBER_PROPERTIES.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        LOADBALANCER_POOL: attributes.Schema(
            _('LOADBALANCER_POOL.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.LOADBALANCER_POOL):
            try:
                parent_obj = self.vnc_lib().loadbalancer_pool_read(id=self.properties.get(self.LOADBALANCER_POOL))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().loadbalancer_pool_read(fq_name_str=self.properties.get(self.LOADBALANCER_POOL))
            except:
                parent_obj = None

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.LoadbalancerMember(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.LOADBALANCER_MEMBER_PROPERTIES) is not None:
            obj_1 = vnc_api.LoadbalancerMemberType()
            if self.properties.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_ADMIN_STATE) is not None:
                obj_1.set_admin_state(self.properties.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_ADMIN_STATE))
            if self.properties.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_STATUS) is not None:
                obj_1.set_status(self.properties.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_STATUS))
            if self.properties.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_STATUS_DESCRIPTION) is not None:
                obj_1.set_status_description(self.properties.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_STATUS_DESCRIPTION))
            if self.properties.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_PROTOCOL_PORT) is not None:
                obj_1.set_protocol_port(self.properties.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_PROTOCOL_PORT))
            if self.properties.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_WEIGHT) is not None:
                obj_1.set_weight(self.properties.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_WEIGHT))
            if self.properties.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_ADDRESS) is not None:
                obj_1.set_address(self.properties.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_ADDRESS))
            obj_0.set_loadbalancer_member_properties(obj_1)
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

        try:
            obj_uuid = super(ContrailLoadbalancerMember, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().loadbalancer_member_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.LOADBALANCER_MEMBER_PROPERTIES) is not None:
            obj_1 = vnc_api.LoadbalancerMemberType()
            if prop_diff.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_ADMIN_STATE) is not None:
                obj_1.set_admin_state(prop_diff.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_ADMIN_STATE))
            if prop_diff.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_STATUS) is not None:
                obj_1.set_status(prop_diff.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_STATUS))
            if prop_diff.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_STATUS_DESCRIPTION) is not None:
                obj_1.set_status_description(prop_diff.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_STATUS_DESCRIPTION))
            if prop_diff.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_PROTOCOL_PORT) is not None:
                obj_1.set_protocol_port(prop_diff.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_PROTOCOL_PORT))
            if prop_diff.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_WEIGHT) is not None:
                obj_1.set_weight(prop_diff.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_WEIGHT))
            if prop_diff.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_ADDRESS) is not None:
                obj_1.set_address(prop_diff.get(self.LOADBALANCER_MEMBER_PROPERTIES, {}).get(self.LOADBALANCER_MEMBER_PROPERTIES_ADDRESS))
            obj_0.set_loadbalancer_member_properties(obj_1)
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

        try:
            self.vnc_lib().loadbalancer_member_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().loadbalancer_member_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('loadbalancer_member %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().loadbalancer_member_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::LoadbalancerMember': ContrailLoadbalancerMember,
    }
