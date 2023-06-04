Python Sum
---

Source code pour l'article sur les orchestrateurs 

https://noether-blog.github.io/posts/Orchestrateur-cest-quoi/


# Setup

Lancez votre venv et installez le requirements.txt

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements
```

# Start application

Pour démarrer l'application lancez la commande suivante

```bash
python sum_api.py 
```
 
# Image docker

Pour construire une image docker de l'application

```bash
docker build python-sum-api:1.0.0 .
```

