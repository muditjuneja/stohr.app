# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install Node.js, npm and cron
RUN apt-get update && apt-get install -y curl cron supervisor && \
    curl -sL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# Verify that Node.js and npm were installed correctly
RUN node -v && npm -v

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Add the cron job file
ADD cronjob /etc/cron.d/cronjob
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cronjob
# Apply cron job
RUN crontab /etc/cron.d/cronjob
# Create the log file to be able to run tail
RUN touch /var/log/cron.log


COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]


# Change the working directory to /app/myfolder
WORKDIR /app/my-store

# Install Node.js modules
RUN npm install

WORKDIR /app/

# Make ports 80 and 8002 available to the world outside this container
EXPOSE 3000 8003

# Add supervisor configuration file
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]

#  start cron service and run the main.py script and also start the webserver powered by express
# CMD service cron start && python main.py && npm run serve