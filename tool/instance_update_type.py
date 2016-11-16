import MySQLdb
import sys

# DATABASE_PWD and DB_HOST must update, data from /etc/nova/nova.conf
# database connect value "connection="
DATABASE_PWD =  "dc91e19c23ad41ec"
DB_HOST = "localhost"

def instance_select(cursor, uuid):
    """database instance os_type data display"""

    sql = """select uuid, os_type from instances where uuid='%s'""" % uuid
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        return data
    except  Exception as e:
        print "Data  query error, %s" % e

def instance_update(cursor, db, uuid):
    """database instance os_type data update"""

    sql = """update instances set os_type='windows' where uuid='%s'""" % uuid
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print "Data update error, %s" % e
        db.rollback()

def main():
    # init database connection
    try:
        db = MySQLdb.connect(DB_HOST, "nova", DATABASE_PWD, "nova")
        cursor = db.cursor()
    except Exception as e:
        print "Mysql connect error, %s" % e
        sys.exit()

    # instance uuid input
    uuid = sys.argv[1]
    # uuid query
    os_type_status = instance_select(cursor, uuid)
    # uuid error or uuid don't exist program exit
    if os_type_status == None:
        print 'Input uuid error,uuid is: %s, please check uuid' % uuid
        cursor.close()
        db.close()
        sys.exit()

    print 'Instances %s os_type is %s' % (os_type_status[0], os_type_status[1])

    if os_type_status[1] != 'windows':
        # start update instance 
        print 'Instance will be update os_type'
        instance_update(cursor, db, uuid)
        update_status = instance_select(cursor, uuid)

        if  update_status[1] == 'windows':
            print 'Instance os_type is: %s' %  update_status[1]
            print 'Instance os_type update success'
    elif os_type_status[1] == 'windows':
        print 'Instance os_type status has been right'

    cursor.close()
    db.close()

if __name__ == '__main__':
    main()
