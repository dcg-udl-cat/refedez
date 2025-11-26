# Requirements

## Network Infrastructure

ReFedEz requires your network infrastructure to be properly configured for federated learning deployments. If you are not running all services (servers and clients) on localhost, you must ensure the following:

- **Domain Name for the Server**: The federated learning server needs a resolvable domain name or IP address that all client machines can access. Clients must be able to ping the server to establish communication.
- **Network Accessibility**: Ensure there are no firewalls, VPN restrictions, or network segmentation blocking traffic between the server and clients on the required ports (typically SSH and any custom ports defined in your configuration).

## Remote Deployment

When using ReFedEz's remote deployment features, additional requirements apply:

- **SSH Access**: All target machines (servers and clients) must allow SSH connections from the machine running ReFedEz. This enables secure transfer of build artifacts and deployment scripts.
- **SSH Keys**: Set up passwordless SSH authentication using public/private key pairs for seamless automation. Ensure the SSH keys are properly configured and the remote machines trust the deploying machine.

## Architecture Compatibility

ReFedEz is currently tested and optimized for x86 architectures. While it may work on other architectures (such as ARM), compatibility is not guaranteed and has not been extensively validated. If you encounter issues on non-x86 systems, consider running ReFedEz on an x86 machine for deployment and orchestration.
