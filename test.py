import csv
from moengage.data.users.dao import UserDAO
from bson import ObjectId

def update_users_attribute(db_name, file_name, attribute_name):
    user_col = UserDAO(db_name=db_name)

    # Read the CSV file
    with open(file_name, 'r') as f:
        reader = csv.DictReader(f)

        failed_updates = []
        for row in reader:
            user_id = row['MoEngage_id']
            new_attribute_value = row[attribute_name]  # setting the attribute to the new value

            user = user_col.findOne({'_id': ObjectId(user_id)})

            if user:
                # Update the user attribute
                try:
                    user_col.update({'_id': user['_id']}, set_spec={attribute_name: new_attribute_value})
                    print(f"Updated user id {str(user['_id'])} with {attribute_name} = {new_attribute_value}")
                except Exception as e:
                    failed_updates.append((user_id, e))
            else:
                print("User Not found:", user_id)

        if failed_updates:
            print("Failed to update the following users:")
            for user_id, error in failed_updates:
                print(f"User id {user_id} - Error: {error}")

file_name = 'Testupdate.csv'              # Change input file name here - CSV file with exact User attributes as column name
db_name = 'Pilgrim'            # Change DB name here
attribute_name = 'u_mb'       # Replace with the actual attribute name you want to set to empty string - Confirm the key on Mongo

update_users_attribute(db_name, file_name, attribute_name)