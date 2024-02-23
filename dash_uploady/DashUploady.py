from dash_uploady.DashUploadyBuild import DashUploadyBuild
from dash_uploady import settings
from dash_uploady.configure_upload import update_upload_api

def DashUploady(
        id,
        children=None,
        multiple=None,
        webkitdirectory=None,  
):
    destination_url = update_upload_api(settings.requests_pathname_prefix, settings.upload_api)

    return DashUploadyBuild(
        id=id,
        children=children,
        destination_url=destination_url,
        multiple=multiple,
        webkitdirectory=webkitdirectory,
    )