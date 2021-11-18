# Takehome assigment 2021
Submission date: 12nd of December.

**Important**
* Do __NOT__ edit .gitlab-ci.yml
* Do __NOT__ edit docker-compose.override.yml
* Do __NOT__ edit the .html files
* Name your services, network, and other named objects exactly as described in this document
* Place both CA Certificate and your Site Certificate in `/etc/nginx/ssl`


In this assignment you will create a database solution behind a TLS proxy. In other words the containers serving the webpage and handling the backend database will not have to deal with encryption as this is handled by the proxy. The proxy also serves as a load balancer to increase the scalability of the solution.

The application seen from the user is a web page from where you can insert or show names in a database. Although this functionality is very simple, it demonstrates a powerful principle. The webpages are provided, but the rest is up to you to build and connect. Appendix A shows how the containers should communicate.

The solution will be built and tested automatically. This is also a powerful principle used in some form by most companies and using it will be an important competence for you in the future. You can test your solution as many times as you want and only the last one will count towards the exam. This way you know when your solution lives up to the requirements and a failing test will give you feedback on what parts need to be improved.

We have automated most of the setup process, but you will need to familiarise yourself with git in order to upload your code. We recommend that you split the assignment into smaller parts that are more manageable to solve and test. It is ok to discuss the solution and to receive help from instructors or fellow students, but you have to make your own solution and we will check for plagiarism so do not give your solution to anyone. Have fun!



## Requirements
The assignment is to build and setup three containers. We will call them `proxy`, `backend` and `database` although other names could be argued for. The exact requirements for the containers and the network between them are listed below. It is important that you stick to the requirements in order to succeed the automated tests.
Your need your project to pass ALL test before the submission date.


### proxy
* `proxy` must communicate with the Actor over https, meaning nginx should terminate the TLS connection.
* `proxy` must serve two html files which are provided in the GitHub repository:
    * `insert.html`
    * `select.html`
* `proxy` must proxy POST /person/ and GET /persons/ to `backend`


### Backend
* `backend` must interact with `database`. How, is for you to decide and you can use whatever programming language to setup the web server, but we can only guarantee to be able to help with Python Flask servers.
* `backend` should serve two API endpoints:
    * `POST /person/`
        * `/person/` must take input from the insert.html form (See Figure 1)
    * `GET /persons/`
        * `/persons/` must return the result from the database in JSON. (See Listing 1)


### Database
* `Database` should be a mysql-container
* `Database` should have one table that contains three columns: An automatically incremented integer called 'PersonID' and two text fields called 'Firstname' and 'Lastname'.


### Network
The network between the containers must be split into two seperate networks, making it impossible for the `proxy` to interact directly with the `database`. This means that the `proxy` and the `backend` are the only containers on `network1`, and the `backend` and the `database` the only containers on `network2`

## Appendix

### Appendix A: Figure 1
![Sequence diagram, showing the insertion of a person](/assets/images/seqDiaIns.svg)

### Appendix B: Figure 2
![Sequence diagram, showing the selection of persons](/assets/images/seqDiaSel.svg)


### Appendix C: Listing 1
~~~json
[
  {
    "Firstname": "Mads",
    "PersonID": 1,
    "Lastname": "Jensen"
  },
  {
    "Firstname": "Mathias",
    "PersonID": 2,
    "Lastname": "Neerup"
  }
]
~~~