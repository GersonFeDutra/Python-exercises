# Use the official Anaconda3 base image
FROM continuumio/anaconda3:2024.10-1

# Set the working directory
WORKDIR /app

# Copy your project files into the container
COPY . /app

# Install additional packages if needed
#RUN conda install -y pandas matplotlib scikit-learn jupyterlab

# Expose the JupyterLab port
EXPOSE 8888

# Set the default command to run JupyterLab
CMD ["jupyter-lab", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
