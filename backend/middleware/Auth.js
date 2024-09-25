import jwt from 'jsonwebtoken';

const jwtValidator = (req,res,next) =>{
    const authHeader = req.headers['authorization'];
    if(!authHeader){
        res.status(401).json({message: 'No token provided'});
        return;
    }

    const token = authHeader.split(' ')[1];
    
    if(!token){
        res.status(402).json({message: 'No token provided'});
        return;
    }

    try {
        const verified = jwt.verify(token, process.env.JWT_SECRET);
        next();
    } catch (error) {
        res.status(401).json({message: 'Invalid token'});
    }
}

export {jwtValidator};