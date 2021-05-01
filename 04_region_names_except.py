import json
from pkg_resources import resource_filename

def get_region_name(region_code):

    endpoint_file = resource_filename('botocore', 'data/endpoints.json')

    with open(endpoint_file, 'r') as f:
        endpoint_data = json.load(f)

    try:
        region_name = endpoint_data['partitions'][0]['regions'][region_code]['description']

        region_name = region_name.replace('Europe', 'EU')

    except Exception as e:
        if region_code == 'ap-northeast-3':
            return 'Asia Pacific (Osaka)'
        
        raise e         # Raise an exception when the region_code cannot be found

    return region_name


if __name__ == "__main__":

    region_name = get_region_name('ap-northeast-3')

    print(region_name)