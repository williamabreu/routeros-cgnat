from ipaddress import IPv4Address, IPv4Network


def split_subnet(network: IPv4Network, netmask: IPv4Address) -> list:
    """Splits an IPv4 network into a list of subnets according to given netmask.

    Args:
        network: IPv4 network that will be splitted.
        netmask: Netmask that resulted subnets will have.
    
    Returns: 
        Resulted subnets listing.

    Raises:
        ValueError: When netmask given is smaller than the source network.
    """

    if network.netmask > netmask:
        raise ValueError('Impossible splitting to a netmask smaller than itself')

    if network.netmask == netmask:
        return [network.exploded]
    else:
        branches = list(network.subnets())
        return split_subnet(branches[0], netmask) + split_subnet(branches[1], netmask)
