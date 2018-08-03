ignore_tables = 'order_logs,user_logs'
mysqldump_option = ' --single-transaction'
mysqldump_option = mysqldump_option + ' --ignore_table=' + ' --ignore_table='.join(ignore_tables.split(','))
print(mysqldump_option)
