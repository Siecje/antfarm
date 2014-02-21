
'''
Helper for serving static content.

'''
from antfarm import response
import mimetypes

class ServeStatic(object):
    def __init__(self, root):
        self.root = root

    def __call__(self, path):
        full_path = os.path.absdir(os.path.join(self.root, path))
        if not full_path.startswith(self.root):
            return response.NotFound()

        # Guess content type
        content_type, encoding = mimetypes.guess_type(full_path)
        content_type = content_type or 'application/octet-stream'

        return response.Response(iter(open(full_path, 'rb')),
            content_type=content_type
        )
