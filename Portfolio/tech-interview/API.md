#API Documentation

###Questions API: `api/questions/`

Provides API for `Stage` `Section` `Question` tables

* Get data from Questions API
	* List of data:
	Send list of data
	##### ```api/questions/sections```
	```json
	[
	  {
	    "id": 1,
	    "name": "section1"
	  },
	  {
	    "id": 2,
	    "name": "section2"
	  }
	]
	```
	##### ```api/questions/stages```
	```json
	[
		{
		"id": 1,
		"name": "stage1",
		"section": {
			"id": 1,
			"name": "newsection1"
			}
		},
		{
		"id": 2,
		"name": "stage2",
		"section": {
			"id": 1,
			"name": "newsection1"
			}
		}
	]
	```
	##### ```api/questions/questions```
	```json
	[
	  {
	    "id": 1,
	    "name": "question1",
	    "hint": null,
	    "stage": {
	      "id": 1,
	      "name": "stage1",
	      "section": {
	        "id": 1,
	        "name": "section1"
	      }
	    }
	  },
	  {
	    "id": 2,
	    "name": "question2",
	    "hint": null,
	    "stage": {
	      "id": 1,
	      "name": "stage1",
	      "section": {
	        "id": 1,
	        "name": "section1"
	      }
	    }
	  }
	]
	```
	
	* Specified data by id:
	##### ```api/questions/sections/1```
	```json
	  {
	    "id": 1,
	    "name": "section1"
	  }
	```
	##### ```api/questions/stages/1```
	```json
	{
		"id": 1,
		"name": "stage1",
		"section": {
			"id": 1,
			"name": "newsection1"
		}
	}
	```
	##### ```api/questions/questions/1```
	```json
	  {
	    "id": 1,
	    "name": "question1",
	    "hint": null,
	    "stage": {
	      "id": 1,
	      "name": "stage1",
	      "section": {
	        "id": 1,
	        "name": "section1"
	      }
	    }
	  }
	```
---
* Post or Put data to QuestionsAPI
	##### `api/questions/sections`
	```json
	{
	  "name": <value>
	}
	```
	##### `api/questions/stages`
	```json
	{
	  "name": <value>,
   "section": <section_name>
	}
	```
	##### `api/questions/questions`
	```json
	{
	  "name": <value>,
   "stage": <stage_name>
	}
	```
---
* Delete data
	* DELETE request to 
		##### `api/questions/sections/<id>`
		##### `api/questions/stages/<id>`
		##### `api/questions/questions/<id>`
---
---
---

###Departments API: `api/departments/`

Provides API for `Department` tables

* Get data from Departments API
	* List of data:
	Send list of data
	##### ```api/departments```
	```json
	[
	  {
     "id": 1,
	    "name": "department1",
	    "questions": [
	      {
	        "id": 1,
	        "name": "question1",
	        "hint": null,
	        "stage": {
	          "id": 1,
	          "name": "stage1",
	          "section": {
	            "id": 1,
	            "name": "section1"
	          }
	        }
	      },
	      {
	        "id": 2,
	        "name": "question2",
	        "hint": null,
	        "stage": {
	          "id": 1,
	          "name": "stage1",
	          "section": {
	            "id": 1,
	            "name": "newsection1"
	          }
	        }
	      }
	    ]
	  },
	  {
     "id": 2,
	    "name": "department2",
	    "questions": []
	  }
	]
	```
	
	* Specified data by id:
	##### ```api/departments/1```
	```json
	  {
     "id": 1,
	    "name": "department1",
	    "questions": [
	      {
	        "id": 1,
	        "name": "question1",
	        "hint": null,
	        "stage": {
	          "id": 1,
	          "name": "stage1",
	          "section": {
	            "id": 1,
	            "name": "section1"
	          }
	        }
	      },
	      {
	        "id": 2,
	        "name": "question2",
	        "hint": null,
	        "stage": {
	          "id": 1,
	          "name": "stage1",
	          "section": {
	            "id": 1,
	            "name": "newsection1"
	          }
	        }
	      }
	    ]
	  }
	```
---
* Post or Put data to DepartmentsAPI
	##### `api/questions/sections`
	```json
	{
	  "name": <value>,
   "questions": [<question_name>, <question_name>]
	}
	```
---
* Delete data
	* DELETE request to 
		##### `api/departments/<id>`
---
---
---

###Interviews API: `api/interviews/`

Provides API for `Interview` tables

* Get data from Departments API
	* List of data:
	Send list of data
	##### ```api/interviews```
	```json
	{
	  "recruiter": {
	    "auth": {
	      "id": 2,
	      "username": "recruiter",
	      "first_name": "",
	      "last_name": "",
	      "email": "recruiter@mail.com"
	    },
	    "role": {
	      "name": "recruiter",
	      "permissions": [
	        {
	          "name": "admin",
	          "code_name": "admin"
	        }
	      ]
	    }
	  },
	  "candidate": {
	    "auth": {
	      "id": 3,
	      "username": "candidate",
	      "first_name": "",
	      "last_name": "",
	      "email": "candidate@mail.com"
	    },
	    "role": {
	      "name": "recruiter",
	      "permissions": [
	        {
	          "name": "admin",
	          "code_name": "admin"
	        }
	      ]
	    }
	  },
	  "expert": {
	    "auth": {
	      "id": 4,
	      "username": "expert",
	      "first_name": "",
	      "last_name": "",
	      "email": "expert@mail.com"
	    },
	    "role": {
	      "name": "recruiter",
	      "permissions": [
	        {
	          "name": "admin",
	          "code_name": "admin"
	        }
	      ]
	    }
	  },
	  "department": {
	    "name": "1_department",
	    "questions": [
	      {
	        "name": "first_question",
	        "hint": "1111",
	        "stage": {
	          "name": "1_srage",
	          "section": {
	            "name": "1_section"
	          }
	        }
	      },
	      {
	        "name": "second_question",
	        "hint": "0000",
	        "stage": {
	          "name": "1_srage",
	          "section": {
	            "name": "1_section"
	          }
	        }
	      }
	    ]
	  },
	  "created_date": "2019-03-01T14:12:59.914059Z",
	  "status": "scheduled",
	  "interview_date": null,
	  "completion_date": null
	}
	```
	
	* Also it can be pecified by id:
	##### ```api/interviewss/1```
---
* Post or Put data to DepartmentsAPI
	##### `api/interviews`
	```json
	{
  	"candidate": <user_id>,
 	  "expert": <user_id>,
	  "department": <department_id>,
    "interview_date": <date>
      
   	
	}
	```
---
* Delete data
	* DELETE request to 
		##### `api/interviews/<id>`
---
---
---

###Feedback API: `api/feedback/`

Provides API for `Answers`, `Comments`, `Grades` tables

* List of data:
	Send list of grades
	##### ```api/feedback/grades```
	```json
	[
	  {
	    "id": 1,
	    "name": "None"
	  },
	  {
	    "id": 2,
	    "name": "Beginner"
	  }
	]
	```
Documentation in progress
---
