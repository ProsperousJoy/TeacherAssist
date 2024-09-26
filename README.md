# TeacherAssist
Teacher Assistant tool made for Code For Impact 2024 Hackathon



## API (ENDPOINT LIST)

| Endpoint     |Require Token |Description |
| ----------- |----------- |----------- |
| /login          | |Login endpoint                                             |
| /userRegister   | |Register Teacher Account to Accsess the application        |
| /teacherInput   | :white_check_mark: |Teacher Input for predict the grade                        |
| /studentData    | :white_check_mark: |Get all student prediction data                            |

## Login Response

Login response when sucsess is give JWT token key.

```
{
    "message": "Login Successfull, Welcome Muhammad Jamal Com",
    "token": "<token>"
}
```