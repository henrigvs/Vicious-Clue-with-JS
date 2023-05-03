DROP TABLE IF EXISTS riddle_model;
DROP TABLE IF EXISTS clue;

CREATE TABLE riddle_model (
    riddle_id TEXT PRIMARY KEY,
    description TEXT NOT NULL,
    solution TEXT NOT NULL,
    difficulty INTEGER NOT NULL,
    category TEXT NOT NULL,
    fk_ownerId TEXT NOT NULL
);

CREATE TABLE clue (
    clue_id TEXT NOT NULL PRIMARY KEY,
    clue_description TEXT NOT NULL,
    fk_riddle_id TEXT NOT NULL,
    FOREIGN KEY (fk_riddle_id) REFERENCES riddle_model (riddle_id)
);
