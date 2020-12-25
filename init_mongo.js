db.createuser(
    {
        user: ${MONGO_USERNAME},
        pwd:  ${MONGO_PASSWORD},
        roles:[
            {
                role: "readWrite",
                db: ${MONGO_DB}
            }
        ]
    }
)