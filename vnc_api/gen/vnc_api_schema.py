
# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

import pydot

def generate_schema_graph():
    graph = pydot.Dot(graph_type='digraph')

    # Generate node definitions and add to graph
    domain_node = pydot.Node('domain')
    graph.add_node(domain_node)
    global_vrouter_config_node = pydot.Node('global-vrouter-config')
    graph.add_node(global_vrouter_config_node)
    instance_ip_node = pydot.Node('instance-ip')
    graph.add_node(instance_ip_node)
    network_policy_node = pydot.Node('network-policy')
    graph.add_node(network_policy_node)
    loadbalancer_pool_node = pydot.Node('loadbalancer-pool')
    graph.add_node(loadbalancer_pool_node)
    virtual_DNS_record_node = pydot.Node('virtual-DNS-record')
    graph.add_node(virtual_DNS_record_node)
    route_target_node = pydot.Node('route-target')
    graph.add_node(route_target_node)
    floating_ip_node = pydot.Node('floating-ip')
    graph.add_node(floating_ip_node)
    floating_ip_pool_node = pydot.Node('floating-ip-pool')
    graph.add_node(floating_ip_pool_node)
    physical_router_node = pydot.Node('physical-router')
    graph.add_node(physical_router_node)
    bgp_router_node = pydot.Node('bgp-router')
    graph.add_node(bgp_router_node)
    virtual_router_node = pydot.Node('virtual-router')
    graph.add_node(virtual_router_node)
    config_root_node = pydot.Node('config-root')
    graph.add_node(config_root_node)
    subnet_node = pydot.Node('subnet')
    graph.add_node(subnet_node)
    global_system_config_node = pydot.Node('global-system-config')
    graph.add_node(global_system_config_node)
    service_appliance_node = pydot.Node('service-appliance')
    graph.add_node(service_appliance_node)
    service_instance_node = pydot.Node('service-instance')
    graph.add_node(service_instance_node)
    namespace_node = pydot.Node('namespace')
    graph.add_node(namespace_node)
    logical_interface_node = pydot.Node('logical-interface')
    graph.add_node(logical_interface_node)
    route_table_node = pydot.Node('route-table')
    graph.add_node(route_table_node)
    physical_interface_node = pydot.Node('physical-interface')
    graph.add_node(physical_interface_node)
    access_control_list_node = pydot.Node('access-control-list')
    graph.add_node(access_control_list_node)
    analytics_node_node = pydot.Node('analytics-node')
    graph.add_node(analytics_node_node)
    virtual_DNS_node = pydot.Node('virtual-DNS')
    graph.add_node(virtual_DNS_node)
    customer_attachment_node = pydot.Node('customer-attachment')
    graph.add_node(customer_attachment_node)
    service_appliance_set_node = pydot.Node('service-appliance-set')
    graph.add_node(service_appliance_set_node)
    config_node_node = pydot.Node('config-node')
    graph.add_node(config_node_node)
    qos_queue_node = pydot.Node('qos-queue')
    graph.add_node(qos_queue_node)
    virtual_machine_node = pydot.Node('virtual-machine')
    graph.add_node(virtual_machine_node)
    interface_route_table_node = pydot.Node('interface-route-table')
    graph.add_node(interface_route_table_node)
    service_template_node = pydot.Node('service-template')
    graph.add_node(service_template_node)
    virtual_ip_node = pydot.Node('virtual-ip')
    graph.add_node(virtual_ip_node)
    loadbalancer_member_node = pydot.Node('loadbalancer-member')
    graph.add_node(loadbalancer_member_node)
    security_group_node = pydot.Node('security-group')
    graph.add_node(security_group_node)
    provider_attachment_node = pydot.Node('provider-attachment')
    graph.add_node(provider_attachment_node)
    virtual_machine_interface_node = pydot.Node('virtual-machine-interface')
    graph.add_node(virtual_machine_interface_node)
    loadbalancer_healthmonitor_node = pydot.Node('loadbalancer-healthmonitor')
    graph.add_node(loadbalancer_healthmonitor_node)
    virtual_network_node = pydot.Node('virtual-network')
    graph.add_node(virtual_network_node)
    project_node = pydot.Node('project')
    graph.add_node(project_node)
    qos_forwarding_class_node = pydot.Node('qos-forwarding-class')
    graph.add_node(qos_forwarding_class_node)
    database_node_node = pydot.Node('database-node')
    graph.add_node(database_node_node)
    routing_instance_node = pydot.Node('routing-instance')
    graph.add_node(routing_instance_node)
    network_ipam_node = pydot.Node('network-ipam')
    graph.add_node(network_ipam_node)
    logical_router_node = pydot.Node('logical-router')
    graph.add_node(logical_router_node)

    # Generate edge definitions and add to graph
    graph.add_edge(pydot.Edge(domain_node, project_node, color = 'red'))
    graph.add_edge(pydot.Edge(domain_node, namespace_node, color = 'red'))
    graph.add_edge(pydot.Edge(domain_node, service_template_node, color = 'red'))
    graph.add_edge(pydot.Edge(domain_node, virtual_DNS_node, color = 'red'))
    graph.add_edge(pydot.Edge(instance_ip_node, virtual_network_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(instance_ip_node, virtual_machine_interface_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(loadbalancer_pool_node, service_instance_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(loadbalancer_pool_node, virtual_machine_interface_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(loadbalancer_pool_node, service_appliance_set_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(loadbalancer_pool_node, loadbalancer_member_node, color = 'red'))
    graph.add_edge(pydot.Edge(loadbalancer_pool_node, loadbalancer_healthmonitor_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(floating_ip_node, project_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(floating_ip_node, virtual_machine_interface_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(floating_ip_pool_node, floating_ip_node, color = 'red'))
    graph.add_edge(pydot.Edge(physical_router_node, virtual_router_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(physical_router_node, bgp_router_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(physical_router_node, virtual_network_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(physical_router_node, physical_interface_node, color = 'red'))
    graph.add_edge(pydot.Edge(physical_router_node, logical_interface_node, color = 'red'))
    graph.add_edge(pydot.Edge(bgp_router_node, bgp_router_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(virtual_router_node, bgp_router_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(virtual_router_node, virtual_machine_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(config_root_node, global_system_config_node, color = 'red'))
    graph.add_edge(pydot.Edge(config_root_node, domain_node, color = 'red'))
    graph.add_edge(pydot.Edge(subnet_node, virtual_machine_interface_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(global_system_config_node, bgp_router_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(global_system_config_node, global_vrouter_config_node, color = 'red'))
    graph.add_edge(pydot.Edge(global_system_config_node, physical_router_node, color = 'red'))
    graph.add_edge(pydot.Edge(global_system_config_node, virtual_router_node, color = 'red'))
    graph.add_edge(pydot.Edge(global_system_config_node, config_node_node, color = 'red'))
    graph.add_edge(pydot.Edge(global_system_config_node, analytics_node_node, color = 'red'))
    graph.add_edge(pydot.Edge(global_system_config_node, database_node_node, color = 'red'))
    graph.add_edge(pydot.Edge(global_system_config_node, service_appliance_set_node, color = 'red'))
    graph.add_edge(pydot.Edge(service_instance_node, service_template_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(logical_interface_node, virtual_machine_interface_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(physical_interface_node, logical_interface_node, color = 'red'))
    graph.add_edge(pydot.Edge(virtual_DNS_node, virtual_DNS_record_node, color = 'red'))
    graph.add_edge(pydot.Edge(customer_attachment_node, virtual_machine_interface_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(customer_attachment_node, floating_ip_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(service_appliance_set_node, service_appliance_node, color = 'red'))
    graph.add_edge(pydot.Edge(virtual_machine_node, virtual_machine_interface_node, color = 'red'))
    graph.add_edge(pydot.Edge(virtual_machine_node, service_instance_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(virtual_ip_node, loadbalancer_pool_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(virtual_ip_node, virtual_machine_interface_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(security_group_node, access_control_list_node, color = 'red'))
    graph.add_edge(pydot.Edge(provider_attachment_node, virtual_router_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(virtual_machine_interface_node, qos_forwarding_class_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(virtual_machine_interface_node, security_group_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(virtual_machine_interface_node, virtual_machine_interface_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(virtual_machine_interface_node, virtual_machine_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(virtual_machine_interface_node, virtual_network_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(virtual_machine_interface_node, routing_instance_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(virtual_machine_interface_node, interface_route_table_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(virtual_network_node, qos_forwarding_class_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(virtual_network_node, network_ipam_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(virtual_network_node, network_policy_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(virtual_network_node, access_control_list_node, color = 'red'))
    graph.add_edge(pydot.Edge(virtual_network_node, floating_ip_pool_node, color = 'red'))
    graph.add_edge(pydot.Edge(virtual_network_node, routing_instance_node, color = 'red'))
    graph.add_edge(pydot.Edge(virtual_network_node, route_table_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(project_node, namespace_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(project_node, security_group_node, color = 'red'))
    graph.add_edge(pydot.Edge(project_node, virtual_network_node, color = 'red'))
    graph.add_edge(pydot.Edge(project_node, qos_queue_node, color = 'red'))
    graph.add_edge(pydot.Edge(project_node, qos_forwarding_class_node, color = 'red'))
    graph.add_edge(pydot.Edge(project_node, network_ipam_node, color = 'red'))
    graph.add_edge(pydot.Edge(project_node, network_policy_node, color = 'red'))
    graph.add_edge(pydot.Edge(project_node, virtual_machine_interface_node, color = 'red'))
    graph.add_edge(pydot.Edge(project_node, floating_ip_pool_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(project_node, service_instance_node, color = 'red'))
    graph.add_edge(pydot.Edge(project_node, route_table_node, color = 'red'))
    graph.add_edge(pydot.Edge(project_node, interface_route_table_node, color = 'red'))
    graph.add_edge(pydot.Edge(project_node, logical_router_node, color = 'red'))
    graph.add_edge(pydot.Edge(project_node, loadbalancer_pool_node, color = 'red'))
    graph.add_edge(pydot.Edge(project_node, loadbalancer_healthmonitor_node, color = 'red'))
    graph.add_edge(pydot.Edge(project_node, virtual_ip_node, color = 'red'))
    graph.add_edge(pydot.Edge(qos_forwarding_class_node, qos_queue_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(routing_instance_node, bgp_router_node, color = 'red'))
    graph.add_edge(pydot.Edge(routing_instance_node, routing_instance_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(routing_instance_node, route_target_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(network_ipam_node, virtual_DNS_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(logical_router_node, virtual_machine_interface_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(logical_router_node, route_target_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(logical_router_node, virtual_network_node, color = 'blue', constraint = False))
    graph.add_edge(pydot.Edge(logical_router_node, service_instance_node, color = 'blue', constraint = False))

    return graph
#end generate_schema_graph

def write_schema_graph(graph, filename):
    graph.write_xdot(filename)
#end write_schema_graph

