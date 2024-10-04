import boto3
import os
import yaml



def main():
  print("Hello, World!")

def sync(local_directory, bucket_name):
  def sync():
    s3 = boto3.client('s3')
    bucket_name = 'your-bucket-name'
    local_directory = 'your-local-directory'

    for root, dirs, files in os.walk(local_directory):
      for file in files:
        local_path = os.path.join(root, file)
        relative_path = os.path.relpath(local_path, local_directory)
        s3_path = relative_path.replace("\\", "/")

        s3.upload_file(local_path, bucket_name, s3_path)

def load_config(file_path):
  with open(file_path, 'r') as config_file:
    config = yaml.safe_load(config_file)
  return config

if __name__ == "__main__":
  config = load_config('config.yml')
  main()