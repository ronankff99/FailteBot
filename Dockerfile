# # FROM ubuntu:18.04

# # ENTRYPOINT []

# # RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==1.10.2

# # ADD . /app/
# # RUN chmod +x /app/start_services.sh
# # CMD /app/start_services.sh

# # from rasa base image
# FROM rasa/rasa:1.10.2
# # copy all source and the Rasa generated model
# COPY . /app

# # inform which port will run on
# EXPOSE 5005

# # script to run rasa core
# COPY startup.sh /app/scripts/startup.sh
# # script to run rasa shell
# COPY shell.sh /app/scripts/shell.sh

# USER root
# RUN chmod a+x /app/scripts/startup.sh
# RUN chmod a+x /app/scripts/shell.sh

# WORKDIR /app

# ENTRYPOINT []
# ENV shell_mode false

# # launch script (rasa shell or rasa run)
# CMD sh -c 'if [ "$shell_mode" = false ]; then /app/scripts/startup.sh; else  /app/scripts/shell.sh; fi'

#Extend the official Rasa SDK image
FROM rasa/rasa-sdk:1.10.2

#Use subdirectory as working directory
WORKDIR /app

#Copy any additional custom requirements, if necessary (uncomment next line)
#COPY actions/requirements.txt ./

#Change back to root user to install dependencies
USER root

#Copy actions folder to working directory
COPY ./actions /app/actions

#Install extra requirements for actions code, if necessary (uncomment next line)
#RUN pip install -r requirements.txt

RUN /opt/venv/bin/python -m pip install --upgrade pip
#By best practices, don't run the code with root user
USER 1000