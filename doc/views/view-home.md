---
title: View · home
drawer: views
source: app/views.py
updated: 2026-04-21T01:50:49
tags: [view, django]
---
# View · home

Função `home` definida em `app/views.py`.

## Descrição
_(sem docstring)_

## Código

```python
def home(request):
    return render(request, 'home.html', {'active_menu': 'solutions'})
```
