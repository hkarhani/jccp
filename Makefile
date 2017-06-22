build:
	docker build -t twofiveone/jccp .

run: stop
	mkdir -p notebooks
	docker run --name jccp \
		-v notebooks:/notebooks  \
		-e OS_AUTH_URL=http://198.18.148.124:5000/v2.0 \
		-e OS_TENANT_ID=01aa33baf27049e196f053504a5966ad \
		-e OS_TENANT_NAME="ApplicationOrchestration" \
		-e OS_USERNAME="admin" \
		-e OS_PASSWORD="contrail123" \
		-e OS_REGION_NAME="RegionOne" \
		-d \
		-p 8888:8888 \
		twofiveone/jccp

start:
	docker start jccp || true

sh: stop start
	docker exec -it jccp sh

rm: stop
	docker rm jccp || true

stop:
	docker stop jccp || true

update-vnc_api:
	curl -o vnc_api/vnc_api.py https://raw.githubusercontent.com/Juniper/contrail-controller/master/src/api-lib/vnc_api.py
	curl -o vnc_api/common/exceptions.py https://raw.githubusercontent.com/Juniper/contrail-controller/master/src/config/common/exceptions.py
	curl -o vnc_api/common/rest.py https://github.com/Juniper/contrail-controller/blob/master/src/config/common/rest.py
