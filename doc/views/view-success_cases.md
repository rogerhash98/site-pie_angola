---
title: View · success_cases
drawer: views
source: app/views.py
updated: 2026-04-21T01:50:49
tags: [view, django]
---
# View · success_cases

Função `success_cases` definida em `app/views.py`.

## Descrição
_(sem docstring)_

## Código

```python
def success_cases(request):
    return render(request, 'success_cases.html', {'active_menu': 'success_cases'})
```
