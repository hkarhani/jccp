build:
	docker build -t twofiveone/jccp .

run: stop rm
	docker run --name jccp -d -p 8888:8888 twofiveone/jccp

bash: stop run
	docker exec -it jccp bash

rm:
	docker rm jccp || true

stop:
	docker stop jccp || true

update-vnc_api:
	curl -o vnc_api/vnc_api.py https://raw.githubusercontent.com/Juniper/contrail-controller/master/src/api-lib/vnc_api.py
	curl -o vnc_api/common/exceptions.py https://raw.githubusercontent.com/Juniper/contrail-controller/master/src/config/common/exceptions.py
	curl -o vnc_api/common/rest.py https://github.com/Juniper/contrail-controller/blob/master/src/config/common/rest.py
