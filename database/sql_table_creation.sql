CREATE TABLE riddle_model (
    riddle_id TEXT PRIMARY KEY,
    description TEXT,
    solution TEXT,
    clue TEXT,
    difficulty INTEGER,
    fk_ownerId TEXT REFERENCES user_model(user_id)
);


CREATE TABLE user_model (
    user_id TEXT PRIMARY KEY,
    firstName TEXT,
    lastName TEXT,
    password TEXT,
    email TEXT,
    role TEXT,
    isConnected BOOLEAN
);
