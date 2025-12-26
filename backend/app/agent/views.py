def build_view(raw_data: dict, view: str):
    if view == "raw":
        return raw_data

    if view == "list":
        return build_list_view(raw_data)

    # default = filtered
    return build_filtered_view(raw_data)

def build_list_view(raw_data: dict):
    output = []

    for account, regions in raw_data.items():
        for region, services in regions.items():
            for service, resources in services.items():
                for resource_type, items in resources.items():
                    for item in items:
                        output.append({
                            "account": account,
                            "region": region,
                            "service": service,
                            "type": resource_type,
                            "id": extract_id(item)
                        })
    return output


def extract_id(item: dict):
    for key in ["InstanceId", "VpcId", "SubnetId", "GroupId", "DBInstanceIdentifier"]:
        if key in item:
            return item[key]
    return "unknown"

def build_filtered_view(raw_data: dict):
    filtered = {}

    for account, regions in raw_data.items():
        filtered[account] = {}

        for region, services in regions.items():
            filtered[account][region] = {}

            if "ec2" in services:
                filtered[account][region]["ec2"] = {
                    "instances": [
                        {
                            "id": i["InstanceId"],
                            "type": i["InstanceType"],
                            "state": i["State"]["Name"],
                            "vpc": i.get("VpcId"),
                            "subnet": i.get("SubnetId")
                        }
                        for i in services["ec2"].get("instances", [])
                    ]
                }

            if "vpc" in services:
                filtered[account][region]["vpc"] = {
                    "vpcs": [
                        {
                            "id": v["VpcId"],
                            "cidr": v["CidrBlock"],
                            "state": v["State"]
                        }
                        for v in services["vpc"].get("vpcs", [])
                    ]
                }

    return filtered
