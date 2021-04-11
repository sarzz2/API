# ``/challenges/weekly``

- [POST ``/challenges/weekly``](#post-new-weekly-challenge)
- [GET ``/challenges/weekly/<id>``](#get-weekly-challengeid)
- [PATCH ``/challenges/weekly/<id>``](#patch-weekly-challengeid)
- [DELETE ``/challenges/weekly/<id>``](#delete-weekly-challengeid)


## POST ``/challenges/weekly``

Create a weekly challenge from the request body.

### Parameters

**Location:** ``body``

Parameter | Type | Description
--------- | ---- | -----------
id | ``str`` or ``int`` | The  challenge's ID
title | ``str`` | The challenge's name
description | ``str`` | The challenge's description
examples | ``str`` | The challenge's examples
rules |  ``str`` | The challenge's rules
difficulty |  ``str`` | Difficulty of the challenge

#### Example request data

```json
 {
        "id": "1",
        "title": "title",
        "description": "this is a test",
        "examples": "x = 1",
        "rules": "work",
        "difficulty": "easy"
    }
```

### Returned data

Returns the created weekly challenge.

Parameter | Type | Description
--------- | ---- | -----------
id | ``str`` or ``int`` | The  challenge's ID
title | ``str`` | The challenge's name
description | ``str`` | The challenge's description
examples | ``str`` | The challenge's examples
rules |  ``str`` | The challenge's rules
created_by |  ``str`` | The author of the challenge
difficulty |  ``str`` | Difficulty of the challenge

#### Example response data

```json
{
    "created_by": "576760984576983060",
    "description": "this is a test",
    "difficulty": "easy",
    "examples": "x = 1",
    "id": "1",
    "rules": "work",
    "title": "title"
}
```

### Status codes

- ``201`` Created  
  The weekly challenge was created in the database.

- ``400`` Bad Request  
  Missing a required parameter.

- ``409`` Conflict  
  A weekly challenge with the provided ID already exists.

## GET ``/challenges/weekly/<id>``

Gets a weekly challenge from its ID.

### Parameters

**Location:** ``url``

Parameter | Type | Description
--------- | ---- | -----------
id | ``int`` | The weekly challenge's ID

#### Example request data

```http
/challenges/weekly/1
```

### Returned data

Returns the weekly challenge.

Parameter | Type | Description
--------- | ---- | -----------
id | ``str`` or ``int`` | The  challenge's ID
title | ``str`` | The challenge's name
description | ``str`` | The challenge's description
examples | ``str`` | The challenge's examples
rules |  ``str`` | The challenge's rules
created_by |  ``str`` | The author of the challenge
difficulty |  ``str`` | Difficulty of the challenge

#### Example response data

```json
{
    "created_by": "576760984576983060",
    "description": "this is a test",
    "difficulty": "easy",
    "examples": "x = 1",
    "id": 1,
    "rules": "work",
    "title": "title"
}
```

### Status codes

- ``200`` Success  
  The weekly challenge is returned.

- ``404`` Not found  
  Weekly challenge with provided ID doesn't exist.

## PATCH ``/challenges/weekly/<id>``

Update elements of a weekly challenge from the request body.

### Parameters

**Location:** ``url``

Parameter | Type | Description
--------- | ---- | -----------
id | ``int`` | The weekly challenge's ID

**Location:** ``body``

Parameter | Type | Description
--------- | ---- | -----------
title | ``str`` | The challenge's name
description | ``str`` | The challenge's description
examples | ``str`` | The challenge's examples
rules |  ``str`` | The challenge's rules
difficulty |  ``str`` | Difficulty of the challenge
#### Example request data

```http
/challenges/weekly/1
```

```json
 {
    "description": "this is a test",
    "difficulty": "medium",
    "examples": "x = 1",
    "id": 1,
    "rules": "work",
    "title": "title 2"
    }
```

### Returned data

Returns the updated weekly challenge.

Parameter | Type | Description
--------- | ---- | -----------
id | ``str`` or ``int`` | The  challenge's ID
title | ``str`` | The challenge's name
description | ``str`` | The challenge's description
examples | ``str`` | The challenge's examples
rules |  ``str`` | The challenge's rules
created_by |  ``str`` | The author of the challenge
difficulty |  ``str`` | Difficulty of the challenge

#### Example response data

```json
 {
        "id": "1",
        "title": "title2",
        "difficulty": "medium"
    }
```

### Status codes

- ``200`` Success  
  The weekly challenge was updated and is returned.

- ``404`` Not found  
  Weekly challenge with provided ID doesn't exist.

## DELETE ``/challenges/weekly/<id>``

Deletes a weekly challenge from its ID.

### Parameters

**Location:** ``url``

Parameter | Type | Description
--------- | ---- | -----------
id | ``int`` | The weekly challenge's ID

#### Example request data

```http
/challenges/weekly/1
```


#### Example response data

```json
[
    "challenge deleted",
    204
]
```

### Status codes

- ``200`` Success  
  The weekly challenge was deleted and is returned.

- ``404`` Not found  
  Weekly Challenge with provided ID doesn't exist.