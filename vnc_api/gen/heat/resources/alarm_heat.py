
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


class ContrailAlarm(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, ALARM_SEVERITY, ALARM_RULES, ALARM_RULES_OR_LIST, ALARM_RULES_OR_LIST_AND_LIST, ALARM_RULES_OR_LIST_AND_LIST_OPERATION, ALARM_RULES_OR_LIST_AND_LIST_OPERAND1, ALARM_RULES_OR_LIST_AND_LIST_OPERAND2, ALARM_RULES_OR_LIST_AND_LIST_OPERAND2_UVE_ATTRIBUTE, ALARM_RULES_OR_LIST_AND_LIST_OPERAND2_JSON_VALUE, ALARM_RULES_OR_LIST_AND_LIST_VARIABLES, UVE_KEYS, UVE_KEYS_UVE_KEY, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, GLOBAL_SYSTEM_CONFIG, PROJECT
    ) = (
        'name', 'fq_name', 'display_name', 'alarm_severity', 'alarm_rules', 'alarm_rules_or_list', 'alarm_rules_or_list_and_list', 'alarm_rules_or_list_and_list_operation', 'alarm_rules_or_list_and_list_operand1', 'alarm_rules_or_list_and_list_operand2', 'alarm_rules_or_list_and_list_operand2_uve_attribute', 'alarm_rules_or_list_and_list_operand2_json_value', 'alarm_rules_or_list_and_list_variables', 'uve_keys', 'uve_keys_uve_key', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'global_system_config', 'project'
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
        ALARM_SEVERITY: properties.Schema(
            properties.Schema.INTEGER,
            _('ALARM_SEVERITY.'),
            update_allowed=True,
            required=False,
        ),
        ALARM_RULES: properties.Schema(
            properties.Schema.MAP,
            _('ALARM_RULES.'),
            update_allowed=True,
            required=False,
            schema={
                ALARM_RULES_OR_LIST: properties.Schema(
                    properties.Schema.LIST,
                    _('ALARM_RULES_OR_LIST.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            ALARM_RULES_OR_LIST_AND_LIST: properties.Schema(
                                properties.Schema.LIST,
                                _('ALARM_RULES_OR_LIST_AND_LIST.'),
                                update_allowed=True,
                                required=False,
                                schema=properties.Schema(
                                    properties.Schema.MAP,
                                    schema={
                                        ALARM_RULES_OR_LIST_AND_LIST_OPERATION: properties.Schema(
                                            properties.Schema.STRING,
                                            _('ALARM_RULES_OR_LIST_AND_LIST_OPERATION.'),
                                            update_allowed=True,
                                            required=False,
                                            constraints=[
                                                constraints.AllowedValues([u'==', u'!=', u'<', u'<=', u'>', u'>=', u'in', u'not in', u'range', u'size==', u'size!=']),
                                            ],
                                        ),
                                        ALARM_RULES_OR_LIST_AND_LIST_OPERAND1: properties.Schema(
                                            properties.Schema.STRING,
                                            _('ALARM_RULES_OR_LIST_AND_LIST_OPERAND1.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                        ALARM_RULES_OR_LIST_AND_LIST_OPERAND2: properties.Schema(
                                            properties.Schema.MAP,
                                            _('ALARM_RULES_OR_LIST_AND_LIST_OPERAND2.'),
                                            update_allowed=True,
                                            required=False,
                                            schema={
                                                ALARM_RULES_OR_LIST_AND_LIST_OPERAND2_UVE_ATTRIBUTE: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('ALARM_RULES_OR_LIST_AND_LIST_OPERAND2_UVE_ATTRIBUTE.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                                ALARM_RULES_OR_LIST_AND_LIST_OPERAND2_JSON_VALUE: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('ALARM_RULES_OR_LIST_AND_LIST_OPERAND2_JSON_VALUE.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                            }
                                        ),
                                        ALARM_RULES_OR_LIST_AND_LIST_VARIABLES: properties.Schema(
                                            properties.Schema.LIST,
                                            _('ALARM_RULES_OR_LIST_AND_LIST_VARIABLES.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                    }
                                )
                            ),
                        }
                    )
                ),
            }
        ),
        UVE_KEYS: properties.Schema(
            properties.Schema.MAP,
            _('UVE_KEYS.'),
            update_allowed=True,
            required=False,
            schema={
                UVE_KEYS_UVE_KEY: properties.Schema(
                    properties.Schema.LIST,
                    _('UVE_KEYS_UVE_KEY.'),
                    update_allowed=True,
                    required=False,
                ),
            }
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
        GLOBAL_SYSTEM_CONFIG: properties.Schema(
            properties.Schema.STRING,
            _('GLOBAL_SYSTEM_CONFIG.'),
            update_allowed=True,
            required=False,
        ),
        PROJECT: properties.Schema(
            properties.Schema.STRING,
            _('PROJECT.'),
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
        ALARM_SEVERITY: attributes.Schema(
            _('ALARM_SEVERITY.'),
        ),
        ALARM_RULES: attributes.Schema(
            _('ALARM_RULES.'),
        ),
        UVE_KEYS: attributes.Schema(
            _('UVE_KEYS.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        GLOBAL_SYSTEM_CONFIG: attributes.Schema(
            _('GLOBAL_SYSTEM_CONFIG.'),
        ),
        PROJECT: attributes.Schema(
            _('PROJECT.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.GLOBAL_SYSTEM_CONFIG):
            try:
                parent_obj = self.vnc_lib().global_system_config_read(id=self.properties.get(self.GLOBAL_SYSTEM_CONFIG))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().global_system_config_read(fq_name_str=self.properties.get(self.GLOBAL_SYSTEM_CONFIG))
            except:
                parent_obj = None
        if parent_obj is None and self.properties.get(self.PROJECT):
            try:
                parent_obj = self.vnc_lib().project_read(id=self.properties.get(self.PROJECT))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().project_read(fq_name_str=self.properties.get(self.PROJECT))
            except:
                parent_obj = None

        if parent_obj is None:
            tenant_id = self.stack.context.tenant_id
            parent_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.Alarm(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.ALARM_SEVERITY) is not None:
            obj_0.set_alarm_severity(self.properties.get(self.ALARM_SEVERITY))
        if self.properties.get(self.ALARM_RULES) is not None:
            obj_1 = vnc_api.AlarmOrList()
            if self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST) is not None:
                for index_1 in range(len(self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST))):
                    obj_2 = vnc_api.AlarmAndList()
                    if self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST) is not None:
                        for index_2 in range(len(self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST))):
                            obj_3 = vnc_api.AlarmExpression()
                            if self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERATION) is not None:
                                obj_3.set_operation(self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERATION))
                            if self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND1) is not None:
                                obj_3.set_operand1(self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND1))
                            if self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2) is not None:
                                obj_4 = vnc_api.AlarmOperand2()
                                if self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2, {}).get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2_UVE_ATTRIBUTE) is not None:
                                    obj_4.set_uve_attribute(self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2, {}).get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2_UVE_ATTRIBUTE))
                                if self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2, {}).get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2_JSON_VALUE) is not None:
                                    obj_4.set_json_value(self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2, {}).get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2_JSON_VALUE))
                                obj_3.set_operand2(obj_4)
                            if self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_VARIABLES) is not None:
                                for index_3 in range(len(self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_VARIABLES))):
                                    obj_3.add_variables(self.properties.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_VARIABLES)[index_3])
                            obj_2.add_and_list(obj_3)
                    obj_1.add_or_list(obj_2)
            obj_0.set_alarm_rules(obj_1)
        if self.properties.get(self.UVE_KEYS) is not None:
            obj_1 = vnc_api.UveKeysType()
            if self.properties.get(self.UVE_KEYS, {}).get(self.UVE_KEYS_UVE_KEY) is not None:
                for index_1 in range(len(self.properties.get(self.UVE_KEYS, {}).get(self.UVE_KEYS_UVE_KEY))):
                    obj_1.add_uve_key(self.properties.get(self.UVE_KEYS, {}).get(self.UVE_KEYS_UVE_KEY)[index_1])
            obj_0.set_uve_keys(obj_1)
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
            obj_uuid = super(ContrailAlarm, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().alarm_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.ALARM_SEVERITY) is not None:
            obj_0.set_alarm_severity(prop_diff.get(self.ALARM_SEVERITY))
        if prop_diff.get(self.ALARM_RULES) is not None:
            obj_1 = vnc_api.AlarmOrList()
            if prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST) is not None:
                for index_1 in range(len(prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST))):
                    obj_2 = vnc_api.AlarmAndList()
                    if prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST) is not None:
                        for index_2 in range(len(prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST))):
                            obj_3 = vnc_api.AlarmExpression()
                            if prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERATION) is not None:
                                obj_3.set_operation(prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERATION))
                            if prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND1) is not None:
                                obj_3.set_operand1(prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND1))
                            if prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2) is not None:
                                obj_4 = vnc_api.AlarmOperand2()
                                if prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2, {}).get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2_UVE_ATTRIBUTE) is not None:
                                    obj_4.set_uve_attribute(prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2, {}).get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2_UVE_ATTRIBUTE))
                                if prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2, {}).get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2_JSON_VALUE) is not None:
                                    obj_4.set_json_value(prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2, {}).get(self.ALARM_RULES_OR_LIST_AND_LIST_OPERAND2_JSON_VALUE))
                                obj_3.set_operand2(obj_4)
                            if prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_VARIABLES) is not None:
                                for index_3 in range(len(prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_VARIABLES))):
                                    obj_3.add_variables(prop_diff.get(self.ALARM_RULES, {}).get(self.ALARM_RULES_OR_LIST, {})[index_1].get(self.ALARM_RULES_OR_LIST_AND_LIST, {})[index_2].get(self.ALARM_RULES_OR_LIST_AND_LIST_VARIABLES)[index_3])
                            obj_2.add_and_list(obj_3)
                    obj_1.add_or_list(obj_2)
            obj_0.set_alarm_rules(obj_1)
        if prop_diff.get(self.UVE_KEYS) is not None:
            obj_1 = vnc_api.UveKeysType()
            if prop_diff.get(self.UVE_KEYS, {}).get(self.UVE_KEYS_UVE_KEY) is not None:
                for index_1 in range(len(prop_diff.get(self.UVE_KEYS, {}).get(self.UVE_KEYS_UVE_KEY))):
                    obj_1.add_uve_key(prop_diff.get(self.UVE_KEYS, {}).get(self.UVE_KEYS_UVE_KEY)[index_1])
            obj_0.set_uve_keys(obj_1)
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
            self.vnc_lib().alarm_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().alarm_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('alarm %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().alarm_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::Alarm': ContrailAlarm,
    }
