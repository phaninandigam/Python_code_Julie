from moengage.orm.dao.mongo.base import BaseDAO
from bson import ObjectId


conn = BaseDAO(database_name="MOEAttributes",collection_name="MOEAttributesConfig",cluster_type="meta")


def get_value():
 while True:
   try:
     value = int(input('Enter value for count_threshold: '))
     break
   except:
     print('Invalid input, please enter a number')
 return value


db_name = input('Enter the db_name: ')
existing_doc = conn.findOne({"db_name":db_name})
print(existing_doc)


if existing_doc:
 print('Doc exists in collection')
 for key in ['action', 'action_attribute', 'user_attribute']:
   try:
     count_threshold = existing_doc['attributes_config'][key].get('count_threshold', 'default value')
   except KeyError:
     count_threshold = 'default value'
   print(f'Existing count_threshold for {key}: ', count_threshold)
 if input('Do you want to edit the config? (Y/N)').lower() == 'y':
   for key in ['action', 'action_attribute', 'user_attribute']:
     if input(f'Do you want to update {key}? (Y/N)').lower() == 'y':
       existing_doc['attributes_config'][key]['count_threshold'] = get_value()
   existing_doc.pop("_id")
   print('Updating config with value...', existing_doc)
   conn.update({"_id":ObjectId(existing_doc.get("_id"))},existing_doc)
   print('Config updated successfully')
else:
 print('Doc does not exist in collection, inserting new doc')
 d = {
   "db_name": db_name,
   "attributes_config": {},
   "blacklisted_config": {}
 }
for key in ['action', 'action_attribute', 'user_attribute']:
    if input(f'Do you want to add count_threshold for {key}? (Y/N)').lower() == 'y':
     d["attributes_config"][key] = {"count_threshold": get_value()}
    else:
     d["attributes_config"][key] = {}


 conn.insert(d)
 print('Doc inserted successfully')
 print('After editing: ', conn.findOne({"db_name":db_name}))
