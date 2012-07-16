inspector-panel
===============

Inspector panel is intended to retrieve information about variables when developing Django applications.

The panel must be used with [django-debug-toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar).


### Installation

    $ pip install inspector_panel

Add the panel to the `DEBUG_TOOLBAR_PANELS` settings variable: 

    DEBUG_TOOLBAR_PANELS = (
        ...
        'inspector_panel.panels.inspector.InspectorPanel',
        ...
    )

Add `inspector_panel` to your `INSTALLED_APPS`