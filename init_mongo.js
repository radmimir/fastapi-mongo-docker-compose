db.createuser(
    {
        user: "Admin",
        pwd:  "plarin_admin",
        roles:[
            {
                role: "readWrite",
                db: "employees"
            }
        ]
    }
)