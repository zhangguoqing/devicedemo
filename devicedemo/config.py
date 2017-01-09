
from oslo_config import cfg 
from oslo_db import options as db_options  # noqa
from oslo_messaging import opts  # noqa


state_opts = [ 
    cfg.StrOpt('backend',
               default='devicedemo',
               help='Backend for the state manager.'),
    cfg.StrOpt('basepath',
               default='/var/lib/devicedemo/states/',
               help='Storage directory for the file state backend.'), ]

cfg.CONF.register_opts(state_opts, 'state')

# oslo.db defaults
db_options.set_defaults(
    cfg.CONF,
    connection='sqlite:////var/lib/devicedemo/devicedemo.sqlite')
