---
title: View · product_winrest_nx
drawer: views
source: app/views.py
updated: 2026-04-21T01:50:49
tags: [view, django]
---
# View · product_winrest_nx

Função `product_winrest_nx` definida em `app/views.py`.

## Descrição
_(sem docstring)_

## Código

```python
def product_winrest_nx(request):
    return render(request, 'products/winrest_nx.html', {'active_menu': 'products'})
```
