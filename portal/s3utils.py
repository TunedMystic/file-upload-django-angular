"""
Got this from: ://martinbrochhaus.com/s3.html

Custom S3 storage backends to store files in subfolders.
"""

from storages.backends.s3boto import S3BotoStorage

MediaRootS3BotoStorage = lambda: S3BotoStorage(location="sandeep")