{{ fullname | escape | underline}}

.. currentmodule:: {{ module }}

.. automodule:: {{ fullname }}
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__, __call__
   :exclude-members: __dict__, __weakref__, __module__

{% if classes %}
Classes
-------

.. autosummary::
   :toctree: .
   :template: custom-class-template.rst
   :nosignatures:

   {% for item in classes %}
   {{ item }}
   {%- endfor %}

{% endif %}

{% if functions %}
Functions
---------

.. autosummary::
   :toctree: .
   :template: custom-function-template.rst
   :nosignatures:

   {% for item in functions %}
   {{ item }}
   {%- endfor %}

{% endif %}

{% if exceptions %}
Exceptions
----------

.. autosummary::
   :toctree: .
   :nosignatures:

   {% for item in exceptions %}
   {{ item }}
   {%- endfor %}

{% endif %}

{% if data %}
Module Attributes
-----------------

.. autosummary::
   :toctree: .

   {% for item in data %}
   {{ item }}
   {%- endfor %}

{% endif %}