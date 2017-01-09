
import copy
import itertools


__all__ = ['list_opts']

_opts = [ 
    ('api', list(itertools.chain(
        devicedemo.api.app.api_opts,))),
]

def list_opts():
    return [(g, copy.deepcopy(o)) for g, o in _opts]
