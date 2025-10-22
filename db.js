import express from 'express';
import pg from 'pg';

const { Pool } = pg;

const pool = new Pool({
    user: 'postgres',
    host: 'localhost',
    database: 'fixme',
    password: 'Passw0rd',
    port: 3000,
});

pool.connect().then(()=>console.log('Connected!')).catch(err=> console.err('Connection error',err.stack));

export default pool;