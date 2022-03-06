# SAT-solitaire


{% for image in rapport/jpg/ %}
 {% if image.path contains 'rapport/jpg/' %}
  ![image]({{ image.path }} 'image')
 {% endif %}
{% endfor %}

![Visualization of the codebase](./diagram.svg)


