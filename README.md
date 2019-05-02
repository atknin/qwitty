# qwitty


server {
    listen 80;
    server_name qwitty.ru www.qwitty.ru 83.220.171.20;
 
    root /home/user/qwitty/flask;
 
    access_log /home/user/qwitty/logsaccess.log;
    error_log /home/user/qwitty/logs/error.log;
 
    location / {
        proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        if (!-f $request_filename) {
            proxy_pass http://127.0.0.1:8000;
            break;
        }
    }
}


[Unit]
Description=Flask Gunicorn
After=syslog.target
After=network.target

[Service]
Type=simple
User=user
WorkingDirectory=/home/user/qwitty/flask
ExecStart=/home/user/env/bin/gunicorn main:app
RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target

sudo systemctl enable flask_gunicorn
sudo systemctl start flask_gunicorn
sudo systemctl status flask_gunicorn
