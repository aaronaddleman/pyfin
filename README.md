# pyfin

python finance

## Running tests

```
python -m pytest -v
```

## Using jupyter

```
docker run --rm -e JUPYTER_ENABLE_LAB=yes -e USE_SSL=yes -e GEN_CERT=yes -p 8888:8888 -v "$PWD":/home/jovyan/work jupyter/base-notebook
```
