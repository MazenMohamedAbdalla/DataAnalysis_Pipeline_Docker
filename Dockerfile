FROM ubuntu

# Install Python3 and necessary dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Install the required packages
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1

# Copy the dataset file to the container
COPY dataset.csv /home/doc-bd-a1/

# Start a bash shell upon container startup
CMD ["bash"]
