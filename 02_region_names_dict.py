import json
from pkg_resources import resource_filename

def get_region_code_name_dict():

    endpoint_file = resource_filename('botocore', 'data/endpoints.json')

    with open(endpoint_file, 'r') as f:
        data = json.load(f)

    regions = data['partitions'][0]['regions']

    region_code_name_dict = {}

    for region_code in regions.keys():
        region_code_name_dict[region_code] = regions[region_code]['description']

    return region_code_name_dict


if __name__ == "__main__":
    
    # regions_code_name_dict is a dictionary that has the region_code as the key and the region_name as the value
    regions_code_name_dict = get_region_code_name_dict()

    region_code = 'us-east-1'
    region_name = regions_code_name_dict[region_code]
    print(region_name)

    region_code = 'ap-southeast-2'
    region_name = regions_code_name_dict[region_code]
    print(region_name)

    region_code = 'eu-central-1'
    region_name = regions_code_name_dict[region_code]
    print(region_name)