apt-get update
apt-get -y install imagemagick

IMAGE_URL=$(curl http://metadata/computeMetadata/v1/instance/attributes/url -H "Metadata-Flavor: Google")
TEXT=$(curl http://metadata/computeMetadata/v1/instance/attributes/text -H "Metadata-Flavor: Google")
CS_BUCKET=$(curl http://metadata/computeMetadata/v1/instance/attributes/bucket -H "Metadata-Flavor: Google")

mkdir image-output
cd image-output
wget $IMAGE_URL
convert * -pointsize 30 -fill white -stroke black -gravity center -annotate +10+40 "$TEXT" output.png

gsutil mb gs://$CS_BUCKET

gsutil cp -a public-read output.png gs://$CS_BUCKET/output.png

cd /image-output
sudo apt-get update
sudo apt-get install -y python3 python3-pip
# sudo gcloud config set project lab-5-254804
sudo gsutil cp -r gs://lab-5bucket/part3-inter .

cd part3-inter
sudo pip3 install --upgrade google-api-python-client

python3 part3.py
