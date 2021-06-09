## oTree Implementation of CEO Stance Experiment

### Table of Contents

[Project Title](#otree-implementation-of-ceo-stance-experiment)

[Table of Contents](#table-of-contents)

[Replication](#Replication)

[Usage](#usage)

[Contribute](#contribute)

[License](#license)


### Replication

Anyone can replicate this project using a new participant sample by cloning the repository, installing the requirements in requirements, and deploying the project to Heroku.

[(back to top)](#political-stance-tweets-project)

### Usage

There are two ways to access this experiment:

1. To demo the experiment:
  Create and activate a new virtual environment
  
  Clone this directory
  
  Change directory to path on your machine: e.g., ```$ cd CEOPolitics```
  
  Install requirements: ```$ pip install requirements.txt```
  
  Open devserver:```$ otree devserver```

2. To distribute this experiment on Heroku:
  Follow steps in 1. to ensure the demo works
  
  Create user profile on (heroku.com)[heroku.com]
  
  Enable web and worker dynos
  
  For < ~10,000 users, provision Heroku Redis Premium-0, Heroku Postgres Hobby Basic
  
  Create a profile on (oTreehub)[https://www.otreehub.com/]
  
  Deploy .otreezip file to Heroku and reset database
  

[(back to top)](#political-stance-tweets-project)

### Contribute

I welcome any commentary or contributions to improve this project.

[(back to top)](#political-stance-tweets-project)

### License
Use of this project is governed under the MIT License.

[MIT License](https://opensource.org/licenses/MIT)

[(back to top)](#political-stance-tweets-project)
