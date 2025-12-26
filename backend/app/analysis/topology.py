def build_topology(data):
    """
    Build a simple VPC → Subnet topology graph
    compatible with the frontend visualizer.
    """

    nodes = []
    edges = []

    for account_id, regions in data.items():
        for region, services in regions.items():
            vpc_data = services.get("vpc")
            if not vpc_data:
                continue

            # VPC nodes
            for vpc in vpc_data.get("vpcs", []):
                nodes.append({
                    "id": vpc["VpcId"],
                    "label": vpc["VpcId"],
                    "account": account_id,
                    "region": region,
                    "type": "vpc"
                })

            # Subnet edges
            for subnet in vpc_data.get("subnets", []):
                edges.append({
                    "from": subnet["VpcId"],
                    "to": subnet["SubnetId"]
                })

    return {
        "nodes": nodes,
        "edges": edges
    }
