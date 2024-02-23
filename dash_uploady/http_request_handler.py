import logging
import pathlib
import traceback

from flask import request
from flask import abort


logger = logging.getLogger(__name__)


class HttpRequestHandler():
    # You may use the flask.request
    # and flask.session inside the methods of this
    # class when needed.
    def __init__(self, server, upload_folder, use_upload_id):
        """
        Parameters
        ----------
        server: flask.Flask
            The flask server instance
        upload_folder: str
            The folder to use for uploads
        use_upload_id: bool
            Determines if the uploads are put into
            folders defined by a "upload id" (upload_id).
            If True, uploads will be put into `folder`/<upload_id>/;
            that is, every user (for example with different
            session id) will use their own folder. If False,
            all files from all sessions are uploaded into
            same folder (not recommended).

        """
        self.server = server
        self.upload_folder = pathlib.Path(upload_folder)
        self.use_upload_id = use_upload_id

    def post(self):
        raise NotImplementedError()



    def get(self):
        raise NotImplementedError()
