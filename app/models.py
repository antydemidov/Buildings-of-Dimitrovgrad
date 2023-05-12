# from werkzeug.security import generate_password_hash, check_password_hash
#
# class User(users):
#
#    def set_password(self, password):
#        self.password_hash = generate_password_hash(password)
#
#    def check_password(self, password):
#        return check_password_hash(self.password_hash, password)


# ADDRESS OBJECT
from app.mongodb_connection import BoD_db


class Addrobj_list:

    def get_data(limit: int, skip: int):
        main_keys = {
            'addrobj': ['NAME', 'TYPENAME', 'LEVEL']
        }
        db = BoD_db()
        addrobj_list = {}

        data = list(db.addrobj.find(
            filter={'ISACTIVE': '1'}, limit=limit, skip=skip))

        for item in data:
            item = dict(item)
            addrobj_list.update({item['OBJECTID']: {}})
            objectid = item['OBJECTID']
            for key, value in item.items():
                if key in main_keys['addrobj']:
                    addrobj_list[objectid].update({key: value})

        return addrobj_list


class Addrobj:

    def get_data(addrobj_objectid: str):
        main_keys = {
            'addrobj': ['OBJECTID', 'NAME', 'TYPENAME', 'LEVEL', 'PARENTOBJID', 'PATH'],
            'munhierarchy': ['OKTMO', 'PATH'],
            'addrobjparams': ['TYPEID', 'VALUE'],
            'paramtypes': ['NAME', 'DESC', 'CODE'],
            'houses': ['OBJECTID', 'HOUSENUM', 'HOUSETYPE'],
            'housesparams': ['TYPEID', 'VALUE'],
            'housetypes': ['NAME', 'SHORTNAME', 'DESC']
        }
        ADDROBJ_OBJECTID = addrobj_objectid
        db = BoD_db()
        obj = {}

        for key, value in db.addrobj.find_one({'OBJECTID': ADDROBJ_OBJECTID, 'ISACTIVE': '1'}).items():
            if key in main_keys['addrobj']:
                obj.update({str(key): str(value)})
        obj.update({'LEVEL_NAME': db.objectlevels.find_one(
            {'LEVEL': obj['LEVEL']})['NAME']})

        for key, value in db.munhierarchy.find_one({'OBJECTID': ADDROBJ_OBJECTID, 'ISACTIVE': '1'}).items():
            if key in main_keys['munhierarchy']:
                obj.update({str(key): str(value)})

        PARENTOBJID = db.munhierarchy.find_one(
            {'OBJECTID': ADDROBJ_OBJECTID, 'ISACTIVE': '1'})['PARENTOBJID']
        for key, value in db.addrobj.find_one({'OBJECTID': PARENTOBJID, 'ISACTIVE': '1'}).items():
            if key in main_keys['addrobj']:
                obj.update({'PARENT_' + str(key): str(value)})
        obj.update({'PARENT_LEVEL_NAME': db.objectlevels.find_one(
            {'LEVEL': obj['PARENT_LEVEL']})['NAME']})

        addrobjparams = list(db.addrobjparams.find(
            {'OBJECTID': ADDROBJ_OBJECTID}))
        paramtypes = db.paramtypes
        for i in range(len(addrobjparams)):
            for key, value in dict(addrobjparams[i]).items():
                if key in main_keys['addrobjparams']:
                    obj.update(
                        {'PARAM_' + str(i+1) + '_' + str(key): str(value)})
            for key, value in paramtypes.find_one({'ID': dict(addrobjparams[i])['TYPEID']}).items():
                if key in main_keys['paramtypes']:
                    obj.update(
                        {'PARAM_' + str(i+1) + '_' + str(key): str(value)})

        children = list(db.munhierarchy.find(
            {'PARENTOBJID': ADDROBJ_OBJECTID}))
        children_list = []
        for item in children:
            children_list.append(dict(item)['OBJECTID'])
        obj.update({'CHILDREN': children_list})

        return obj


class House_list:

    def get_data():
        pass


class House:

    def get_data(house_objectid: str):
        main_keys = {
            'addrobj': ['OBJECTID', 'NAME', 'TYPENAME', 'LEVEL', 'PARENTOBJID', 'PATH'],
            'munhierarchy': ['OKTMO', 'PATH'],
            'addrobjparams': ['TYPEID', 'VALUE'],
            'paramtypes': ['NAME', 'DESC', 'CODE'],
            'houses': ['OBJECTID', 'HOUSENUM', 'HOUSETYPE'],
            'housesparams': ['TYPEID', 'VALUE'],
            'housetypes': ['NAME', 'SHORTNAME', 'DESC']
        }
        db = BoD_db()
        HOUSE_OBJECTID = house_objectid
        obj = {}

        for key, value in db.houses.find_one({'OBJECTID': HOUSE_OBJECTID, 'ISACTIVE': '1'}).items():
            if key in main_keys['houses']:
                obj.update({str(key): str(value)})

        for key, value in db.housetypes.find_one({'ID': obj['HOUSETYPE'], 'ISACTIVE': 'true'}).items():
            if key in main_keys['housetypes']:
                obj.update({'HOUSETYPES_' + str(key): str(value)})

        for key, value in db.munhierarchy.find_one({'OBJECTID': HOUSE_OBJECTID, 'ISACTIVE': '1'}).items():
            if key in main_keys['munhierarchy']:
                obj.update({str(key): str(value)})

        PARENTOBJID = db.munhierarchy.find_one(
            {'OBJECTID': HOUSE_OBJECTID, 'ISACTIVE': '1'})['PARENTOBJID']
        for key, value in db.addrobj.find_one({'OBJECTID': PARENTOBJID, 'ISACTIVE': '1'}).items():
            if key in main_keys['addrobj']:
                obj.update({'PARENT_1_' + str(key): str(value)})
        obj.update({'PARENT_1_LEVEL_NAME': db.objectlevels.find_one(
            {'LEVEL': obj['PARENT_1_LEVEL']})['NAME']})

        PARENTOBJID = db.munhierarchy.find_one(
            {'OBJECTID': PARENTOBJID, 'ISACTIVE': '1'})['PARENTOBJID']
        for key, value in db.addrobj.find_one({'OBJECTID': PARENTOBJID, 'ISACTIVE': '1'}).items():
            if key in main_keys['addrobj']:
                obj.update({'PARENT_2_' + str(key): str(value)})
        obj.update({'PARENT_2_LEVEL_NAME': db.objectlevels.find_one(
            {'LEVEL': obj['PARENT_2_LEVEL']})['NAME']})

        PARENTOBJID = db.munhierarchy.find_one(
            {'OBJECTID': PARENTOBJID, 'ISACTIVE': '1'})['PARENTOBJID']
        for key, value in db.addrobj.find_one({'OBJECTID': PARENTOBJID, 'ISACTIVE': '1'}).items():
            if key in main_keys['addrobj']:
                obj.update({'PARENT_3_' + str(key): str(value)})
        obj.update({'PARENT_3_LEVEL_NAME': db.objectlevels.find_one(
            {'LEVEL': obj['PARENT_3_LEVEL']})['NAME']})

        housesparams = list(db.housesparams.find({'OBJECTID': HOUSE_OBJECTID}))
        paramtypes = db.paramtypes
        for i in range(len(housesparams)):
            for key, value in dict(housesparams[i]).items():
                if key in main_keys['housesparams']:
                    obj.update(
                        {'PARAM_' + str(i+1) + '_' + str(key): str(value)})
            for key, value in paramtypes.find_one({'ID': dict(housesparams[i])['TYPEID']}).items():
                if key in main_keys['paramtypes']:
                    obj.update(
                        {'PARAM_' + str(i+1) + '_' + str(key): str(value)})

        obj.update({'FULL_ADDRESS': obj['HOUSETYPES_SHORTNAME'] + ' ' + obj['HOUSENUM'] + ', ' + obj['PARENT_1_NAME'] +
                   ' ' + obj['PARENT_1_TYPENAME'] + '., ' + obj['PARENT_3_NAME'] + ', Российская Федерация'})

        return obj
