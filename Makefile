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
