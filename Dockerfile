FROM jupyter/scipy-notebook

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
	&& apt-get install -y \
		ca-certificates \
		git \
		gcc \
		make \
		libpcre3-dev \
		zlib1g-dev \
		libldap2-dev \
		libssl-dev \
		nano \
		net-tools \
		procps \
		gettext-base \
		jq \
		libirrlicht-dev \
		openssh-client \
        libsasl2-dev \
        xterm \
        sqlite3 \
        libsqlite3-dev

# install scipy-notebook "extensions"
USER $NB_USER
RUN cd ~

# iplantuml an UML drawing toolkit PyPDF2 docker python-ldap
# pixiedust used for pixiedebugger which only works in Classical Notebook so far
# caisrosvg: image utilities
RUN pip install iplantuml pixiedust cairosvg PyPDF2 pytube docker python-ldap
RUN pip install git+https://github.com/innovationOUtside/ipython_magic_tikz
RUN pip install --no-deps git+https://github.com/innovationOUtside/ipython_magic_eralchemy.git
RUN pip install git+https://github.com/psychemedia/eralchemy.git
RUN pip install git+https://github.com/b3b/ipython-restmagic
RUN pip install git+https://github.com/gbrault/ipython-sql.git
RUN pip install qgrid
RUN git clone --depth=1 https://github.com/gbrault/qgrid qgrid.git
RUN pip install jupyterlab_sql
RUN pip install pdfminer.six
RUN pip install bqplot==0.12.2

RUN conda install --quiet --yes \
     'python-pptx'

RUN conda install --quiet --yes -c anaconda \
     'netcdf4' \
     'pandas-datareader' \
     'memory_profiler' \
     'line_profiler' \
     'graphviz' \
     'python-graphviz' \
     'openpyxl'

RUN conda install --quiet --yes -c conda-forge \
     'voila' \
     'version_information' \
     'wikipedia' \
     'sparqlwrapper' \
     'imagemagick' \
     'ipysheet'

RUN conda install --quiet --yes -c bokeh jupyter_bokeh

RUN conda install --quiet --yes -c phlya adjusttext

RUN jupyter labextension install --no-build @jupyter-widgets/jupyterlab-manager
RUN jupyter labextension install --no-build qgrid.git/js/
RUN jupyter labextension install --no-build ipysheet
RUN jupyter labextension install --no-build jupyterlab-drawio
RUN jupyter labextension install --no-build @jupyterlab/toc
RUN jupyter labextension install --no-build @lckr/jupyterlab_variableinspector
RUN jupyter labextension install --no-build @jupyter-voila/jupyterlab-preview
RUN jupyter serverextension enable jupyterlab_sql --py --sys-prefix
RUN jupyter labextension install --no-build bqplot@0.5.2
RUN jupyter labextension uninstall --no-build jupyterlab_bokeh
RUN jupyter labextension install --no-build @bokeh/jupyter_bokeh
RUN pip install --upgrade jupyterlab-git
RUN jupyter lab build --minimize=False --dev-build=False
     
RUN conda clean --all -f -y
