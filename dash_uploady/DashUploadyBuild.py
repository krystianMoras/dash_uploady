# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashUploadyBuild(Component):
    """A DashUploadyBuild component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children of DashUploady.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- destination_url (string; optional)

- errors (list; optional)

- finished (boolean; default True)

- multiple (boolean; default False)

- progress (number; default 0)

- webkitdirectory (boolean; default False)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_uploady'
    _type = 'DashUploadyBuild'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, multiple=Component.UNDEFINED, progress=Component.UNDEFINED, webkitdirectory=Component.UNDEFINED, finished=Component.UNDEFINED, errors=Component.UNDEFINED, destination_url=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'destination_url', 'errors', 'finished', 'multiple', 'progress', 'webkitdirectory']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'destination_url', 'errors', 'finished', 'multiple', 'progress', 'webkitdirectory']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(DashUploadyBuild, self).__init__(children=children, **args)
