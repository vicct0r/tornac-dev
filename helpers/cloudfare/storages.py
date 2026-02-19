from storages.backends.s3 import S3Storage

class MediaFileStorage(S3Storage):
    location = 'media'
    file_overwrite = False


class StaticFileStorage(S3Storage):
    location = 'static'
    file_overwrite = False