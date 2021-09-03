# OWRxCREATE-Database-Venture

## Git - How to start
1. Do not work on the main branch directly. Always work on branches other than the main branch.
2. Git pull from main for latest changes on all files.
3. Git push your changes to your working branch.
4. Always submit a pull request if you want to merge the changes (from your working branch) into the main branch. 
5. Someone else will review your pull request and approve it.

## Backend

### Virtual Environment
For now we're using `pipenv` for the python virtual environment for development. To build this environment:
1. Clone the repo
2. Move into the backend repo: `cd backend`
3. Assuming you have python installed etc.; user install `pipenv` with `pip`: `pip install --user pipenv`
4. Install the required python packages: `pipenv install`
5. Finally, activate the virtual environment: `pipenv shell`
Further documentation on `pipenv` may be found [here](https://pipenv.pypa.io/en/latest/)

### Running the uvicorn server
For now we're using FastAPI to build the API (surprise surprise). You run the server by running `uvicorn main:app --reload` in the `backend/app` directory. This will run the server on some localhost address like `http://127.0.0.1:8000`. The nifty Swagger docs page can then be accessed at `http://127.0.0.1:8000/docs`.

## Frontend