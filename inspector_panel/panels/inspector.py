from django.conf import settings
from django.template.loader import render_to_string
from debug_toolbar.panels import DebugPanel
from console_utils import console_debug
import inspect
try:
    import threading
except ImportError:
    threading = None

CONSTANT_ID = 1
RECORDS = {}


class DebugRecord(object):
    def __init__(self, *args, **kwargs):
        pass


def clear_record_for_current_thread():
    if threading is None:
        t_id = CONSTANT_ID
    else:
        t_id = threading.currentThread()
    RECORDS[t_id] = []


def get_record_for_current_thread():
    if threading is None:
        t_id = CONSTANT_ID
    else:
        t_id = threading.currentThread()
    if t_id not in RECORDS:
        RECORDS[t_id] = []
    return RECORDS[t_id]


def log_record(record):
    slot = get_record_for_current_thread()
    slot.append(record)


def debug_class(the_class, record):
    """ Adds class and module information
    """
    record.class_name = the_class.__name__
    record.docs = the_class.__doc__
    module = inspect.getmodule(the_class)
    debug_module(module, record)


def debug_module(module, record):
    import __builtin__
    record.source_file = "__builtin__"
    if module != __builtin__:
        record.source_file = inspect.getsourcefile(module)
    record.module_name = module.__name__


def debug_default(value, record):
    __class = value.__class__
    debug_class(__class, record)


def debug(value, console=True):
    if not hasattr(settings, 'DEBUG') or settings.DEBUG is False:
        return
    stack = inspect.stack()[1]
    frm = stack[0]
    print frm.f_locals
    record = DebugRecord()
    record.globals = frm.f_globals
    record.locals = frm.f_locals
    record.value = str(value)
    record.invoked = {}
    record.invoked['file'] = stack[1]
    record.invoked['line'] = stack[2]
    record.invoked['function'] = stack[3]

    if inspect.isclass(value):
        debug_class(value, record)
    elif inspect.ismodule(value):
        debug_module(value, record)
    else:
        debug_default(value, record)

    record.dir = dir(record)
    log_record(record)
    if console:
        console_debug(record)


class InspectorPanel(DebugPanel):

    name = 'InspectorPanel'
    template = 'inspector.html'
    has_content = True

    def __init__(self, *args, **kwargs):
        super(InspectorPanel, self).__init__(*args, **kwargs)
        clear_record_for_current_thread()

    def nav_title(self):
        return 'Inspector Panel'

    def nav_subtitle(self):
        records = get_record_for_current_thread()
        return "%s values to debug" % len(records)

    def title(self):
        return 'All values to debug'

    def url(self):
        return ''

    def content(self):

        context = self.context.copy()

        records = get_record_for_current_thread()
        context.update({
            'records': records,
            'count': len(records)
        })

        return render_to_string(self.template, context)
