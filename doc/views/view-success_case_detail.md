---
title: View · success_case_detail
drawer: views
source: app/views.py
updated: 2026-04-21T01:50:49
tags: [view, django]
---
# View · success_case_detail

Função `success_case_detail` definida em `app/views.py`.

## Descrição
_(sem docstring)_

## Código

```python
def success_case_detail(request, slug='h3-new-hamburgology'):
    return render(request, 'success_case_detail.html', {
        'active_menu': 'success_cases',
        'slug': slug,
    })
```
