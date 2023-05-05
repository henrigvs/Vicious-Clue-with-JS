ALTER TABLE riddle_model
ADD COLUMN correctAnswer INTEGER;

ALTER TABLE riddle_model
ADD COLUMN incorrectAnswers INTEGER;

ALTER TABLE riddle_model
ADD COLUMN clueRequested INTEGER;

ALTER TABLE riddle_model
ADD COLUMN consecutiveSeriesOfThree INTEGER;

UPDATE user_model
SET correctAnswer = 0,
    incorrectAnswers = 0,
    consecutiveSeriesOfThree = 0,
    clueRequested = 0
where user_id like '%%';