Automated Build of Docker Image twofiveone/jccp

Accelerates and simplifies CCP (Contrail Cloud Platform) APIs consumption, by offering a pre-bundled development environment with Juniper Contrail and OpenStack Python APIs client, including other Juniper automation Libraries (PyEZ / jxmlease / SpaceEZ), with Jupyter Notebook.

Built on top of juniper/pyez, with Alpine-SDK, PyEZ, jxmlease, SpaceEZ while adding Python client APIs for Contrail Cloud Platform (OpenStack + Contrail) - Including: Keystone (v2/v3), Nova, VNC_APIs, Heat, Glance / Swift / Cinder clients. Tutorial Notebooks around CCP APIs are being built which can be later pulled into this container.

Usage:
docker run --name jccp -d -p 8888:8888 twofiveone/jccp

Then browse to http://docker-machine-ip:8888/ to simply begin consuming / testing the APIs of your existing Contrail Cloud Platform Setup. Enjoy!


## Todo
- [x] update `cfgm_common`
- [x] update `gen` dir
