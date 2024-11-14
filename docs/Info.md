# Notes

## setup repo

### …or create a new repository on the command line

```bash
echo "# Sqlite_DB_python" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/shahnawazkcl/Sqlite_DB_python.git
git push -u origin main
```

### **…or push an existing repository from the command line**

```bash
git remote add origin https://github.com/shahnawazkcl/Sqlite_DB_python.git
git branch -M main
git push -u origin main
```

## Data types in SQL

- NULL
- INTEGER
- REAL
- TEXT
- BLOB: images, vidioes etc

## queying

- **fetch**: fetchone or fetchall/many gives us a list which can be indexed using `list[0]` etc.
