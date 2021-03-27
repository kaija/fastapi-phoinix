REPO=docker.trendops.co
IMG=phoinix
TAG=latest

all: build

build:
	docker build -t ${REPO}/${IMG}:${TAG} .

run:
	docker run -d --env-file .env -p 8000:8000 --name ${IMG} ${REPO}/${IMG}:${TAG}

stop:
	docker stop ${IMG}
	docker rm ${IMG}
