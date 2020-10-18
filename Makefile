build:
	docker-compose build

start: build
	docker-compose up -d --remove-orphans

stop:
	docker-compose down

logs:
	docker-compose logs
