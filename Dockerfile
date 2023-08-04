# run in terminal docker build -t laughingrook:2023-SPR .
FROM jupyter/scipy-notebook:2023-05-30
# Install requirements
COPY --chown=${NB_UID}:${NB_GID} requirements.txt /tmp/
RUN pip install --no-cache-dir --requirement /tmp/requirements.txt && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"