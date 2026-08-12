
---

#         Introduction to NoSQL & MongoDB  
A comprehensive guide to understanding **NoSQL databases**, their types, benefits, and practical usage with **MongoDB**. This project serves as an educational resource for beginners and intermediate developers exploring modern database systems beyond traditional SQL.

---

##    Project Overview  
This project introduces the core concepts behind **NoSQL databases**, explains how they differ from SQL systems, and demonstrates how to perform CRUD operations using **MongoDB**, one of the most popular NoSQL document stores.

The content is based on official MongoDB documentation and educational tutorials.  
> “NoSQL is an approach to databases that represents a shift away from traditional relational database management systems… NoSQL databases do not rely on these structures and use more flexible data models.”  


MongoDB is highlighted as the primary example:  
> “MongoDB is a document-oriented and NoSQL database solution that provides great scalability and flexibility along with a powerful querying system.”  


---

##    Objectives  
- Understand what **NoSQL** means  
- Compare **SQL vs NoSQL**  
- Learn **ACID** properties  
- Explore **document storage**  
- Identify **NoSQL database types**  
- Understand **benefits of NoSQL**  
- Learn how to **query**, **insert**, **update**, and **delete** data  
- Learn how to **use MongoDB** (Shell + Python)  
- Install MongoDB on **WSL**, **Windows**, and **macOS**

---

##    Guiding Questions  
These are the exact questions this README answers:

1. **What NoSQL means?**  
2. **What is difference between SQL and NoSQL?**  
3. **What is ACID?**  
4. **What is a document storage?**  
5. **What are NoSQL types?**  
6. **What are benefits of a NoSQL database?**  
7. **How to query information from a NoSQL database?**  
8. **How to insert/update/delete information from a NoSQL database?**  
9. **How to use MongoDB?**

---

##    What NoSQL Means  
NoSQL means **“not SQL”** or **“not only SQL.”**  
It refers to databases that **do not use relational tables** and instead rely on **flexible data models** such as documents, key‑value pairs, graphs, or wide‑columns.

> “NoSQL databases do not rely on tables, columns, rows, or schemas… and use more flexible data models.”  


---

##    SQL vs NoSQL — Comparison  
| Feature | SQL | NoSQL |
|--------|------|--------|
| **Model** | Relational | Non‑relational |
| **Structure** | Tables, rows, columns | Documents, key‑value, graph, wide‑column |
| **Schema** | Strict | Dynamic |
| **Scalability** | Vertical | Horizontal |
| **ACID** | Fully supported | Partial (depends on DB) |
| **Best for** | Structured data | Unstructured / semi‑structured |

> “SQL databases use predefined and strict schema… NoSQL databases store heterogeneous and structureless data efficiently.”  


---

##    What Is ACID?  
ACID describes the reliability of database transactions:

- **Atomicity** — all or nothing  
- **Consistency** — valid state after transaction  
- **Isolation** — transactions don’t interfere  
- **Durability** — data persists after commit

---

##    What Is Document Storage?  
Document stores save data as **self‑describing documents** (JSON, BSON, XML).

> “Document databases typically store self-describing JSON, XML, and BSON documents… a value is a single document that stores all data related to a specific key.”  


MongoDB uses **BSON**, a binary JSON format.

---

##    Types of NoSQL Databases  
> “These fall into four main categories: key-value, document, wide-column, and graph stores.”  


### 1. Key‑Value Stores  
Simple, fast, flexible (Redis, Riak).

### 2. Document Stores  
JSON/BSON documents (MongoDB, CouchDB).

### 3. Wide‑Column Stores  
Column families (Cassandra, HBase).

### 4. Graph Stores  
Nodes + edges (Neo4j).

---

##    Benefits of NoSQL  
> “NoSQL databases offer scalability, performance, high availability, global availability, and flexible data modeling.”  


- **Horizontal scalability**  
- **High performance**  
- **High availability**  
- **Global distribution**  
- **Flexible schemas**  
- **Great for unstructured data**

---

##    Querying Data in MongoDB  
MongoDB uses JavaScript-like syntax.

### Find all  
```js
db.collection.find()
```

### Find with filter  
```js
db.collection.find({ author: "Joanna" })
```
> “db.tutorial.find({author: "Joanna"})…”  


### Aggregation  
```js
db.collection.aggregate([
  { $match: { status: "active" } },
  { $group: { _id: "$category", total: { $sum: 1 } } }
])
```

---

##    Insert / Update / Delete in MongoDB  
### Insert  
```js
db.collection.insertOne({ title: "New Tutorial" })
```

### Update  
```js
db.collection.updateOne(
  { author: "Jon" },
  { $set: { author: "Jonathan" } }
)
```

### Delete  
```js
db.collection.deleteOne({ author: "Joanna" })
```

> “mongosh supports insertOne, insertMany, updateOne, deleteOne…”  


---

##    Using MongoDB  
MongoDB can be used via:

### 1. **MongoDB Shell (mongosh)**  
> “Use the MongoDB Shell to test queries and interact with the data in your MongoDB database.”  


### 2. **Python (PyMongo)**  
```python
from pymongo import MongoClient
client = MongoClient()
db = client.mydatabase
db.users.insert_one({"name": "Krotos"})
```

> “MongoDB provides an official Python driver called PyMongo.”  


---

##    Installing MongoDB

###    WSL (Ubuntu)
```bash
sudo apt update
sudo apt install -y mongodb
sudo systemctl start mongodb
sudo systemctl enable mongodb
```

###    Windows  
> “Select the Windows platform… choose the .msi installer… run the installer and follow instructions.”  


Steps:  
1. Download MongoDB MSI  
2. Run installer  
3. Enable “Install MongoDB as a Service”  
4. Open **mongosh** from Start Menu

###    macOS (Homebrew)  
> “You can use Homebrew to install MongoDB on your system.”  


```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

---

##    References  
- MongoDB Documentation  
- RealPython — *Python and MongoDB*  
- Riak — *NoSQL Databases Explained*  
- Guru99 — *What is NoSQL?*  
- Derek Banas — *MongoDB Tutorial*  
- freeCodeCamp — *MongoDB Crash Course*

---

##    Conclusion  
NoSQL databases provide the flexibility, scalability, and performance required for modern applications. MongoDB stands out as a powerful, developer-friendly document store with rich querying capabilities and seamless integration with languages like Python.

This README gives you a complete foundation to understand NoSQL concepts and start working confidently with MongoDB.

---

### Author: Eugneio Martinez
