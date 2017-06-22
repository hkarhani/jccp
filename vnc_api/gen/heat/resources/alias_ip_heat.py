
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


class ContrailAliasIp(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, ALIAS_IP_ADDRESS, ALIAS_IP_ADDRESS_FAMILY, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, PROJECT_REFS, VIRTUAL_MACHINE_INTERFACE_REFS, ALIAS_IP_POOL
    ) = (
        'name', 'fq_name', 'display_name', 'alias_ip_address', 'alias_ip_address_family', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'project_refs', 'virtual_machine_interface_refs', 'alias_ip_pool'
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
        ALIAS_IP_ADDRESS: properties.Schema(
            properties.Schema.STRING,
            _('ALIAS_IP_ADDRESS.'),
            update_allowed=True,
            required=False,
        ),
        ALIAS_IP_ADDRESS_FAMILY: properties.Schema(
            properties.Schema.STRING,
            _('ALIAS_IP_ADDRESS_FAMILY.'),
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
        PROJECT_REFS: properties.Schema(
            properties.Schema.LIST,
            _('PROJECT_REFS.'),
            update_allowed=True,
            required=False,
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
            update_allowed=True,
            required=False,
        ),
        ALIAS_IP_POOL: properties.Schema(
            properties.Schema.STRING,
            _('ALIAS_IP_POOL.'),
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
        ALIAS_IP_ADDRESS: attributes.Schema(
            _('ALIAS_IP_ADDRESS.'),
        ),
        ALIAS_IP_ADDRESS_FAMILY: attributes.Schema(
            _('ALIAS_IP_ADDRESS_FAMILY.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        PROJECT_REFS: attributes.Schema(
            _('PROJECT_REFS.'),
        ),
        VIRTUAL_MACHINE_INTERFACE_REFS: attributes.Schema(
            _('VIRTUAL_MACHINE_INTERFACE_REFS.'),
        ),
        ALIAS_IP_POOL: attributes.Schema(
            _('ALIAS_IP_POOL.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.ALIAS_IP_POOL):
            try:
                parent_obj = self.vnc_lib().alias_ip_pool_read(id=self.properties.get(self.ALIAS_IP_POOL))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().alias_ip_pool_read(fq_name_str=self.properties.get(self.ALIAS_IP_POOL))
            except:
                parent_obj = None

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.AliasIp(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.ALIAS_IP_ADDRESS) is not None:
            obj_0.set_alias_ip_address(self.properties.get(self.ALIAS_IP_ADDRESS))
        if self.properties.get(self.ALIAS_IP_ADDRESS_FAMILY) is not None:
            obj_0.set_alias_ip_address_family(self.properties.get(self.ALIAS_IP_ADDRESS_FAMILY))
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

        # reference to project_refs
        if self.properties.get(self.PROJECT_REFS):
            for index_0 in range(len(self.properties.get(self.PROJECT_REFS))):
                try:
                    ref_obj = self.vnc_lib().project_read(
                        id=self.properties.get(self.PROJECT_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().project_read(
                        fq_name_str=self.properties.get(self.PROJECT_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_project(ref_obj)

        # reference to virtual_machine_interface_refs
        if self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_REFS):
            for index_0 in range(len(self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_REFS))):
                try:
                    ref_obj = self.vnc_lib().virtual_machine_interface_read(
                        id=self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_machine_interface_read(
                        fq_name_str=self.properties.get(self.VIRTUAL_MACHINE_INTERFACE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_virtual_machine_interface(ref_obj)

        try:
            obj_uuid = super(ContrailAliasIp, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().alias_ip_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.ALIAS_IP_ADDRESS) is not None:
            obj_0.set_alias_ip_address(prop_diff.get(self.ALIAS_IP_ADDRESS))
        if prop_diff.get(self.ALIAS_IP_ADDRESS_FAMILY) is not None:
            obj_0.set_alias_ip_address_family(prop_diff.get(self.ALIAS_IP_ADDRESS_FAMILY))
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

        # reference to project_refs
        ref_obj_list = []
        if self.PROJECT_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.PROJECT_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().project_read(
                        id=prop_diff.get(self.PROJECT_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().project_read(
                        fq_name_str=prop_diff.get(self.PROJECT_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_project_list(ref_obj_list)
            # End: reference to project_refs

        # reference to virtual_machine_interface_refs
        ref_obj_list = []
        if self.VIRTUAL_MACHINE_INTERFACE_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().virtual_machine_interface_read(
                        id=prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_machine_interface_read(
                        fq_name_str=prop_diff.get(self.VIRTUAL_MACHINE_INTERFACE_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_virtual_machine_interface_list(ref_obj_list)
            # End: reference to virtual_machine_interface_refs

        try:
            self.vnc_lib().alias_ip_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().alias_ip_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('alias_ip %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().alias_ip_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::AliasIp': ContrailAliasIp,
    }