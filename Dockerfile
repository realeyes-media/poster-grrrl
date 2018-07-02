FROM quay.io/realeyes/alpine-node-python-yamltools:master

WORKDIR /app

COPY app-notify.py /opt/app-notify.py
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

ENV SLACK_WEBHOOK="https://hooks.slack.com/services/GETYOUROWNWEBHOOK"
ENV VERSION_NUMBER="0.0.0"
ENV PLAYER_NAME="Test Player"
ENV BITBUCKET_REPO_SLUG="repo-name"
ENV BITBUCKET_BUILD_NUMBER="000"
ENV SLACK_NOTIFICATION_TITLE="Test Notification"
ENV PLAYER_BASE="GETYOUROWN"
ENV PLAYER_END="GETYOUROWN"

CMD ["python","/opt/app-notify.py","--help"]
