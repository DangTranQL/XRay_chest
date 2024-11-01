.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/chest.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/chest
    .. image:: https://readthedocs.org/projects/chest/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://chest.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/chest/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/chest
    .. image:: https://img.shields.io/pypi/v/chest.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/chest/
    .. image:: https://img.shields.io/conda/vn/conda-forge/chest.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/chest
    .. image:: https://pepy.tech/badge/chest/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/chest
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/chest

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

=====
X-Ray Chest Pneumonia
=====


X-ray scans segmentation model for chest pneumonia    

The dataset contains 3 folders: train, val, test with each folder has 2 subfolders: NORMAL and PNEUMONIA. All X-Ray scans are .jpeg images

train: 1341 NORMAL and 3875 PNEUMONIA

val: 8 NORMAL and 8 PNEUMONIA

test: 234 NORMAL and 390 PNEUMONIA

.. _pyscaffold-notes:

Note
====

Set up an environment, and to install all packages: **pip install -r requirements.txt**

Data visualization can be found at *src/data_visualization.ipynb*

For interactive plot, do: **panel serve src\interactive_plot.py --dev**