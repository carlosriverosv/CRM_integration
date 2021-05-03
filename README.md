# CRM Integration

_This project takes the principles of parallism   with python_

## Problem 📋

In a company X there is a custom-made CRM that its sales agents use in its daily basis. This system is a pipeline where leads could convert into prospects. In order to do that conversion the sales agents have to run manual checks to validate that the person is elegible to be a prospect in the company. The company needs to automate this process.

## Requirement 📋
It is necessary to integrate with other external systems and include the functionality in the CRM in order to let the sales agents to trigger those validations by demand.

Every lead stages with basical personal information. And the critieria to turn sales qualiafied lead into a prospect is to pass various validations with different systems

- The person should exists in the national registry identification (external system)
- The person does not have any judicial records in the national archives (external system)
- Our internal prospect qualification system gives a satisfactory score for that person. This system outputs a random score between 0 and 100. A lead could be turned into prospect if the score is greater than 60 


There are some considerations, the national registry request have to made in parallel with the judicial record requests. And the output have to pass by the internal prospect qualification.

## Analysis 🚀

### Improvements 🔧
There are some improvements that could be done
 
 - Improve and do a lot more of tests
 - Fake an invalid response from one or both of the external servers
 - Include some error handling in case of an invalid response
 

##Running the project  ⚙️

_The project have to dowload an run with the next commands_
`$ python main.py <person identifications>`

Ex:

`$ python main.py 123 456 789 `

After that you will see a response like this in the console

`started at 02:07:09
--------------------------------------------------
person id: 1, qualification result: 3
--------------------------------------------------
--------------------------------------------------
person id: 2, qualification result: 9
--------------------------------------------------
--------------------------------------------------
person id: 3, qualification result: 42
--------------------------------------------------
finished at 02:07:18`


##Running the tests  ⚙️

_The project have to dowload an run with the next commands_
`$ python -m unittest  discover -v`

