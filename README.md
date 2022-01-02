# BigData_CodeCompetition

Preconditions:
- Docker and docker-compose has to be installed 
- Port 8087 has to be freed or changed in docker-compose.yml
- Connection to DockerHub is required

How to Run: \
```docker-compose up -d```

How to Access: 

http://localhost:8087/d/q9fbeYT7k/codecompetition?orgId=1&kiosk


Do not: \
```docker-compose restart``` \
```Docker restart ...``` \
Otherwise the database would be loaded again and you have duplicate values.