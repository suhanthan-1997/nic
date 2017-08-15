from pyramid.response import Response
from pyramid.view import view_config
from pyramid.renderers import render_to_response
import os
import uuid
import shutil


from sqlalchemy.exc import DBAPIError

from pyramid.httpexceptions import (
    HTTPForbidden,
    HTTPFound,
    HTTPNotFound,
    )
@view_config(route_name='home', renderer='../templates/p/im.pt')
def home(request):
    return{}

@view_config(route_name='h')
def h(request):
    # ``filename`` contains the name of the file in string format.
    #
    # WARNING: this example does not deal with the fact that IE sends an
    # absolute file *path* as the filename.  This example is naive; it
    # trusts user input.

    filename = request.POST['jpg'].filename

    # ``input_file`` contains the actual file data which needs to be
    # stored somewhere.

    input_file = request.POST['jpg'].file

    # Note that we are generating our own filename instead of trusting
    # the incoming filename since that might result in insecure paths.
    # Please note that in a real application you would not use /tmp,
    # and if you write to an untrusted location you will need to do
    # some extra work to prevent symlink attacks.

    file_path = os.path.join('/home', '%s.jpg' % uuid.uuid4())
    print (file_path)

    # We first write to a temporary file to prevent incomplete files from
    # being used.

    temp_file_path = file_path + '~'

    # Finally write the data to a temporary file
    input_file.seek(0)
    with open(temp_file_path, 'wb') as output_file:
        shutil.copyfileobj(input_file, output_file)

    # Now that we know the file has been fully saved to disk move it into place.

    os.rename(temp_file_path, file_path)

    return Response('OK')
	
