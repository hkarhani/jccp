
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


class ContrailQosQueue(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, MAX_BANDWIDTH, QOS_QUEUE_IDENTIFIER, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, MIN_BANDWIDTH, GLOBAL_QOS_CONFIG
    ) = (
        'name', 'fq_name', 'display_name', 'max_bandwidth', 'qos_queue_identifier', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'min_bandwidth', 'global_qos_config'
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
        MAX_BANDWIDTH: properties.Schema(
            properties.Schema.INTEGER,
            _('MAX_BANDWIDTH.'),
            update_allowed=True,
            required=False,
        ),
        QOS_QUEUE_IDENTIFIER: properties.Schema(
            properties.Schema.INTEGER,
            _('QOS_QUEUE_IDENTIFIER.'),
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
        MIN_BANDWIDTH: properties.Schema(
            properties.Schema.INTEGER,
            _('MIN_BANDWIDTH.'),
            update_allowed=True,
            required=False,
        ),
        GLOBAL_QOS_CONFIG: properties.Schema(
            properties.Schema.STRING,
            _('GLOBAL_QOS_CONFIG.'),
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
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        MAX_BANDWIDTH: attributes.Schema(
            _('MAX_BANDWIDTH.'),
        ),
        QOS_QUEUE_IDENTIFIER: attributes.Schema(
            _('QOS_QUEUE_IDENTIFIER.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        MIN_BANDWIDTH: attributes.Schema(
            _('MIN_BANDWIDTH.'),
        ),
        GLOBAL_QOS_CONFIG: attributes.Schema(
            _('GLOBAL_QOS_CONFIG.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.GLOBAL_QOS_CONFIG):
            try:
                parent_obj = self.vnc_lib().global_qos_config_read(id=self.properties.get(self.GLOBAL_QOS_CONFIG))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().global_qos_config_read(fq_name_str=self.properties.get(self.GLOBAL_QOS_CONFIG))
            except:
                parent_obj = None

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.QosQueue(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.MAX_BANDWIDTH) is not None:
            obj_0.set_max_bandwidth(self.properties.get(self.MAX_BANDWIDTH))
        if self.properties.get(self.QOS_QUEUE_IDENTIFIER) is not None:
            obj_0.set_qos_queue_identifier(self.properties.get(self.QOS_QUEUE_IDENTIFIER))
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
        if self.properties.get(self.MIN_BANDWIDTH) is not None:
            obj_0.set_min_bandwidth(self.properties.get(self.MIN_BANDWIDTH))

        try:
            obj_uuid = super(ContrailQosQueue, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().qos_queue_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.MAX_BANDWIDTH) is not None:
            obj_0.set_max_bandwidth(prop_diff.get(self.MAX_BANDWIDTH))
        if prop_diff.get(self.QOS_QUEUE_IDENTIFIER) is not None:
            obj_0.set_qos_queue_identifier(prop_diff.get(self.QOS_QUEUE_IDENTIFIER))
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
        if prop_diff.get(self.MIN_BANDWIDTH) is not None:
            obj_0.set_min_bandwidth(prop_diff.get(self.MIN_BANDWIDTH))

        try:
            self.vnc_lib().qos_queue_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().qos_queue_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('qos_queue %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().qos_queue_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::QosQueue': ContrailQosQueue,
    }
