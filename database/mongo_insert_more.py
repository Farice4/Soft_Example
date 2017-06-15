#!/bin/env python
import pymongo
import uuid
import datetime
import dateutil.parser

class Mongo(object):
    def __init__(self, host, user, pw):
        self.host = host
        self.user = user
        self.pw = pw

    def db_connect(self):
        conn = pymongo.Connection(self.host, 27017)
        #db = conn.ceilometer
        db = conn['ceilometer']
        db.authenticate(self.user, self.pw)
        return db

    def db_write(self):
        counter_name = ['cpu_util','memory.usage','bandwidth','disk.read.bytes.rate','disk.write.bytes.rate','disk.read.requests.rate','disk.write.requests.rate','network.incoming.bytes.rate','ntwork.outgong.bytes.rate','network.incoming.packets.rate','network.outgong.packets.rate']

        project_id = []
        for pi in range(1,5):
            project_id.append(str(uuid.uuid4()))

        resource_id = []
        for ri in range(1,4):
            resource_id.append(str(uuid.uuid4()))

        db = self.db_connect()
        meter = db.meter
        hour = 0
        while True:
            if hour < 10:
                for i in range(0,61):
                    for name in counter_name:
                        for pj in project_id:
                            for rs in resource_id:
                                if i <10:
                                    time_record = "2017-05-14T0%d:0%s:30.111Z" % (hour, i)
                                    #time_record = str(dateutil.parser.parser(time_record))
                                    time_record = dateutil.parser.parse(time_record)

                                elif i >=10 and i <60:
                                    time_record = "2017-05-14T0%d:%s:30.111Z" % (hour, i)
                                    #time_record = dateutil.parser.parser(time_record)
                                    time_record = dateutil.parser.parse(time_record)
                                meter.insert({"counter_name":name,"user_id":'null',"message_signature":"b9681a1af0476a70eff74e396afc815b68a433a1562205fbd410fcd45c88ea66","timestamp":time_record,"resource_id":rs,"resource_metadata":{},"source" :"openstack","counter_unit":"B","counter_volume":0,"recorded_at":time_record,"project_id":pj,"message_id":"3a2f9f06-4f36-11e7-b7a7-42c73e110a4c","counter_type":"gauge"})
                global hour
                hour += 1
                continue
            elif hour >= 10 and hour < 24:
                for i in range(0,61):
                    for name in counter_name:
                        for pj in project_id:
                            for rs in resource_id:
                                if i <10:
                                    time_record = "2017-05-14T%d:0%s:30.111Z" % (hour, i)
                                    #time_record = dateutil.parser.parser(time_record)
                                    time_record = dateutil.parser.parse(time_record)
                                elif i >=10 and i < 60:
                                    time_record = "2017-05-14T%d:%s:30.111Z" % (hour, i)
                                    #time_record = dateutil.parser.parser(time_record)
                                    time_record = dateutil.parser.parse(time_record)
                                meter.insert({"counter_name":name,"user_id":'null',"message_signature":"b9681a1af0476a70eff74e396afc815b68a433a1562205fbd410fcd45c88ea66","timestamp":time_record,"resource_id":rs,"resource_metadata":{},"source" :"openstack","counter_unit":"B","counter_volume":0,"recorded_at":time_record,"project_id":pj,"message_id":"3a2f9f06-4f36-11e7-b7a7-42c73e110a4c","counter_type":"gauge"})
                global hour
                hour += 1
                continue

            else:
                break

    def db_select(self):
        db = self.db_connect()
        print  db.meter.count()


def main():
    m = Mongo('127.0.0.1', 'ceilometer', 'ceilometer')
    m.db_write()
    m.db_select()

if __name__ == '__main__':
    main()
