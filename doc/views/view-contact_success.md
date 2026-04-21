---
title: View · contact_success
drawer: views
source: app/views.py
updated: 2026-04-21T01:50:49
tags: [view, django]
---
# View · contact_success

Função `contact_success` definida em `app/views.py`.

## Descrição
_(sem docstring)_

## Código

```python
def contact_success(request):
    return render(request, 'contact_success.html', {'active_menu': 'contact'})
```
