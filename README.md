## oTree Implementation of CEO Stance Experiment

### Table of Contents

[Project Title](#otree-implementation-of-ceo-stance-experiment)

[Table of Contents](#table-of-contents)

[Replication](#Replication)

[Usage](#usage)

[Contribute](#contribute)

[License](#license)


### Replication

Anyone can replicate this project using a new participant sample by cloning the repository, installing the requirements.txt, and deploying the project to Heroku.

[(back to top)](#political-stance-tweets-project)

### Usage

There are two ways to access this experiment:

**To demo the experiment:**  
    1. Create and activate a new virtual environment  
    2. Clone this directory  
    3. Change directory to path on your machine: e.g., ```$ cd CEOPolitics```  
    4. Install requirements: ```$ pip install requirements.txt```  
    5. Open devserver:```$ otree devserver```  

**To distribute this experiment on Heroku:**  
    1. Follow steps to demo the experiment to ensure the demo works  
    2. Create user profile on [heroku.com](heroku.com)  
    3. In the project's "Resources" tab, enable web and worker dynos  
    4. For < ~10,000 users, provision Heroku Redis Premium-0, Heroku Postgres Hobby Basic  
    5. Create a profile on [oTreehub](https://www.otreehub.com/)  
    6. Deploy .otreezip file to Heroku and reset database  
  

[(back to top)](#political-stance-tweets-project)

### Contribute

I welcome any commentary or contributions to improve this project.

[(back to top)](#political-stance-tweets-project)

### License
Use of this project is governed under the MIT License.

[MIT License](https://opensource.org/licenses/MIT)

[(back to top)](#political-stance-tweets-project)
