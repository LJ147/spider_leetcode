#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by LJ on 2019-02-28

class dbFilter(object):
    def get_key_value_line(self, item):
        key_line = ''
        value_list = []
        for key, value in item.items():
            key_line += key + ','
            value_list.append(value)
        key_line = key_line.rstrip(',')
        return key_line, value_list

    def make_sql_line(self, table, key_line, value_list):
        count_vlaue = len(value_list)
        value_line = '%s,' * count_vlaue
        value_line = value_line.rstrip(',')
        sql_line = 'insert into {} ({}) values({})'.format(table, key_line, value_line)
        return sql_line

    def excute_sql(self, sql, value_list, cursor):
        cursor.execute(sql, value_list)
        # conn.commit()

    def get_rip_data(self, table, cursor, item, *args):
        if not args:
            return True
        conditions = []
        for key in args:
            exConditionLine = '{key} = "{value}"'.format(key=key, value=item[key])
            conditions.append(exConditionLine)
        conditionLine = ' and '.join(conditions)
        line = 'select * from {table} where {conditionLine}'.format(table=table, conditionLine=conditionLine)
        cursor.execute(line)
        if len(cursor.fetchall()) > 0:
            return False
        else:
            return True
if __name__ == '__main__':
    pass