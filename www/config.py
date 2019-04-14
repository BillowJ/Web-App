#PYthon 3.7
#Designed by LiJingJie

import config_default

class Dict(dict):

    def __init__(self,name=(),value=(),**kw):
        super(Dict,self).__init__(**kw)
        for k,v in zip(name,value):
            self[k] = v
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("Dict object has no attr %s" %key)
    def __setattr__(self, key, value):
        self[key] = value

def merge(defaults,overwrite):
    r = {}
    for k,v in defaults.items():
        if k in overwrite:
            if isinstance(k,dict):
                merge(v,overwrite[k])
            else:
                r[k] = overwrite[k]
        else:
            r[k] = v
    return r

def toDict(d):
    D = Dict()
    for k,v in d.items():
        D[k] = toDict(v) if isinstance(v,dict) else v
    return D
configs = config_default.configs
try:
    import configs_overwrite
    configs = merge(configs,config_over_write.configs)
except ImportError:
    pass

configs = toDict(configs)

