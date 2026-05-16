AUTH_VALID_SCHEMA = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "access_token": {
      "type": "string"
    },
    "refresh_token": {
      "type": "string"
    }
  },
  "required": [
    "access_token",
    "refresh_token"
  ]
}

AUTH_INVALID_SCHEMA = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "message": {
      "type": "string"
    },
    "statusCode": {
      "type": "number"
    }
  },
  "required": [
    "message",
    "statusCode"
  ]
}