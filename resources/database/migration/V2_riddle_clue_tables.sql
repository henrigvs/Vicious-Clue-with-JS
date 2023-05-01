DROP TABLE IF EXISTS riddle;
DROP TABLE IF EXISTS clue;

CREATE TABLE riddle (
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
    FOREIGN KEY (fk_riddle_id) REFERENCES riddle (riddle_id)
);
