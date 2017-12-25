from openstack import profile
from openstack import connection
from openstack import exceptions
import functools
from oslo_log import log as logging

LOG = logging.getLogger(__name__)

auth_url='http://10.10.10.114:5000/v3'
region='RegionOne'
project_name='admin'
user_domain_name='Default'
project_domain_name='Default'
username='admin'
password='123'


class SenlinException(Exception):
    """Base Senlin Exception.

    To correctly use this class, inherit from it and define a 'msg_fmt'
    property. That msg_fmt will get printed with the keyword arguments
    provided to the constructor.
    """
    message = ("An unknown exception occurred.")

    def __init__(self, **kwargs):
        self.kwargs = kwargs

        try:
            self.message = self.msg_fmt % kwargs
            # if last char is '.', wipe out redundant '.'
            if self.message[-1] == '.':
                self.message = self.message.rstrip('.') + '.'
        except KeyError:
            # exc_info = sys.exc_info()
            # if kwargs doesn't match a variable in the message
            # log the issue and the kwargs
            LOG.exception('Exception in string format operation')
            for name, value in kwargs.items():
                LOG.error("%s: %s" % (name, value))  # noqa

            if _FATAL_EXCEPTION_FORMAT_ERRORS:
                raise
                # raise exc_info[0], exc_info[1], exc_info[2]

    def __str__(self):
        return six.text_type(self.message)

    def __unicode__(self):
        return six.text_type(self.message)

    def __deepcopy__(self, memo):
        return self.__class__(**self.kwargs)

class InternalError(SenlinException):
    """A base class for internal exceptions in senlin.

    The internal exception classes which inherit from :class:`SenlinException`
    class should be translated to a user facing exception type if need to be
    made user visible.
    """
    msg_fmt = ("%(message)s")
    message = ('Internal error happened')

    def __init__(self, **kwargs):
        self.code = kwargs.pop('code', 500)
        self.message = kwargs.pop('message', self.message)
        super(InternalError, self).__init__(
            code=self.code, message=self.message, **kwargs)

class ResourceNotFound(Exception):
    pass

class NotFoundException(Exception):
    pass


def translate_exception(func):
    """Decorator for exception translation."""

    @functools.wraps(func)
    def invoke_with_catch(driver, *args, **kwargs):
        try:
            return func(driver, *args, **kwargs)
        except Exception as ex:
            LOG.exception(ex)
            raise parse_exception(ex)

    return invoke_with_catch

def create_connection():
    prof = profile.Profile()
    prof.set_region(profile.Profile.ALL, region)
    conn = connection.Connection(profile=prof, auth_url=auth_url, project_name=project_name, username=username, password=password, user_domain_name=user_domain_name, project_domain_name=project_domain_name)
    return conn

conn = create_connection()


def list_server(conn):
    print "List server: "
    s1 = conn.compute.get_server('a8a7de59-a119-4b9b-abdb-143b18ea34fe')
    #s2 = conn.compute.get_server('ec4763c2-f62a-481e-92f7-78774cdd8cd6')
    #print s
    server1 = s1.to_dict()
    #server2 = s2.to_dict()
    print server1
    print '------------'
    #print server2
    print server1['image']
    #print server['image']
    #print server['attached_volumes']
    #print server['flavor']['id']
    #print s.attached_volumes['id']
    #print s.image

#list_server(conn)

def find_server(conn):
    print "find server:"
    res = conn.compute.get_server('51748b73-760e-43f6-ae5c-62398f22c7af')
    print res
    print res.id
    print res.image

#find_server(conn)

@translate_exception
def delete_server(conn):
    print "Delete server:"
    try:
        res = conn.compute.delete_server("cf1cc2ef-632a-48c2-a7a9-fe81cdf5ed16", force=True)
    # except exceptions.NotFoundException:
    except ResourceNotFound as ex:
        print ex
        print 'Use ResourceNotFound'
    except NotFoundException as ex:
        print 'Use NotFoundException'
    except InternalError as ex:
        print 'Use InterError'
    #except Exception as ex:
    #    print 'Use Exception'
    #    print ex

    #print res

delete_server(conn)



