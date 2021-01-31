import csv, position, time


def sleep_writer(duration):
    duration = duration/30
    with open('position_val.csv', mode='w') as position_file:
        value_writer = csv.writer(position_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for x in range(1, 30):
            time.sleep(duration)
            value_writer.writerow([position.return_i2c()])


