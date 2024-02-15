const express = require('express');
const Pool = require('pg');
const fs = require('fs');
const toml = require('toml');

const app = express();
const port = 3000;

// 读取配置文件
fs.readFile('config.toml', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  try {
    // 解析 .toml 文件
    const parsedToml = toml.parse(data);
    console.log(parsedToml);
  } catch (error) {
    console.error('Error parsing TOML:', error);
  }
});

// 提取配置文件中的数据库配置信息
const databaseName = parsedToml.databases.database;
const databaseHost = parsedToml.databases.host;
const databaseUsername = parsedToml.databases.username;
const databasePassword = parsedToml.databases.password;

// PostgreSQL 连接配置
const pool = new Pool({
  user: databaseUsername,
  host: databaseHost,
  database: databaseName,
  password: databasePassword,
});
app.set('view engine', 'ejs');

app.use(urlencoded({ extended: true }));

app.get('/', async (req, res) => {
  try {
    const { rows } = await pool.query('SELECT * FROM your_table_name');
    res.render('index', { rows });
  } catch (err) {
    console.error('Error executing query', err.stack);
    res.status(500).send('Internal Server Error');
  }
});

app.post('/upload', async (req, res) => {
  const { data } = req.body;

  try {
    await pool.query('INSERT INTO your_table_name (data) VALUES ($1)', [data]);
    res.redirect('/');
  } catch (err) {
    console.error('Error executing query', err.stack);
    res.status(500).send('Internal Server Error');
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
