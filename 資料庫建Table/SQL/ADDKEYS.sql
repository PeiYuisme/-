ALTER TABLE `bs`
ADD CONSTRAINT `fk_seasons_id`
FOREIGN KEY (`seasonsID`) REFERENCES `seasons`(`seasonsID`)
ON DELETE CASCADE
ON UPDATE CASCADE;
