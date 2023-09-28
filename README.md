# PAD-project: Event planning application

## 1. Application suitability
 The event planning system is suitable for a microservices architecture because it involves various components, such as user management, event creation, guest invitations, task management, and more, which can be developed and maintained independently. As mentioned, distributed systems allow to scale specific components of the application independently. For example, during a popular event, it’s possible to scale the invitation management service to handle a large number of guest responses without affecting other parts of the application. This ensures that the application remains responsive even during peak usage
 ## 2. Service boundaries
* **User authentication service:**
  * Sign up (create user)
  * Login (authenticate user) 
  * Change password
  * See user profile
* **Event management service:** 
  * Create event
  * Update event details
  * Add participants
  * Remove participants
  * Delete event.

## 3. System design diagram
![](image.png)

## 4. Technology stack

**.NET for microservices:** .NET is a strong choice for building microservices due to its comprehensive ecosystem, cross-platform compatibility, performance, developer productivity, and security features. It supports multiple programming languages, offers scalability, and integrates well with other technologies and containerization, making it well-suited for modern microservices architectures.

**MSSQL Database for microservices:** MSSQL provides seamless integration with the .NET ecosystem, high performance, robust security features, and reliability. MSSQL is well-supported by Microsoft's development tools and offers compatibility with industry standards, making it a strong choice for building database-driven applications in the .NET framework.

**Java for API gateway:** Java is a favorable choice for implementing an API gateway due to its maturity (well-established, reliable, and proven over time), scalability, rich ecosystem, and strong security features. Its cross-platform compatibility, community support, and integration capabilities make it a reliable and customizable solution for managing, securing, and routing API requests in a microservices architecture.

## 5. Data management
  ### I. User authentication service

* Sign Up (Create User):
```
Endpoint: POST /api/login
Request Payload: {
   "username": "string (The user's username)",
   "password": "string (The user's password)"
}
Response (Successful): HTTP status code 200
Response (Unsuccessful): HTTP status code 401
```
* Login (Authenticate User): 
```
Endpoint: POST /api/changepassword
Request Payload: {
   "userId": "string or integer (Unique identifier for the user)",
   "currentPassword": "string (The user's current password)",
   "newPassword": "string (The user's new password)"
}
Response (Successful): HTTP status code 200
Response (Unsuccessful): HTTP status code 400
```

* Change Password:
```
Endpoint: POST /api/changepassword
Request Payload: {
   "userId": "string or integer (Unique identifier for the user)",
   "currentPassword": "string (The user's current password)",
   "newPassword": "string (The user's new password)"
}
Response (Successful): HTTP status code 200
Response (Unsuccessful): HTTP status code 400
```

* See user Profile:
```
Endpoint: POST /api/changepassword
Request Payload: {
   "userId": "string or integer (Unique identifier for the user)",
   "currentPassword": "string (The user's current password)",
   "newPassword": "string (The user's new password)"
}
Response (Successful): HTTP status code 200
Response (Unsuccessful): HTTP status code 400
```

   ### II.	 Creation and managing events service:
* Create Event:
```
Endpoint: POST /api/events
Request Payload: {
   "eventName": "string",
   "eventDescription": "string",
   "eventDetails": {
      "date": "string or date/time format",
      "location": "string",
      "dressCode": "string"
   }
}
Response (Successful): HTTP status code 201
Response (Unsuccessful): HTTP status code 400
```

* Update Event Details:
```
Endpoint: PUT /api/events/{eventId}
Request Parameters: {
   "eventId": "string or integer (Unique identifier for the event being updated)"
}
Request Payload: {
   "eventName": "string (Updated event name, optional)",
   "eventDescription": "string (Updated event description, optional)",
   "eventDetails": {
      "date": "string or date/time format (Updated event date and time, optional)",
      "location": "string (Updated event location, optional)",
      "dressCode": "string (Updated dress code, optional)"
   }
}
Response (Successful): HTTP status code 200
Response (Unsuccessful): HTTP status code 404 or 400
```

* Add Participants:
```
Endpoint: POST /api/events/{eventId}/participants
Request Parameters: {
   "eventId": "string or integer (Unique identifier for the event)"
}
Request Payload: {
   "participantId": "string or integer (Unique identifier for the user to be added as a participant)"
}
Response (Successful): HTTP status code 201
Response (Unsuccessful): HTTP status code 404 or 400

```

* Remove Participants:
```
Endpoint: DELETE /api/events/{eventId}/participants/{participantId}
Request Parameters: {
   "eventId": "string or integer (Unique identifier for the event)",
   "participantId": "string or integer (Unique identifier for the user to be removed as a participant)"
}
Response (Successful): HTTP status code 204
Response (Unsuccessful): HTTP status code 404 or 400

```
* Delete Event:
```
Endpoint: DELETE /api/events/{eventId}
Request Parameters: {
   "eventId": "string or integer (Unique identifier for the event to be deleted)"
}
Response (Successful): HTTP status code 204
Response (Unsuccessful): HTTP status code 404
```

## 6. Deployment and scaling
**Docker** is valuable for deployment and scaling due to its containerization technology, providing isolation, portability, and consistency. It enables efficient resource utilization and seamless horizontal scaling using container orchestration tools. Docker's version control, dependency management, and security features further streamline the deployment process, making it a popular choice for modern application development and operations.