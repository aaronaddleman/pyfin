# pyfin

python finance

## Running tests

```
python -m pytest -v
```

## Using jupyter

```
export PROJECT=$PWD

docker run -it \
-p 8888:8888 \
-e JUPYTER_ENABLE_LAB=yes \
-e USE_SSL=yes \
-e GEN_CERT=yes \
-v $PROJECTDIR:/home/jovyan/project \
jupyter/base-notebook
```

