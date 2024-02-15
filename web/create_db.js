const{ Pool } = require('pg');
const fs = require('fs');
const toml = require('@iarna/toml');
const path = require('path');

// 读取配置文件
const confFilePath = path.join('..', 'config.toml');
const data = fs.readFileSync(confFilePath, 'utf-8')
const parsedToml = toml.parse(data)


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

// 生成指定范围内的随机整数
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }  

// 生成插入数据的 SQL 语句
function generateInsertQuery(name, id) {
  return `INSERT INTO students (name, id, sid) VALUES ('${name}', '${id}', '${sid}');`;
}

// 生成一堆插入 PostgreSQL 的数据
async function generateData() {
  try {
    const client = await pool.connect();

    // 循环生成 100 条数据
    for (let i = 1; i <= 50; i++) {
      const name = `User${i}`;
      const id = `${i.toString().padStart(2, '0')}`
      const sid = `202308${sid}`
      const query = generateInsertQuery(name, id, sid);

      // 执行插入数据的 SQL 语句
      await client.query(query);
      console.log(`Inserted data: ${name}, ${id}, ${sid}`);
    }

    client.release();
    console.log('All data inserted successfully!');
  } catch (err) {
    console.error('Error executing query', err.stack);
  }
}

// 调用生成数据的函数
generateData();
