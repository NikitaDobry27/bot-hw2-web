# Python CLI Bot addressbook

Address Book Bot is a command-line application that helps you manage your contacts, notes, and birthdays. You can add, modify, and delete records, as well as search for contacts, notes, or tags. The bot also allows you to save and load records from a file, sort files, and find contacts with upcoming birthdays.

## **Commands and their usage**

### **Add**

- **`add record 'name'`**: Adds a new record with the specified name.
- **`add phone 'name' 'phone'`**: Add new phone to the record.
- **`add email 'name' 'email'`**: Add email to the record. Can be only one.
- **`add birthday 'name' 'birthday'`**: Add birthday to the record. Can be only one. Birthday format: dd-mm-yyyy.
- **`add note`**: Add note to the notebook.
- **`add tags`**: Add tag(s) to the note you'll choose from the notebook.

### **Change**

- **`change phone 'name' 'old phone' 'new phone'`**: Change old phone with new one.
- **`change email 'name' 'email'`**: Change email in the record.
- **`change birthday 'name' 'birthday'`**: Change birthday in the record. Birthday format: dd-mm-yyyy.
- **`change note`**: Change the note text.
- **`change note title`**: Change the note title.
- **`change tags`**: Change the tags for the chosen note.

### **Delete**

- **`del record 'name'`**: Delete record with specified name.
- **`del phone 'name' 'phone'`**: Delete phone from the record.
- **`del email 'name' 'email'`**: Delete email from the record.
- **`del birthday 'name' 'birthday'`**: Delete birthday from the record.
- **`del note`**: Delete the note from the notebook completely.
- **`del tags`**: Delete all tags from the note.

### **Other Commands**

- **`birthdays 'number of days'`**: Shows contacts who have a birthday in the specified number of days.
- **`# tag1 tag2...`**: Search by tags.

## **Setup**

To install the Address Book Bot, run the following command:

```bash
pip install git+https://github.com/NightSpring1/PythonCore_FinalProject_Team4
```

This will install the bot and its dependencies.

## **Usage**

To start the bot, run the following command:

```bash
bot-start
```

This will launch the command-line interface for the Address Book Bot. Enter your commands according to the usage instructions provided above.

For any issues or questions, please refer to the **[GitHub repository](https://github.com/NightSpring1/PythonCore_FinalProject_Team4)**.
