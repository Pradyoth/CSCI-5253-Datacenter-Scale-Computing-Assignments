sudo apt update
sudo apt install -y redis-server
sudo echo "protected-mode no" >> /etc/redis/redis.conf
sudo systemctl restart redis-server

