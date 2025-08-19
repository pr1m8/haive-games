{# Enhanced AutoAPI module template with better summaries and Pydantic/Enum support #}
{% if not obj.display %}
:orphan:

{% endif %}
{% set display_name = obj.name.split('.')[-1] %}
{{ display_name }}
{{ "=" * display_name|length }}

.. py:module:: {{ obj.name }}

{% if obj.docstring %}
.. autoapi-nested-parse::

   {{ obj.docstring|indent(3) }}

{% endif %}

{% block summary %}
{% set visible_children = obj.children|selectattr("display")|list %}
{% if visible_children %}

Module Summary
--------------

.. autosummary::
   :nosignatures:
   :toctree: _autosummary
   :template: custom-module-summary.rst

   {% for child in visible_children %}
   {{ child.name }}
   {%- endfor %}

{% endif %}
{% endblock %}

{% block subpackages %}
{% set visible_subpackages = obj.subpackages|selectattr("display")|list %}
{% if visible_subpackages %}

Subpackages
-----------

.. toctree::
   :maxdepth: 1

{% for subpackage in visible_subpackages %}
   {{ subpackage.short_name }} <{{ subpackage.short_name }}/index>
{% endfor %}

{% endif %}
{% endblock %}

{% block submodules %}
{% set visible_submodules = obj.submodules|selectattr("display")|list %}
{% if visible_submodules %}

Submodules
----------

.. toctree::
   :maxdepth: 1

{% for submodule in visible_submodules %}
   {{ submodule.short_name }} <{{ submodule.short_name }}/index>
{% endfor %}

{% endif %}
{% endblock %}

{% block classes %}
{% set visible_classes = obj.classes|selectattr("display")|list %}
{% if visible_classes %}

Classes
-------

{% for class in visible_classes %}

.. autoclass:: {{ class.name }}
   :members:
   :show-inheritance:
   :inherited-members:
   :special-members: __init__, __call__
   
   {% if class.bases %}
   .. rubric:: Inheritance
   
   .. inheritance-diagram:: {{ class.name }}
      :parts: 1
   {% endif %}
   
   {% if class.obj.type == "pydantic_model" %}
   .. autopydantic_model:: {{ class.name }}
      :model-show-json: True
      :model-show-field-summary: True
      :model-show-validator-members: True
      :field-list-validators: True
      :field-show-constraints: True
   {% endif %}

{% endfor %}
{% endif %}
{% endblock %}

{% block functions %}
{% set visible_functions = obj.functions|selectattr("display")|list %}
{% if visible_functions %}

Functions
---------

{% for function in visible_functions %}

.. autofunction:: {{ function.name }}

{% endfor %}
{% endif %}
{% endblock %}

{% block exceptions %}
{% set visible_exceptions = obj.exceptions|selectattr("display")|list %}
{% if visible_exceptions %}

Exceptions
----------

{% for exception in visible_exceptions %}

.. autoexception:: {{ exception.name }}
   :members:
   :show-inheritance:

{% endfor %}
{% endif %}
{% endblock %}

{% block enums %}
{% set enums = obj.children|selectattr("type", "equalto", "enum")|selectattr("display")|list %}
{% if enums %}

Enumerations
------------

{% for enum in enums %}

.. autoenum:: {{ enum.name }}
   :members:
   :show-inheritance:
   :undoc-members:

{% endfor %}
{% endif %}
{% endblock %}

{% block attributes %}
{% set visible_attributes = obj.attributes|selectattr("display")|list %}
{% if visible_attributes %}

Module Attributes
-----------------

{% for attribute in visible_attributes %}

.. autodata:: {{ attribute.name }}
   :annotation:

   {{ attribute.docstring|indent(3) }}

{% endfor %}
{% endif %}
{% endblock %}