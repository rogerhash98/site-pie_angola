---
title: View · product_pingwin_bo
drawer: views
source: app/views.py
updated: 2026-04-21T01:50:49
tags: [view, django]
---
# View · product_pingwin_bo

Função `product_pingwin_bo` definida em `app/views.py`.

## Descrição
_(sem docstring)_

## Código

```python
def product_pingwin_bo(request):
    return render(request, 'products/pingwin_bo.html', {'active_menu': 'products'})
```
