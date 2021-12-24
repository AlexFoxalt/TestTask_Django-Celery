import uuid


def generate_file_path(instance, filename) -> str:
    """
    Uploads file to:
    media/users_data/user_uuid/files/filename
    """
    user_uuid = instance.user.uuid
    return f"users_data/user_{user_uuid}/files/{filename}"


def generate_uuid():
    return uuid.uuid4()
