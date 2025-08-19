{{ fullname | escape | underline}}

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__, __call__, __enter__, __exit__
   :exclude-members: __dict__, __weakref__, __module__, __annotations__

   {% if methods %}
   
   .. rubric:: Methods

   .. autosummary::
      :nosignatures:
      :toctree: .

      {% for item in methods %}
      ~{{ name }}.{{ item }}
      {%- endfor %}

   {% endif %}

   {% if attributes %}
   
   .. rubric:: Attributes

   .. autosummary::
      :toctree: .

      {% for item in attributes %}
      ~{{ name }}.{{ item }}
      {%- endfor %}

   {% endif %}

   {% if inherited_members %}
   
   .. rubric:: Inherited Members

   .. autosummary::
      :nosignatures:
      :toctree: .

      {% for item in inherited_members %}
      ~{{ name }}.{{ item }}
      {%- endfor %}

   {% endif %}