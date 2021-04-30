import json
from pkg_resources import resource_filename

def get_region_name(region_code):

    endpoint_file = resource_filename('botocore', 'data/endpoints.json')

    with open(endpoint_file, 'r') as f:
        data = json.load(f)

    region_name = data['partitions'][0]['regions'][region_code]['description']

    return region_name


if __name__ == "__main__":
    # region_code = 'ap-south-1'

    # region_name = get_region_name(region_code)

    # print(region_name)

    import boto3

    ec2_client = boto3.client('ec2')

    response = ec2_client.describe_regions()

    regions = response['Regions']

    for region in regions:
        region_code = region['RegionName']

        region_name = get_region_name(region_code)

        print(region_code, '-', region_name)


        