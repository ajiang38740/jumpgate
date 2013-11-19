from .endpoints.availability_zones import AvailabilityZonesV2
from .endpoints.extensions import ExtensionsV2
from .endpoints.extra_specs import ExtraSpecsFlavorV2
from .endpoints.dns import DNSDomainsV2, DNSDomainEntryV2
from .endpoints.flavors import (
    FlavorV2, FlavorsV2, FlavorsDetailV2)
from .endpoints.floating_ips import OSFloatingIpsV2
from .endpoints.keypairs import KeypairsV2, KeypairV2
from .endpoints.limits import LimitsV2
from .endpoints.quota_sets import OSQuotaSetsV2
from .endpoints.servers import (ServerV2, ServersV2,
                                ServersDetailV2,
                                ServerActionV2)
from .endpoints.security_groups import OSSecurityGroupsV2
from .endpoints.usage import UsageV2
from .endpoints.volumes import OSVolumeAttachmentsV2
from .endpoints.networks import OSNetworksV2, OSNetworkV2
from .endpoints.instance_actions import InstanceActionsV2


def setup(app, disp):
    # V2 Routes
    flavor = FlavorV2(app)
    flavors = FlavorsV2(app)
    flavors_detail = FlavorsDetailV2(app)

    disp.set_handler('v2_availability_zone', AvailabilityZonesV2())
    disp.set_handler('v2_availability_zone_detail', AvailabilityZonesV2())

    disp.set_handler('v2_extensions', ExtensionsV2())

    disp.set_handler('v2_os_extra_specs_flavor', ExtraSpecsFlavorV2())

    disp.set_handler('v2_flavor', flavor)
    disp.set_handler('v2_flavors', flavors)
    disp.set_handler('v2_flavors_detail', flavors_detail)

    disp.set_handler('v2_os_floating_ip_dns', DNSDomainsV2())
    disp.set_handler('v2_os_floating_ip_dns_domain_entry', DNSDomainEntryV2())

    disp.set_handler('v2_limits', LimitsV2())

    disp.set_handler('v2_os_floating_ips', OSFloatingIpsV2())

    disp.set_handler('v2_os_tenant_networks', OSNetworksV2())
    disp.set_handler('v2_os_tenant_network', OSNetworkV2())
    disp.set_handler('v2_os_networks', OSNetworksV2())
    disp.set_handler('v2_os_network', OSNetworkV2())

    disp.set_handler('v2_os_keypair', KeypairV2())
    disp.set_handler('v2_os_keypairs', KeypairsV2())

    disp.set_handler('v2_os_quota_sets', OSQuotaSetsV2())
    disp.set_handler('v2_os_tenant_quota_sets', OSQuotaSetsV2())

    disp.set_handler('v2_os_server_security_groups', OSSecurityGroupsV2())
    disp.set_handler('v2_os_security_groups', OSSecurityGroupsV2())

    disp.set_handler('v2_os_volume_attachments', OSVolumeAttachmentsV2())

    disp.set_handler('v2_server', ServerV2(app))
    disp.set_handler('v2_servers', ServersV2(app))
    disp.set_handler('v2_servers_detail', ServersDetailV2(app))
    disp.set_handler('v2_server_action', ServerActionV2(app))
    disp.set_handler('v2_os_instance_actions', InstanceActionsV2())

    disp.set_handler('v2_tenant_flavor', flavor)
    disp.set_handler('v2_tenant_flavors', flavors)
    disp.set_handler('v2_tenant_flavors_detail', flavors_detail)

    disp.set_handler('v2_tenant_usage', UsageV2())
