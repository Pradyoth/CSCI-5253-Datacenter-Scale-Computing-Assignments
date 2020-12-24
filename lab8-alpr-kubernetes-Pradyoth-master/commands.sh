
docker run -d --name redis -p 6379:6379 redis
kubectl create deployment redis-deployment --image=redis:latest
kubectl get pods
kubectl expose deployment redis-deployment --port 6379 --target-port 6379

docker run -d --name rabbitmq -p 5672:5672 redis
kubectl create deployment rabbitmq-deployment --image=rabbitmq:latest
kubectl expose deployment rabbitmq-deployment --port 5672 --target-port 5672

docker build -t gcr.io/datacenter5/rest-app:v1 .
docker push gcr.io/datacenter5/rest-app:v1
docker run --rm gcr.io/datacenter5/rest-app:v1
kubectl create deployment rest-deployment --image=gcr.io/datacenter5/rest-app:v1
kubectl expose deployment rest-deployment --port 5000 --target-port 5000


docker build -t gcr.io/datacenter5/worker-app:v1 .
docker push gcr.io/datacenter5/worker-app:v1
docker run --rm gcr.io/datacenter5/worker-app:v1
kubectl create deployment worker-deployment --image=gcr.io/datacenter5/worker-app:v1
kubectl expose deployment worker-deployment --image=gcr.io/datacenter5/worker-app:v1


