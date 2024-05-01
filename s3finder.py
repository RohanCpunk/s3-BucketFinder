#RohanCpunk
import boto3

def find_world_editable_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    for bucket in response['Bucket']:
        bucket_name = bucket['Name']
        try:
            acl = s3.get_bucket_acl(Bucket=bucket_name)
            for grant in acl['Grant']:
                if 'URI' in grant['Grantee'] and grant['Grantee']['URI'] == 'http://acs.amazonaws.com/groups/global/AllUsers':
                    print(f"Bucket '{bucket_name}' is world-readable.")
        except Exception as e:
            print(f"Error checking bucket '{bucket_name}':{e}")

if __name__ == "__main__":
    find_world_editable_buckets()
