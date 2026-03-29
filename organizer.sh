#!/bin/bash


GRADES_FILE="grades.csv"
ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"


if [ ! -f "$GRADES_FILE" ]; then
    echo "error: '$GRADES_FILE' not found."
    exit 1
fi


if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
    echo "$ARCHIVE_DIR directory created."
fi


TIMESTAMP=$(date +"%Y%m%d-%H%M%S")


ARCHIVED_NAME="grades_${TIMESTAMP}.csv"


mv "$GRADES_FILE" "$ARCHIVE_DIR/$ARCHIVED_NAME"
echo "Archived: $GRADES_FILE to $ARCHIVE_DIR/$ARCHIVED_NAME"


touch "$GRADES_FILE"
echo "Reset: new '$GRADES_FILE' created."


echo "[$TIMESTAMP] $GRADES_FILE archived as $ARCHIVE_DIR/$ARCHIVED_NAME" >> "$LOG_FILE"
echo "logged to: $LOG_FILE"
