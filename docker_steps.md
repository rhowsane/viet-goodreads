# Steps used to publish the image on the Docker hub

To build the image Docker will interpret its name under tag -t and will look at the current directory for the Dockerfile:

1. sudo docker build -t viet-goodreads -f Dockerfile .  

Verify if the image was built:  
2. docker images  

To run the container it will be necessary to create a volume, which is persistant data generated and used by the docker container. So the test dataset will be placed on the internal port of the container /home/jovyan. The file to be run is the inference.py which uses the saved model and apply an inference to the test dataset. And display the metrics.  

3. sudo docker run -v ./test_df.csv:/home/jovyan/test_df.csv viet-goodreads python3 inference.py  

Login to the Docker Hub:

4. docker login

To tag the container:

5. sudo docker tag viet-goodreads name_of_account/viet-goodreads

Push the docker image:
 
5. sudo docker tag viet-goodreads name_of_account/viet-goodreads
