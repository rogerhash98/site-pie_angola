---
title: View · solutions
drawer: views
source: app/views.py
updated: 2026-04-21T01:50:49
tags: [view, django]
---
# View · solutions

Função `solutions` definida em `app/views.py`.

## Descrição
_(sem docstring)_

## Código

```python
def solutions(request):
    return render(request, 'solutions.html', {'active_menu': 'solutions'})
```
