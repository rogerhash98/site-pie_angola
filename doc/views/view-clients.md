---
title: View · clients
drawer: views
source: app/views.py
updated: 2026-04-21T01:50:49
tags: [view, django]
---
# View · clients

Função `clients` definida em `app/views.py`.

## Descrição
_(sem docstring)_

## Código

```python
def clients(request):
    return render(request, 'clients.html', {'active_menu': 'clients'})
```
