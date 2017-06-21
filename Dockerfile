FROM juniper/pyez

MAINTAINER Johannes Rueschel <code@rueschel.de>

RUN apk add --no-cache --update alpine-sdk libevent-dev linux-headers
RUN pip install --upgrade pip && git clone https://github.com/Juniper/py-space-platform.git && pip install ./py-space-platform && pip install jxmlease && pip install jupyter && pip install python-openstackclient && pip install python-keystoneclient && pip install python-heatclient && pip install python-novaclient && pip install python-glanceclient && pip install python-cinderclient && pip install python-swiftclient && pip install python-neutronclient

# clean up pip cache
RUN rm -rf ~/.cache/pip

RUN mkdir -p /notebooks /usr/lib/python2.7/site-packages/cfgm_common/ /usr/lib/python2.7/site-packages/vnc_api/

ADD jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py
ADD vnc_api /usr/lib/python2.7/site-packages/vnc_api/
ADD cfgm_common /usr/lib/python2.7/site-packages/cfgm_common/

EXPOSE 8888

#CMD ["/usr/bin/jupyter"]
ENTRYPOINT ["jupyter", "notebook", "--no-browser", "--allow-root"]
