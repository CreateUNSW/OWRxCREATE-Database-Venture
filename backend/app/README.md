# Start backend: uvicorn main:app ---reload

Make sure you have the required environment variables in a .env file (example show below).

* JWT_SECRET="xxxxxxxxxxxxx"
* JWT_ALGORITHM="HS256"
* ACCESS_TOKEN_EXPIRE_MINUTES=15
* DATABASE_USERNAME="postgres"
* DATABASE_PASSWORD="password"