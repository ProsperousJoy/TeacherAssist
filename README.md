# TeacherAssist
Teacher Assistant tool made for Code For Impact 2024 Hackathon



## API (ENDPOINT LIST)

| Endpoint     | Description |
| ----------- | ----------- |
| /login          | Login endpoint                                             |
| /userRegister   | Register Teacher Account to Accsess the application        |
| /teacherInput   | Teacher Input for predict the grade                        |
| /studentData    | Get all student prediction data                            |

## Login Response

Login response when sucsess is give JWT token key.

```
{
    "message": "Login Successfull, Welcome Muhammad Jamal Com",
    "token": "<token>"
}
```