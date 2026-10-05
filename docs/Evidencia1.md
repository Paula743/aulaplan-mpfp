# Evidencia 28 de Septiembre de 2026
María Paula Flores Prieto  
Lenguajes Modernos de Programación

## Código nuevo

### apps/api/src/http/routes_health.py

```python
from flask import Flask
from src.http.routes_health import health_bp

def test_health():
    app = create_app(testing=True)
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['runtime'] == 'python'

```

### apps/api/dev.py

```python
from src.http.app import create_app
 
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=8000)
```