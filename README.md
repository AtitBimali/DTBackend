
# DT Backend WebDev Challenges

A brief description of the API endpoints.

Base URL: ```/api/v3/app/events/ ```
### API Documentation: - [Postman Link](https://documenter.getpostman.com/view/25025161/2s93eR5Fsn)

### Challenge Link: [Google Sheet](https://docs.google.com/spreadsheets/d/1pBt5QBZ6CRDo34w4alM7AQnbLd7T_AHGUTOs3NwNMu4/edit?usp=sharing)


## Installation

Install the requirements with pip

```bash
pip install -r requirements.txt
```

## Running the server

```bash
python3 manage.py runserver
```

    
## API Reference

#### Get all Events
```http
  GET /api/v3/app/events/
```

#### Get single event

```http
  GET /api/v3/app/events/{{event_id}}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `event_id`      | `integer` | **Required**. Id of event to fetch |


#### Update single event

```http
  PUT /api/v3/app/events/{{event_id}}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `event_id`      | `integer` | **Required**. Id of event to Update |

#### Delete single event

```http
  DELETE /api/v3/app/events/{{event_id}}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `event_id`      | `integer` | **Required**. Id of event to fetch |

#### Get Latest Events With Pagination

```http
  GET /api/v3/app/events/?page=2&limit=2&type=latest
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `page`      | `integer` | **Required**. Page number to fetch |
| `limit`      | `integer` | **Required**. Number of events to fetch per page |


## Frameworks Used

 - [Django](https://www.djangoproject.com/)
 - [Django Rest Framework](https://www.django-rest-framework.org/)


