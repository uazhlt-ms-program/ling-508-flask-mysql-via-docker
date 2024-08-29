CREATE DATABASE lexicon;
ALTER DATABASE lexicon CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use lexicon;

CREATE TABLE lexentries (
    written_form VARCHAR(30),
    pronunciation NVARCHAR(40),
    pos ENUM('noun', 'verb', 'adv', 'adj', 'adp', 'det'),
    definition VARCHAR(300));

INSERT INTO lexentries
(written_form, pronunciation, pos, definition)
VALUES
('coffee', N'ˈkʰɔ.fi', 'noun', 'boiled bean water'),
('drink', N'dɹɪŋk','verb','to imbibe');

