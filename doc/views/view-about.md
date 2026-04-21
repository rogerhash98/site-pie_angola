---
title: View · about
drawer: views
source: app/views.py
updated: 2026-04-21T01:50:49
tags: [view, django]
---
# View · about

Função `about` definida em `app/views.py`.

## Descrição
_(sem docstring)_

## Código

```python
def about(request):
    return render(request, 'about.html', {'active_menu': 'about'})
```
