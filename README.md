# Assignment Analysis
## Objective
- website that accept data uploaded in a CSV format, and represent it in a visual way.

## Logic
- **Adjacency Matrix:**
    - graph vertices, with a 1 or 0 in position (v_i,v_j) according to whether v_i and v_j are adjacent or not.
    - For a simple graph with no self-loops, the adjacency matrix must have 0s on the diagonal
    - The adjacency matrix is a matrix of ones and zeros where a one indicates the presence of a connection. 
- **Handling Data**
    - CSV to be parsed inro json object
    - length of the json object
    - number of zeros and ones
    - one = edge from j to i
    - N nodes = N * N
    - each node corresponds to an activity

## tools to be used
  - ### Front-End:
    - HTML
    - Css
    - Bootstrap
    - Js/Dom
  - ### Back-End
    - Python
      - Django
      - chart.js with django
      - **Resources**
        - [chart.js with django](https://www.youtube.com/watch?v=B4Vmm3yZPgc&list=PLiT3w9BVkqvFgCyiCHpPtVdOP1nqQ03G4)
    - JavaScript
      - Node.js

## Milestones
  - [ ] Front End upload interface
  - [ ] Fetch the data and print them in json format
  - [ ] handle the data to see back visualization
  - [ ] Show Tasks in a modern way
### what to do
  - [x] create git repo
  - [x] Setup Work Environment
    - [x] HTML, CSS, JS
    - [x] install django
  - [ ] basic fronend interface


### Commands Used
```
$ pip install Django==4.0.2
$ python -m pip install --upgrade pip
$ source nodesApp/Scripts/activate
$ django-admin startproject nodesApp .
$ python manage.py runserver
$ python manage.py migrate
```

### Issues Faced
- Path issues and pip freeze error
- python launcher
- version od python and launcher must match