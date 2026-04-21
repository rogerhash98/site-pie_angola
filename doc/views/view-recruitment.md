---
title: View · recruitment
drawer: views
source: app/views.py
updated: 2026-04-21T01:50:49
tags: [view, django]
---
# View · recruitment

Função `recruitment` definida em `app/views.py`.

## Descrição
_(sem docstring)_

## Código

```python
def recruitment(request):
    if request.method == 'POST':
        return redirect('contact_success')
    return render(request, 'recruitment.html', {'active_menu': 'recruitment'})
```
