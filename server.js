import express from 'express';
import pool from './db.js';
import cors from 'cors';

const app = express();
const port = 3002;

app.use(express.json());
app.use(cors());
app.get('/users',async (req,res)=>{
    try{
        const result = await pool.query("SELECT * FROM users");
        res.json(result.rows);
    }catch(err){
        res.status(500).send({ error: 'Server Error'});
    }
});

app.post('/register',(req,res)=> {
    res.send('<h1>Registration Success</h1>');
});

app.listen(port,()=>{
    console.log(`Listening on port ${port}`);
});

export default app;