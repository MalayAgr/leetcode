import os

DIFFICULTY_MAP = {"E": "easy", "M": "medium", "H": "hard"}

PY_FILE_DIR = "./src"

EXPLANATIONS_DIR = os.path.join(".", "docs", "explanations")

TEMPLATE = """---
layout: default
parent: Easy Problems
grand_parent: Explanations
has_toc: false
nav_order: {{ number }}
---

# <!-- omit in toc --> Problem {{ number }} - {{ name }}

> Leetcode Link: [{{ name }}]({{ link }}).

## Statement

## Examples
{% if n_solutions == 1 %}
## Solution

### Concept

### Example

### Time complexity
{% else %}{% for i in (1..n_solutions) %}
## Solution {{ i }}

### Concept

### Example

### Time complexity
{% endfor %}{% endif %}"""
