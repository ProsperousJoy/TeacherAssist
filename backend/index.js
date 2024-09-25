import express from 'express';
import { PrismaClient } from '@prisma/client';
import bcrypt from 'bcrypt';
import 'dotenv/config';
import jwt from 'jsonwebtoken';
import { jwtValidator } from './middleware/Auth.js';
import axios from 'axios';

const prisma = new PrismaClient();
const app = express();
app.use(express.json());
app.use(express.urlencoded({extended: true}));

app.get('/users', async(req, res)=>{
    const users = await prisma.teacherAssist.findMany();
    res.json(users);
})

app.post('/login', async(req, res)=>{
    const {username, password} = req.body;
    const user = await prisma.teacherAssist.findFirst({
        where:{
            username: username,
        }
    })
    if(user){
        const isMatch = await bcrypt.compare(password, user.password);
        if(isMatch){
            const token = jwt.sign({id: user.id}, process.env.JWT_SECRET);
            res.json({message: `Login Successfull, Welcome ${user.fullname}`,
            token: token});
        }else{
            res.json({message: 'Invalid password'});
        }
    } else{
        res.json({message: 'User not found with this username'});
    }
})

app.post('/userRegister' ,async(req,res) =>{
    try {
        const {username,fullname, password, email} = req.body;

        const user = await prisma.teacherAssist.findFirst({
            where:{
                OR:[
                    {
                        username: username
                    },
                    {
                        email: email
                    }
                ]
            }
        })

        if(user){
            res.json({message: 'User already exists with this username or email'});
            return;
        }

        var hashPassword = await bcrypt.hash(password, 10);
        const insertData = await prisma.teacherAssist.create({
            data:{
                email: email,
                fullname: fullname,
                password: hashPassword,
                username: username,
            }
        })
        res.json(insertData);    
    } catch (error) {
        res.json({message: 'Error in registering user',
            error: error.message
        });
    }
    
})

app.post('/teacherInput',jwtValidator, async(req,res) =>{
    const {studytime, failures,absences,schoolsup,paid,health,G1,G2,G3,average, studentname} = req.body;
    const json = {
        studentname: studentname,
        studytime: parseInt(studytime),
        failures: parseInt(failures),
        absences: parseInt(absences),
        schoolsup: schoolsup === "true" ? true : false,
        paid: paid === "true" ? true : false,
        health: parseInt(health),
        G1: parseInt(G1),
        G2: parseInt(G2),
        G3: parseInt(G3),
        average: parseInt(average),
        prediction: 0
    };
    try {

        const studentData = await prisma.studentData.create({data: json});
        console.log(studentData);

        if(studentData){
            const predict = await axios.post('http://localhost:5000/predict', json, {
                headers: {
                    'Content-Type': 'application/json'
                }
            })

            const updateData = await prisma.studentData.update({
                where:{
                    id: studentData.id
                },
                data:{
                    prediction: predict.data.prediction
                }
            })

            res.json({message: 'Prediction Successfull',
                data: predict.data
            });
        }
    } catch (error) {
        res.json({message: 'Error input data', error: error.message});
        console.log(error)
    }
})

app.listen(3000,() =>{
    console.log('Server is running on port 3000');
})